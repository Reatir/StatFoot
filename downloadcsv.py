import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="chromedriver")
browser.get('https://www.football-data.co.uk/francem.php')
