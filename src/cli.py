#! /usr/bin/env python3
import click
import urllib.request
import re
import os
import sys
from tabulate import tabulate

def remove_dupl(arr):
    return list(dict.fromkeys(arr))

def parse_to_int(x, lower_bound=1, upper_bound=sys.maxsize):  
    err_msg = f"Error: Option should be an integer between {lower_bound} and {upper_bound}"

    try:
        x = int(x)
        if x < lower_bound or x > upper_bound:
            click.echo(err_msg)
            sys.exit(1)
    except ValueError:
        click.echo(err_msg)
        sys.exit(1)

    return x

def cap(x, upper_bound):
    if x > upper_bound:
        x = upper_bound

    return x

def print_options(video_ids):
    ret = []
    index = 0
    for video_id in video_ids:
        vid_url = f"https://www.youtube.com/watch?v={video_id}"
        video = urllib.request.urlopen(vid_url)
        results = re.findall(r"<\/title><meta name=\"title\" content=\"(.+?(?=\"))|<link itemprop=\"name\" content=\"(.+?(?=\"))", video.read().decode())
        title, author = results[0][0].replace('&#39;', '').replace("amp;", ""), results[1][1].replace('&#39;', '').replace("amp;", "")
        index += 1
        ret.append([index, title, author])

    head = ["#", "Title", "Creator"]
    click.echo(tabulate(ret, headers=head, tablefmt="grid"))

    click.echo("")
    click.echo("Enter the number of the video you would like to select")
    click.echo("")

def play_video(video_id, load_video):
    url = f"https://www.youtube.com/watch?v={video_id}"
    click.echo(f"Playing {url} ...\n")
    os.system(f"mpv {load_video} {url}")

@click.command()
@click.option('--query', '-q', help='Search query', prompt="Search")
@click.option('--load-video', '-lv', help='Load video (1) or not (0), by default 1')
@click.option('--option', '-o', help='(optional) Number of option to choose')
@click.option('--num-videos', '-nv', help='Number of results to print, by default 5; do not use -o and -nv together!')
def search(query, load_video, option, num_videos):
    click.echo("Searching...")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + '+'.join(query.split()))
    video_ids = remove_dupl(re.findall(r"watch\?v=(\S{11})", html.read().decode()))  # remove duplicates 
    click.echo(f"Found {len(video_ids)} videos.")

    query = 0
    to_play = ""
    if option is None:
        if num_videos is None:
            num_videos = 5    
        else:
            num_videos = parse_to_int(num_videos)
        num_videos = cap(num_videos, len(video_ids))

        video_ids = video_ids[:num_videos]  # keep first num_videos elements
        print_options(video_ids)
        query = parse_to_int(click.prompt('Option'), lower_bound=1, upper_bound=num_videos)

    else:
        if num_videos is not None:
            click.echo("Do not use -o and -nv together!")
            sys.exit(1)
        query = parse_to_int(option, lower_bound=1, upper_bound=len(video_ids))

    click.echo("")

    to_play = video_ids[query - 1] 
    load_video = "--no-video" if load_video == "0" else ""
    play_video(to_play, load_video)

if __name__ == '__main__':
    search()
