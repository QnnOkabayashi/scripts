# PiDiffuserCam Setup
Quinn Okabayashi and Josh Vandervelde
___
This script streamlines the process of configuring our [PiDiffuserCam code](https://github.com/QnnOkabayashi/PiDiffuserCam).

Currently only Mac OS is supported.
___
## Configure SSH on your Raspberry Pi
Follow the instructions [here](https://github.com/QnnOkabayashi/scripts/blob/master/HeadlessPi/README.md) for configuring your Raspberry Pi for headless mode and connecting via SSH.
___
## Initialize project code
Once connected via SSH, setup the project with the following command:
```
$ source <(curl -s https://raw.githubusercontent.com/QnnOkabayashi/scripts/master/PiDiffuserCam/setup.sh)
```
> Warning: You should always verify that scripts from URLs are safe before running! Check out the source code below yourself.

[Source code](https://github.com/QnnOkabayashi/scripts/blob/master/PiDiffuserCam/setup.sh)

This will:
1. Update the package manager
2. Install Git and PiCamera, required dependencies
3. Clone the project repo code to the home directory
4. Enable the camera module
5. Reboot
> Note: Sometimes this code doesn't do anything for reasons beyond me. If it doesn't work at first, wait a minute and try again.