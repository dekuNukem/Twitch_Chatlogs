Chat logs of a number of past Twitch events, as well as the chat logger itself. I run it in a headless Raspberry Pi.

## Included chat logs

* AGDQ2015
* SGDQ2015
* AGDQ2016
* SGDQ2016
* AGDQ2017
* Bob Ross marathon
* Nintendo Switch introduction
* [Mister Rogers' Neighborhood](https://drive.google.com/file/d/0ByqN9QHBVEsvbUpoVjd5VXBUX0U/view?usp=sharing)

## Usage

* go to [https://twitchapps.com/tmi/](https://twitchapps.com/tmi/) and get your oauth
* put your username and oauth into the beginning of `comment_logger.py`
* `python3 comment_logger.py channel`