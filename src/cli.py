#! /usr/bin/env python3
import click
import urllib.request
import re
import os

def remove_dupl(arr):
    return list(dict.fromkeys(arr))

def cap(x, upper_bound):
    if x > upper_bound:
        print(f"Found only {upper_bound} videos (not {x} or more as expected).")
        x = upper_bound

    return x

def play_video(optionslist, query, load_video):
    if query == 0:
        search()
    else:
        os.system(f"mpv {load_video} https://www.youtube.com/watch?v={optionslist[query - 1]}")

@click.command()
@click.option('--query', '-q', help='Search query', prompt="Search")
@click.option('--load-video', '-lv', help='Load video (1) or not (0), by default 1')
@click.option('--num-videos', '-nv', help='Number of results to print, by default 5')
def search(query, load_video, num_videos):
   
    click.echo("Searching...")
    ret = []
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + '+'.join(query.split()))
    video_ids = remove_dupl(re.findall(r"watch\?v=(\S{11})", html.read().decode()))  # remove duplicates 
    
    if num_videos is None:
        num_videos = 5
    else:
        num_videos = int(num_videos)
    num_videos = cap(num_videos, len(video_ids))

    video_ids = video_ids[:num_videos]  # keep first num_videos elements

    for video_id in video_ids:
        vidurl = f"https://www.youtube.com/watch?v={video_id}"
        video = urllib.request.urlopen(vidurl)
        results = re.findall(r"<\/title><meta name=\"title\" content=\"(.+?(?=\"))|<link itemprop=\"name\" content=\"(.+?(?=\"))", video.read().decode())
        title, author = results[0][0].replace('&#39;', '').replace("amp;", ""), results[1][1].replace('&#39;', '').replace("amp;", "")
        ret.append([title, author, vidurl])

    click.echo("")
    click.echo("#). Title-------------------------------------Creator-----------------------")
    for y in range(len(ret)):
        t, a = ret[y][0], ret[y][1]
        tlen, alen = len(t), len(a)

        if tlen > 40:
            t = t[:39] + '  '
        else:
            t = t + (' ' * (41 - tlen))
        if alen > 30:
            a = a[:29]
        outpstr = f"{y+1}). {t} {a}"
        click.echo(outpstr)
    click.echo("")
    click.echo("Enter the number of the video you would like to select, or 0 to search again")
    click.echo("")

    query = int(click.prompt('Option')), len(video_ids)
    load_video = "--no-video" if load_video == "0" else ""
    play_video(video_ids, query, load_video)

if __name__ == '__main__':
    search()
