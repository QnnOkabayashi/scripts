echo "Select your SD card"

volumes=() len=0
while IFS=  read -r -d $'\0'; do
    if [ $len -ne 0 ]
    then
        volumes+=("$REPLY")
        echo $len: $REPLY
    fi
    ((len++))
done < <(find /Volumes -print0 -maxdepth 1)
((len--)) 

read user_input

num_id=$(($user_input - 1))

if [[ $num_id -lt 0 || $num_id -ge $i ]]
then
    echo "Invalid directory choice: $user_input"
    exit 1
fi

sd_path=${volumes[$num_id]}

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
