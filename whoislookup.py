import whois
import pyfiglet
print(pyfiglet.figlet_format("W h o i s" , font="banner3"))
print("I will gather WHOIS data of given url \nPlease make sure you are connected to internet")
print(" \n \n enter the url")
a = input("> ")
w = whois.whois(a)
print(w)