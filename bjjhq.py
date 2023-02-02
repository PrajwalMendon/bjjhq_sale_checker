from bs4 import BeautifulSoup
import requests
from win32com.client import Dispatch

text = "boxing glove"  # Modify this var to search for a specific product

url = "https://www.bjjhq.com"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

product = doc.find_all({'h1': {'class': 'right'}})
sale = [elm.text for elm in product]

path = r'C:\users\prajwal\desktop\bjjsale.lnk'

if text in sale[1].lower():
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = url
    shortcut.save()
