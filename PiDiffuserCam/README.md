# PiDiffuserCam Setup
Quinn Okabayashi and Josh Vandervelde
___
This page streamlines the process of configuring our [PiDiffuserCam code](https://github.com/QnnOkabayashi/PiDiffuserCam).

Currently only Mac OS is supported.
___
## Hardware Requirements
* Raspberry Pi
* Raspberry Pi Camera module
* Micro SD card [(requirements)](https://www.raspberrypi.org/documentation/installation/sd-cards.md)
___
## Software Configuration
1. Follow the instructions [here](https://github.com/QnnOkabayashi/scripts/blob/master/HeadlessPi/README.md) for configuring your Raspberry Pi for headless mode and connecting via SSH.

2. Once connected via SSH, setup the project with the following command:
    ```
    $ source <(curl -s https://raw.githubusercontent.com/QnnOkabayashi/scripts/master/PiDiffuserCam/setup.sh)
    ```
    > Warning: You should always verify that scripts from URLs are safe before running! Check out the source code below yourself.

    [Source code](https://github.com/QnnOkabayashi/scripts/blob/master/PiDiffuserCam/setup.sh)

    This will:
    * Update the package manager
    * Install Git and PiCamera, required dependencies
    * Clone the project repo code to the home directory
    * Enable the camera module
    * Reboot
    > Note: Sometimes this code doesn't do anything for reasons beyond me. If it doesn't work at first, wait a minute and try again.
