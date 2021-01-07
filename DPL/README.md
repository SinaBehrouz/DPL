# DPL

## Note
This is a source code for the Alpha version and is lacking many of the essential and improved features.
The final product source code is proprietary.

## Instructions
Assuming user already has python3 and python3-pip installed.

To run the package you should:

Modify files on micro-controller:

    $ sudo vim /boot/cmdline.txt

    delete: console = serial1, 115200 and kgdboc = serial1, 115200

    After modification:

    dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2  rootfstype=ext4 elevator=deadline fsck.repair=yes  rootwait

    $ sudo nano /boot/config.txt

    add: dtoverlay=sc16is752-spil, int_pin=24

    $ sudo reboot

After modifying above files:

  1. Setting up a virtual environment:
    - sudo pip3 install virtualenv
    - python3 -m venv env
    - source env/bin/activate
    After you're finished with the package - deactivate your environment
      - deactivate

  2. install the dependancies
    - sudo pip3 install -r requirements.txt

  3. To run the file run the following command:
    - python3 main.py
