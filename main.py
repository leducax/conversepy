import pytube
from moviepy.editor import *
import os
import sys
import time
from colorama import Fore, Style, init

# Clear function to clear the console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Initialize colorama
init(autoreset=True)

# Print logo
print(Fore.GREEN + """

╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━┳╮╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╰╮╭╯┃
┃┃╱╰╋━━┳━╮╭╮╭┳━━┳━┳━━┳━━╮┃╰━╯┣╮╰╯╭╯
┃┃╱╭┫╭╮┃╭╮┫╰╯┃┃━┫╭┫━━┫┃━┫┃╭━━╯╰╮╭╯
┃╰━╯┃╰╯┃┃┃┣╮╭┫┃━┫┃┣━━┃┃━┫┃┃╱╱╱╱┃┃
╰━━━┻━━┻╯╰╯╰╯╰━━┻╯╰━━┻━━╯╰╯╱╱╱╱╰╯ 
""")

time.sleep(5)
print(Fore.GREEN + "                     𝕄𝕒𝕕𝕖 𝕓𝕪: 𝕃𝕖𝔻𝕦𝕔𝔸𝕏")
time.sleep(3)
clear()

# Check command line arguments
if len(sys.argv) < 2:
    print(Fore.RED + "Please specify the option -m for music conversion or -v for video conversion.")
    sys.exit(1)

# Check the specified option
option = sys.argv[1]

if option == "-m":
    print(Fore.GREEN + """

╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━┳╮╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╰╮╭╯┃
┃┃╱╰╋━━┳━╮╭╮╭┳━━┳━┳━━┳━━╮┃╰━╯┣╮╰╯╭╯╭╮╭┳╮╭┳━━┳┳━━╮
┃┃╱╭┫╭╮┃╭╮┫╰╯┃┃━┫╭┫━━┫┃━┫┃╭━━╯╰╮╭╯╱┃╰╯┃┃┃┃━━╋┫╭━╯
┃╰━╯┃╰╯┃┃┃┣╮╭┫┃━┫┃┣━━┃┃━┫┃┃╱╱╱╱┃┃╱╱┃┃┃┃╰╯┣━━┃┃╰━╮
╰━━━┻━━┻╯╰╯╰╯╰━━┻╯╰━━┻━━╯╰╯╱╱╱╱╰╯╱╱╰┻┻┻━━┻━━┻┻━━╯ 
""")

    time.sleep(5)
    print(Fore.GREEN + "                     𝕄𝕒𝕕𝕖 𝕓𝕪: 𝕃𝕖𝔻𝕦𝕔𝔸𝕏")
    time.sleep(3)

    print(Fore.YELLOW + "The conversion program is starting...")
    time.sleep(2)

    os.makedirs("Downloader/Music", exist_ok=True)

    with open("url_yt-music", "r") as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download("Downloader/Music/")

        video_filename = os.path.join("Downloader/Music", video.default_filename)
        mp3_file = video_filename.replace(".mp4", ".mp3")
        video_clip = VideoFileClip(video_filename)
        video_clip.audio.write_audiofile(mp3_file)

        music_name = os.path.splitext(os.path.basename(mp3_file))[0]

        video_clip.close()
        os.remove(video_filename)

        print(Fore.GREEN + f"The video has been successfully downloaded and converted to MP3 ({music_name}).")

    print(Fore.GREEN + "All videos have been successfully downloaded and converted to MP3.")

elif option == "-v":
    print(Fore.GREEN + """

╭━━━╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━━━┳╮╱╱╭╮╱╱╱╱╱╱╭╮
┃╭━╮┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╰╮╭╯┃╱╱╱╱╱╱┃┃
┃┃╱╰╋━━┳━╮╭╮╭┳━━┳━┳━━┳━━╮┃╰━╯┣╮╰╯╭╯╭╮╭┳┳━╯┣━━┳━━╮
┃┃╱╭┫╭╮┃╭╮┫╰╯┃┃━┫╭┫━━┫┃━┫┃╭━━╯╰╮╭╯╱┃╰╯┣┫╭╮┃┃━┫╭╮┃
┃╰━╯┃╰╯┃┃┃┣╮╭┫┃━┫┃┣━━┃┃━┫┃┃╱╱╱╱┃┃╱╱╰╮╭┫┃╰╯┃┃━┫╰╯┃
╰━━━┻━━┻╯╰╯╰╯╰━━┻╯╰━━┻━━╯╰╯╱╱╱╱╰╯╱╱╱╰╯╰┻━━┻━━┻━━╯ 
""")

    time.sleep(5)
    print(Fore.GREEN + "                     𝕄𝕒𝕕𝕖 𝕓𝕪: 𝕃𝕖𝔻𝕦𝕔𝔸𝕏")
    time.sleep(3)

    print(Fore.YELLOW + "The conversion program is starting...")
    time.sleep(2)

    os.makedirs("Downloader/Video", exist_ok=True)

    with open("url_yt-video", "r") as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        youtube = pytube.YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download("Downloader/Video/")

        video_name = os.path.splitext(os.path.basename(video.default_filename))[0]

        print(Fore.GREEN + f"The video has been successfully downloaded ({video_name}).")

    print(Fore.GREEN + "All videos have been successfully downloaded.")

else:
    print(Fore.RED + "Invalid option. Please specify -m for music conversion or -v for video conversion.")
