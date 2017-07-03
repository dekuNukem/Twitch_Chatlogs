rm -r ~/python_games/
sudo apt-get -y purge scratch
sudo apt-get -y purge wolfram-engine
sudo apt-get -y purge minecraft-pi
sudo apt-get -y purge sonic-pi
sudo apt-get -y purge pistore
sudo apt-get -y purge omxplayer
sudo apt-get -y purge libreoffice*
sudo apt-get -y purge bluej
sudo apt-get -y purge nodered
sudo apt-get -y autoremove
sudo apt-get clean
sudo apt-get -y update
sudo apt-get -y upgrade

# sudo apt-get install tightvncserver