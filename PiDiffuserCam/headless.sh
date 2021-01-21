echo 'Enter the path to your SD card:'

read sd_path

if [ ! -w $sd_path ]
then
    echo "Directory doesn't exist: $sd_path"
    exit 1
fi

echo "Enter your WiFi SSID:"

read ssid

echo "Enter your WiFi password:"

read pass

echo "Initializing headless mode..."

touch ${sd_path}/ssh
touch ${sd_path}/wpa_supplicant.conf

echo $"country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    scan_ssid=1
    ssid=\"$ssid\"
    psk=\"$pass\"
}" > ${sd_path}/wpa_supplicant.conf

echo "Initialization complete. You may eject the SD card."
