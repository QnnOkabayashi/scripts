echo "Updating..."
sudo apt-get update

echo "Installing Git, PiCamera, and RealVNC. This may take awhile..."
sudo apt-get install git python3-picamera realvnc-vnc-server

echo "Cloning project repo..."
git clone https://github.com/QnnOkabayashi/PiDiffuserCam.git /home/$(whoami)/PiDiffuserCam

echo "Enabling camera module..."
sudo raspi-config nonint do_camera 0

echo "Enabling RealVNC..."
sudo raspi-config nonint do_vnc 0

echo "Enabling experimental capture mode in RealVNC..."
sudo -s <<HERE
echo "CaptureTech=raspi" >> /root/.vnc/config.d/vncserver-x11
HERE

# https://stackoverflow.com/a/13322549/12401179
echo "Your VNC IP address is: $(ifconfig wlan0 | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')"

echo "Rebooting..."
sudo reboot