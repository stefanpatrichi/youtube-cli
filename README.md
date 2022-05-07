# CLI Youtube Client

This is a program to search and watch Youtube videos from the command line. While this works as described, I made this mostly to learn about CLIs with python and regex.

## Installation
Requires [Python](https://www.python.org/downloads/) and [mpv](https://github.com/mpv-player/mpv).

On your local machine, clone into this repository and install with `pip install -r requirement.txt`.
If you have superuser privileges, you can add `src/cli.py` as a bash command:

```console
[foo@bar youtube-cli]$ sudo ln -s src/cli.py /usr/bin/youtube-cli
[sudo] password for foo: 
[foo@bar youtube-cli]$ sudo chmod +x /usr/bin/youtube-cli
```

## Idea
I originally intended to use the Youtube Data API, but considering that the idea required very little data from youtube, I considered other options. I soon found this [article](https://codefather.tech/blog/youtube-search-python/), adapted the code to allow for multiple search terms and video options and then expanded the results for more functionality. Because I wanted to provide functionality for searching within the command line, I searched the HTML code for the returned videos and wrote some RegEx to find the title and uploader of the video (yes, this is inefficient, but it requires no API key).

## Usage

```console
[foo@bar youtube-cli]$ youtube-cli --help    
Usage: youtube-cli [OPTIONS]

Options:
  -q, --query TEXT        Search query
  -lv, --load-video TEXT  Load video (1) or not (0), by default 1
  -o, --option TEXT       (optional) Number of option to choose
  -nv, --num-videos TEXT  Number of results to print, by default 5; do not use
                          -o and -nv together!
  --help                  Show this message and exit.
```
(or `python src/cli.py --help` if you didn't follow the steps in Installation)
