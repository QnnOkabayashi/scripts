echo "Beginning PiDiffuserCam installation..."

sudo apt-get update
sudo apt-get install git python3-picamera

git clone https://github.com/QnnOkabayashi/PiDiffuserCam.git /home/$(whoami)/PiDiffuserCam

echo "Finished PiDiffuserCam installation."