import pandas as pd
#import pytube
#from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import xlsxwriter
from urllib import parse

workbook = xlsxwriter.Workbook('output_excel.xlsx')
worksheet = workbook.add_worksheet()

df = pd.read_excel('Untitled spreadsheet.xlsx', sheet_name='Sheet1', usecols=['url'])

row = 0
#column = 0
i = 0

nan = False

print(len(df.index))
id_value = 0
title = ""
channel_id = 0

for index in range(len(df.index) + 1):

    nan = False

    if (i == 0):
        worksheet.write(row, 0, "URL")
        worksheet.write(row, 1, "ID")
        worksheet.write(row, 2, "TITLE")
    else:
        try:
            worksheet.write(row, 0, df.at[i, "url"])
            r = requests.get(df.at[i, "url"])
            soup = BeautifulSoup(r.text)
            link = soup.find_all(name="title")[0]
            title = link.text
            print(title)

            soup2 = BeautifulSoup(r.text, 'html.parser')
            channel_id = soup2.select_one('meta[property="og:url"]')['content'].strip('/').split('/')[-1]

            #id_value = video_id(df.at[i, "url"])
            print(channel_id)



        except:
            nan = True
            pass

        if (nan == False):
            #do nothing
            worksheet.write(row, 1, channel_id)
            worksheet.write(row, 2, title)

    i += 1
    row += 1

workbook.close()
                                                    
                                                                                                                    
                                                                                                                    
                                                                                                                    
                                                                                                                    
