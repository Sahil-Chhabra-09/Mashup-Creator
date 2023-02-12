import os
import sys

from moviepy import editor as mp
from moviepy.editor import AudioFileClip, concatenate_audioclips
from pytube import Search, YouTube
from pydub import AudioSegment


def mashup(singer: str, count: int, duration: int, output_file: str) -> None:
    singer = singer+" songs with lyrics"
    s = Search(singer)
    urls = []
    while len(s.results) < count:
        s.get_next_results()

    for v in s.results[:count]:
        urls.append(v.watch_url)

    path = "."
    for url in urls:
        try:
            yt = YouTube(url)
        except:
            print("Error connecting to url")
        try:
            yt.streams.filter(progressive=True).first().download(output_path=path)
        except:
            print("Error downloading video")

    print("Download completed")

    files = os.listdir(".")
    for f in files:
        if ".3gpp" in f:
            try:
                v = mp.VideoFileClip(f)
                audio_file = os.path.splitext(os.path.basename(f))[0]
                v.audio.write_audiofile(audio_file + ".mp3")
            except:
                print("Error converting video to audio")

    audioClips = []
    try:
        for af in files :
            if '.mp3' in af:
                audioClips.append(AudioFileClip(af).subclip(0,duration))

        finalClip = concatenate_audioclips(audioClips)
        finalClip.write_audiofile(output_file)
    except:
        print('cant merge audio')
        
        
def rerun(duration: int, output_file: str) -> None:
    files = os.listdir(".")
    audioClips = []
    try:
        for af in files :
            if '.mp3' in af:
                audioClips.append(AudioFileClip(af).subclip(0,duration))

        finalClip = concatenate_audioclips(audioClips)
        finalClip.write_audiofile(output_file)
    except:
        print('cant merge audio')


if len(sys.argv) != 5:
    raise ValueError("Expected 4 arguments: singer, count, duration, output_file")
singer = sys.argv[1]
count = int(sys.argv[2])
duration = int(sys.argv[3])
output_file = sys.argv[4]
mashup(singer, count, duration, output_file)
rerun(duration, output_file)