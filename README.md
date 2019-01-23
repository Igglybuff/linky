# linky

`linky` is a work-in-progress command-line tool which can search the internet for movies and TV shows hosted on 1-click hosting websites like OpenLoad (full list of supported hosters coming soon).

`linky` integrates tightly with [JDownloader](http://jdownloader.org/) and can send any URL (or multiple URLs as a comma-separated list) to a JDownloader "device" via the [my.jdownloader.org](https://my.jdownloader.org/) API or to a [pyLoad](https://pyload.net/) instance.

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
By default, `linky` looks for `~/.config/linky/linky.conf` for configuration. For example, to configure JDownloader, pyLoad, and Orion:

```
[client jdownloader]
default = true
email = foo@bar.com
password = foobar123
device_id = 12345678

[client pyload]
hostname = localhost
port = 8000
username = pyload
password = pyload
ssl = false

[indexer orion]
user_key = ABCDEFGHIJ123456
app_key = KLMNOPQRS789012
```

#### MyJDownloader
Sign up for an account and sign in to it on your JDownloader client(s). You can find your client's device ID by clicking on it on the MyJDownloader website and reading the `deviceId=` URL parameter in your address bar.

### Searching for links
Only OpenLoad links are returned at the moment, but there are plans to enable setting different sources in the future.

#### Basic keyword search

`linky search --hosters openload --indexer orion --media-type movie "White Boy Rick"`

#### IMDB ID search with 10 results

`linky search --hosters openload --indexer orion --query-type imdb --media-type movie --results 10 "5519340"`

#### TMDB ID search for 720p only

`linky search -w openload -i orion -t tmdb -m movie -q hd1080 -r 6 "424694"`

### Sending links to JDownloader

`linky push --link "<url>" --downloader jdownloader`

### Searching and sending a link to JDownloader

`linky push --link $(linky search --indexer orion "White Boy Rick") --downloader jdownloader`

### Checking the status of your downloads

`linky status --downloader jdownloader`

### Planned features
All subcommands:
- [ ] Implement a more convenient way of searching and pushing in the same command
- [x] Implement taking a comma-separated list of URLs as input
- [x] Implement the `--silence` feature to suppress informational log output
- [x] Implement pyLoad integration
- [ ] Implement human-readable output as a default with `--json` as an optional alternative (and maybe `--pretty-print` too)

`linky search`:
- [x] Implement a `--results` option to print the first n URLs returned from Orion API as a comma-separated list
- [x] Implement a `--hosters` option to set the 1-click-host source
- [x] Implement a `--query-type` option to override the default keyword search, e.g. to search by IMDB/TVDB/TMDB ID.
- [x] Implement a `--quality` option to set the preferred video quality to return

`linky push`:
- [ ] Implement a way to print info about pushed links including package ID and file name

`linky status`:
- [ ] Implement `--all` option to output a report for everything in your download manager (this is the default now)
- [ ] Implement a main argument to get the status of a specific package/download by file name
- [ ] Implement an `--id` option to get the status of a package by ID
- [ ] Implement human-readable output to print % completed, total size, download speed, and name