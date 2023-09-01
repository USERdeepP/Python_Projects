import wget
import pyfiglet
a = pyfiglet.figlet_format("Downloader" , font="big")
print(a)
print("\n This tool is designed to download only single file \n it can not download a folder \n")
URL = input("Enter the url > ")
wget.download(URL)