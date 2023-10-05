# Sports display on older iPad
Display my teams scores
Have an older ipad and wanted to display sports scores on it. Javascript wasn't an option because the device was too old. So, flask it was.  I have this running on a raspberrypi and use crontab to run every min.

AIP data: https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b
uefa_champions = 'https://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/scoreboard'
The last bit beyond the / of 
uefa_champions was taken from the ESPN website.  https://www.espn.com/soccer/schedule/_/league/uefa.champions


This is a work in progress.
