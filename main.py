"""
Name: Jose Duarte (https://github.com/Pursn)
Project Started: 4/7/2026

Description:
    An educational program design to convert YoutTube
    videos & playlists into mp3 and mp4 files.

Basic Function Added: 4/8/2026
    Convert single YT video into MP3 or MP4 (Downloads folder)
    Convert YT playlist into MP3 or MP4
    (Creates new folder with [playlist title] in Downloads folder)
"""
import yt_dlp
import os
from pathlib import Path

#Gets the the current machine's path (Windows, Linux, or MacOs) and finds the Downloads folder
#Converts this path into a string
download_folder = str(Path.home() / "Downloads")

#Boolean that is use when we give the user an option
#if the user gives a valid option, we break the loop 
#by turning "testing" to False.
testing = True

#FUNCTIONS----------------------------------------------------
def videoTpMP3(URL):
    with yt_dlp.YoutubeDL({
        'paths': {'home': download_folder},
        'extract_audio': True,
        'format': 'bestaudio/best',
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'outtmpl': '%(title)s',
    }) as video:
        video.download(URL)

def playlistToMP3(URL):
    new_path = ""

    with yt_dlp.YoutubeDL({
        'paths': {'home': download_folder},
        'extract_audio': True,
        'format': 'bestaudio/best',
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'outtmpl': '%(title)s',
        'yes-playlist': True
    }) as P:
        playlist_info = P.extract_info(URL, download=False)
        playlist_title = playlist_info.get('title')
        
        new_path = download_folder + '/' + playlist_title

    Path(new_path).mkdir(parents=True, exist_ok=True)

    with yt_dlp.YoutubeDL({
        'paths': {'home': new_path},
        'extract_audio': True,
        'format': 'bestaudio/best',
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'outtmpl': '%(title)s',
        'yes-playlist': True
    }) as video:
        video.download(URL)



def videoToMP4(URL):
    with yt_dlp.YoutubeDL({
        'paths': {'home': download_folder},
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        
        'outtmpl': '%(title)s.%(ext)s',
    }) as audio:
        audio.download(URL)

def playlistToMP4(URL):
    new_path = ""

    with yt_dlp.YoutubeDL({
        'paths': {'home': download_folder},
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        
        'outtmpl': '%(title)s.%(ext)s',
        'yes-playlist': True
    }) as P:
        playlist_info = P.extract_info(URL, download=False)
        playlist_title = playlist_info.get('title')
        
        new_path = download_folder + '/' + playlist_title

    
    Path(new_path).mkdir(parents=True, exist_ok=True)

    with yt_dlp.YoutubeDL({
        'paths': {'home': new_path},
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        
        'outtmpl': '%(title)s.%(ext)s',
        'yes-playlist': True
    }) as audio:
        audio.download(URL)


def MP3orMP4():
    testing = True
    print("MP3 (1) or MP4 (0): Enter 1 or 0")
    temp = input()
    while(testing):
        if(temp != "1" and temp != "0"):
            print("ERROR: Invalid Option")
            temp = input()
        else:
            testing = False
    
    if(temp == "1"):
        return "mp3"
    elif(temp == "0"):
        return "mp4"
    else:
        print("ERROR: i don't even know how you got here?")

def intro():
    pass
#END OF FUNCTIONS----------------------------------------------------



#START OF PROGRAM



#Displays options for downloading a single video or a playlist
print("Downloading Single YT Video Or PlayList:")
print("1.Single YT Video")
print("2.YT PlayList")

while(testing):
    option = input()
    if(option != "1" and option != "2"):
        print("ERROR: Invalid Option")
        option = input()
    else:
        testing = False

match option:
    case "1":
        print("Single YT Video")
        print("Provide URL To Video:")

        URL = input()

        format = MP3orMP4()

        if(format == "mp3"):
            videoTpMP3(URL)
        elif(format == "mp4"):
            videoToMP4(URL)

    case "2":
        print("YT Playlist")
        print("Provide URL to !!!PLAYLIST!!!")

        URL = input()

        format = MP3orMP4()

        if(format == "mp3"):
            playlistToMP3(URL)
        elif(format == "mp4"):
            playlistToMP4(URL)
