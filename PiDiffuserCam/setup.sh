echo "Beginning PiDiffuserCam installation..."

echo "Updating..."
sudo apt-get update &>/dev/null

echo "Installing Git and PiCamera..."
sudo apt-get install git python3-picamera &>/dev/null

echo "Cloning project repo..."
git clone https://github.com/QnnOkabayashi/PiDiffuserCam.git /home/$(whoami)/PiDiffuserCam &>/dev/null

echo "Finished PiDiffuserCam installation."