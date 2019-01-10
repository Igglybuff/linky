# linky

`linky` is a work-in-progress command-line tool which can search the internet for movies and TV shows hosted on 1-click hosting websites like OpenLoad, Streamango, RapidVideo, and more (full list of supported hosters coming soon).

Optionally, you can also tell `linky` to automatically send any links it finds to JDownloader.

## Installation
To install `linky`:

```
# clone this repository
git clone https://github.com/Igglybuff/linky.git && cd linky

# install it with pip
pip install .

# test that it installed correctly
linky --help
``` 

## Usage
### Configuration
By default, `linky` looks for `~/.config/linky/linky.conf` for configuration. For example, to configure JDownloader and Orion:

```
[client jdownloader]
email = foo@bar.com
password = foobar123
device_id = 12345678

[indexer orion]
user_key = ABCDEFGHIJ123456
app_key = KLMNOPQRS789012
```

### Searching for links

`linky search --indexer orion --query "4537896"`

NB: `4537896` is the IMDB ID for [White Boy Rick (2018)](https://www.imdb.com/title/tt4537896/?ref_=fn_al_tt_1).

### Sending links to JDownloader

`linky push --link "<url>" --downloader jdownloader`

### Searching and sending a link to JDownloader

`linky push --link $(linky search --indexer orion --query "White Boy Rick") --downloader jdownloader`