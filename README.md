# CLI Youtube Client

## Intro

This is a program to search and watch youtube from the command line. While this works as described, I made this mostly to learn about CLIs with python and regex.

Uses-

- Click
- PyInstaller
- MPV

## Idea

I originally intended to use the Youtube Data API, but considering that I required [than the api provided], I considered other options. I soon found this [article](https://codefather.tech/blog/youtube-search-python/) and adapted the code to allow for multiple search terms and return multiple video links and expanded the results for more functionality. Because I wanted to provide functionality for search within the command line, I searched the html code for returned videos and wrote regex to find the title and creator of the video (yes this is inefficient, but requires no api key).

## Code

The code itself is relatively simple, and is built from one python file. As described above, the program takes in a search query and returns search results using regex on decoded source html from the videos. If the user chooses to select one, the selected video should open in a new window with [mpv](https://github.com/mpv-player/mpv).

## Usage

I have included an executable and .exe in /dist, which can be run with `cmdytc/cli.exe [ARGUMENTS]`

Using --help, usage is described below:

```
Usage: cli.exe [OPTIONS]

Options:
  -q, --query TEXT  Search query
  --help            Show this message and exit.
```

To build it yourself- run the following:

```
pip install --editable .
pyinstaller src/main/cli.py -F -n cmdytc
```

The executable should then be in /dist.
