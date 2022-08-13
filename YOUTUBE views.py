#driver = webdriver.Chrome(r"C:\Python codes\VET Volume\venv\Lib\site-packages\webdriver_manager\chromedriver.exe")
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
#import schedule
#import itertools
#import undetected_chromedriver as webdrivers
import time
import os
import threading
import webbrowser


def printit():

  os.startfile(r"C:\Users\Administrator\Desktop\\NL chrome\Chrome-001")
  threading.Timer(20.0, printit).start()
  time.sleep(15)
  os.system("taskkill /im chrome.exe /f")

printit()





