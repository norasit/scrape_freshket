import bs4
import pandas as pd
from selenium import webdriver

from freshket_vet import scrape # call method

df = scrape(1,5) # set any numbers of page that need to scraping.
# print(df.head())
# print(df.info())

df.to_csv('freshket.csv') # export pandas dataframe to csv file
df.to_excel('freshket.xlsx') # export pandas dataframe to excel file