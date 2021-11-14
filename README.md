# weather-pi
A project to create a weather station that streams data when has connection and pushes it to GoogleCloud

# What to do in Raspberry Pi

## Edit cron and add the start command

$ `sudo crontab -e`

`@reboot python path/to/weather-pi/rasp/weather-station.py >> /var/log/daily-backup.log 2>&1`

`sudo reboot`

 * 
* Install git
    + `sudo apt install git-all`
* Edit token config
