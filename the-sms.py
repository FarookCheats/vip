import requests,json,time,threading,os,sys
import urllib.request, os, threading, time, random, sys
import colorama
from colorama import Fore, Style, init
#from requests_futures.sessions import FuturesSession
#from requests_futures import sessions
os.system("clear")
print(Fore.RED + "[+]" + Fore.YELLOW + " Number in Memu Termux")
print("")
print(Fore.YELLOW + "[:::::::::::::::::::::::::::::::::::::::::::]")
print("")
print(Fore.GREEN + "[1]" + Fore.BLUE + " Spam SMS")
print("")
print(Fore.GREEN + "[2]" + Fore.BLUE + " zphisher")
print("")
print(Fore.GREEN + "[3]" + Fore.BLUE + " Spam Gmail")
print("")
print(Fore.GREEN + "[::::::::::::::::::::::::::::::::::::::::::::]")
print("")
verfly = input(Fore.YELLOW + "[+] Numbers : ")
if verfly == '1':
	os.system("python way.py")
	
if verfly == '2':
	os.system("pkg update")
	
if verfly == '3':
	os.system("python g.py")