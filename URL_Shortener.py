#pip install pyshorteners

import pyshorteners as sh

data = input("Enter the URL you want to shorten: ")

link = data

s = sh.Shortener()

print(s.tinyurl.short(link))
