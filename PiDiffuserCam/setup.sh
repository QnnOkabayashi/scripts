echo "Beginning PiDiffuserCam installation..."

echo "Updating..."
sudo apt-get update

echo "Installing Git and PiCamera..."
sudo apt-get install git python3-picamera

echo "Cloning project repo..."
git clone https://github.com/QnnOkabayashi/PiDiffuserCam.git /home/$(whoami)/PiDiffuserCam

echo "Enabling camera module..."
sudo raspi-config nonint do_camera 0

echo "Rebooting..."
sudo reboot