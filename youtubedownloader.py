import pyfiglet
from pytube import YouTube

result = pyfiglet.figlet_format("Youtube downloader" , font="bubble")
print(result)
link = input(" > Enter the YouTube video URL: ")
#path = input("enter the path in which you need to download the file \n leave empty if you want it in current directory")


youtubeObject = YouTube(link)
youtubeObject = youtubeObject.streams.get_highest_resolution()
youtubeObject.download()