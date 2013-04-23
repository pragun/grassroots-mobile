#!/bin/bash
while [ ! -c /dev/ttyUSB0 ]
do
	echo 'waiting for spidev...'
	sleep 1s
done
python pwsw-daemon.py


