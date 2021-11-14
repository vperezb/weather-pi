# weather-pi
A project to create a weather station that streams data when has connection and pushes it to GoogleCloud

# Docs stuff I write to be more efficient

https://docs.google.com/document/d/e/2PACX-1vSwtt75HAaLf8mak6CjRxxAyzRvRG9KmS2q-SgFhdzwDsXh1IkIIJi-068JX5pkKKqJHJzL9lwzYafa/pub

# What to do in Raspberry Pi

## Edit cron and add the start command

$ `sudo crontab -e`

`@reboot python path/to/weather-pi/rasp/weather-station.py >> /var/log/daily-backup.log 2>&1`

`sudo reboot`

 * 
* Install git
    + `sudo apt install git-all`
* Edit token config
