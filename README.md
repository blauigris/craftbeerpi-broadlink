# craftbeerpi-broadlink

Simple Craftbeerpi 3.x plugin for broadlink actors. Supports all the 
smart plugs supported by python-broadlink.


Quickstart
----------

Install requirements

    pip install broadlink
   
Download or clone the repo, then move the broadlink_actor directory
to the plugin path of crafbeerpi.

    git clone https://github.com/blauigris/craftbeerpi-broadlink.git
    cd craftbeerpi-broadlink
    cp -r broadlink_actor <PATH TO CRAFTBEERPI ROOT>/modules/plugins
    cd ..
    rm -rf craftbeerpi-broadlink
    

Configuration
-------------

The only property available for this plugin is the IP of the device. If
unset it will pick the first it finds.

