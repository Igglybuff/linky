# linky

`linky` is a work-in-progress command-line tool which can search the internet for movies and TV shows hosted on 1-click hosting websites like OpenLoad, Streamango, RapidVideo, and more (full list of supported hosters coming soon).

`linky` integrates tightly with [JDownloader](http://jdownloader.org/) and can send any URL to a JDownloader "device" via the [my.jdownloader.org](https://my.jdownloader.org/) API. There are plans to also integrate with [pyLoad](https://pyload.net/) soon.

At the moment, `linky` uses the [Orion API](https://orionoid.com/) to find links which requires an app key. To acquire an app key, you must sign up for an Orion account and register for an app key via their registration form.

## Installation
To install `linky`:

```
# clone this repository
git clone https://github.com/Igglybuff/linky.git && cd linky

# install it with pip
pip3 install .

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

#### MyJDownloader
Sign up for an account and sign in to it on your JDownloader client(s). You can find your client's device ID by clicking on it on the MyJDownloader website and reading the `deviceId=` URL parameter in your address bar.

### Searching for links
Only OpenLoad links are returned at the moment, but there are plans to enable setting different sources in the future.

`linky search --indexer orion --query "4537896"`

NB: `4537896` is the IMDB ID for [White Boy Rick (2018)](https://www.imdb.com/title/tt4537896/?ref_=fn_al_tt_1).

### Sending links to JDownloader

`linky push --link "<url>" --downloader jdownloader`

### Searching and sending a link to JDownloader

`linky push --link $(linky search --indexer orion --query "White Boy Rick") --downloader jdownloader`

### Checking the status of your downloads

`linky status`

### Planned features
All subcommands:
- [ ] Implement a more convenient way of searching and pushing in the same command
- [x] Implement taking a comma-separated list of URLs as input
- [x] Implement the `--silence` feature to suppress informational log output
- [x] Implement pyLoad integration
- [ ] Implement human-readable output as a default with `--json` as an optional alternative (and maybe `--pretty-print` too)

`linky search`:
- [ ] Implement a `--results` option to print the first n URLs returned from Orion API as a comma-separated list
- [ ] Implement a `--hosters` option to set the 1-click-host source
- [ ] Implement keyword search by default, with ability to override with `--imdb`, `--tvdb`, or `--tmdb` instead
- [ ] Implement a `--quality` option to set the preferred video quality to return

`linky status`:
- [ ] Implement `--all` option to output a report for everything in your download manager (this is the default now)
- [ ] Implement a `--name` option to get the status of a specific package/download