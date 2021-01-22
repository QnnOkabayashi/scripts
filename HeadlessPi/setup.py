'''
python3 -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/QnnOkabayashi/scripts/master/HeadlessPi/setup.py').read())"
'''

import os, subprocess, zipfile, urllib.request

def get_disk_choice() -> str:
    list_cmd = 'diskutil list'

    out = (subprocess
        .run(list_cmd.split(), capture_output=True)
        .stdout
        .decode('utf-8')
    )

    disks = [line.split('*')[1].rsplit(maxsplit=1)
        for disk in out.split('\n\n')   # loop through each "disk" section that's physical
        if '(external, physical)' in disk
        for line in disk.split('\n')    # find line representing entire disk
        if '*' in line
    ]

    if len(disks) == 0:
        exit('You have no external drives connected')

    print("Select your SD card (0 to exit)")
    for i, (size, name) in enumerate(disks):
        print(f'{i + 1}: {name}\t{size}')

    user_choice = input('Disk ID: ')
    try:
        id = int(user_choice)
        if id == 0:
            exit('No volume selected')
        elif id > len(disks):
            exit(f'Disk ID is too large: {id}')
        elif id < 0:
            exit(f'Disk ID cannot be negative: {id}')
    except ValueError:
        exit(f'Invalid disk ID: {user_choice}')

    disk_name = disks[id - 1][1]

    return disk_name


def unmount_disk(disk_path: str):
    print(f'Unmounting {disk_path}...')

    unmount_cmd = f'sudo diskutil unmountDisk {disk_path}'

    subprocess.run(unmount_cmd.split(), capture_output=True)


def flash_rpi_os(rdisk_path: str):
    print('Downloading OS image. This may take awhile...')

    image_url = 'https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2021-01-12/2021-01-11-raspios-buster-armhf-lite.zip'

    zip_path, _ = urllib.request.urlretrieve(image_url)

    with zipfile.ZipFile(zip_path, 'r') as f:
        f.extractall('/tmp')

    image_path = '/tmp/2021-01-11-raspios-buster-armhf-lite.img'

    print('Flashing Raspberry Pi OS Lite (32-bit). This may take awhile...')

    flash_cmd = f'sudo dd bs=1m if={image_path} of={rdisk_path}'

    err = (subprocess
        .run(flash_cmd.split(), capture_output=True)
        .stderr
        .decode('utf-8')
    )

    subprocess.run(['sync'])

    if 'Operation not permitted' in err:
        exit('Volumes cannot access terminal. Enable at System Preferences > Security & Privacy > Privacy > Files and Folders, and give removable volumes access to Terminal.')
    elif 'Permission denied' in err:
        print('Permission was denied, so clearing and trying again')
        erase_cmd = f'sudo diskutil partitionDisk {rdisk_path} 1 MBR "Free Space" "%noformat%" 100%'

        subprocess.run(erase_cmd.split())

        subprocess.run(flash_cmd.split())
    elif 'bytes transferred in' not in err:
        exit(f'An error occurred:\n{err}')

    os.remove(image_path)


def enable_ssh_and_wifi():
    print('Enabling SSH via WiFi')

    ssid = input('Enter your WiFi SSID: ')
    password = input('Enter your WiFi password: ')

    with open('/Volumes/boot/ssh', 'w') as f:
        pass

    with open('/Volumes/boot/wpa_supplicant.conf', 'w') as f:
        f.write(f'''country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={{
    scan_ssid=1
    ssid="{ssid}"
    psk="{password}"
}}''')


def eject_sd_card(rdisk_path: str):
    eject_cmd = f'sudo diskutil eject {rdisk_path}'

    err = (subprocess
        .run(eject_cmd.split(), capture_output=True)
        .stderr
        .decode('utf-8')
    )

    if 'Volume failed to eject' in err:
        print('The volume could not be ejected because it is in use, but all necessary contents are written')
    else:
        print('You may now eject the SD card')


if __name__ == '__main__':
    disk_name = get_disk_choice()

    disk_path = f'/dev/{disk_name}'
    rdisk_path = f'/dev/r{disk_name}'

    unmount_disk(disk_path)

    flash_rpi_os(rdisk_path)

    enable_ssh_and_wifi()

    eject_sd_card(rdisk_path)

