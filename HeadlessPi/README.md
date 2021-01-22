# HeadlessPi
Quinn Okabayashi
___
This page streamlines the process of configuring your Raspberry Pi for [headless operation](https://en.wikipedia.org/wiki/Headless_computer).

Currently only Mac OS is supported.
___
## Flashing the OS image
Insert an unused micro SD card into your machine, and enter the following command:

```
$ python3 -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/QnnOkabayashi/scripts/master/HeadlessPi/setup.py').read())"
```

> Warning: You should always verify that scripts from URLs are safe before running! Check out the source code below yourself.

[Source code](https://github.com/QnnOkabayashi/scripts/blob/master/HeadlessPi/setup.py)

This will:
1. Prompt you to select a drive to format
2. Flash Raspberry Pi OS Lite (32-bit) to it
3. Prompt you for WiFi credentials
4. Enable SSH via WiFi for the Pi
5. Safely eject the drive

You may now remove the micro SD card and insert it into your Raspberry Pi.
___
## Connecting via SSH
1. When your Pi is powered on, open your terminal and enter the following:
    ```
    $ ssh pi@raspberrypi.local
    ```

2. If this is the first time connecting, you will see a message like the following, which you need to allow:
    ```
    The authenticity of host 'raspberrypi.local (xxxx:xxx:xxxx:xxxx::xxxx)' can't be established.
    ECDSA key fingerprint is SHA256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
    Are you sure you want to continue connecting (yes/no/[fingerprint])?
    ```

3. It will then prompt you for the password, which is `raspberry` by default.

4. To disconnect from the SSH, use the `exit` command.

