#! /usr/bin/env python3
# # coding=utf-8
'''
This program will request the html of a given link. It will then
scrape the html for tags to gather data and return each row of data.
It will then create a data frame using pandas.

Charlie Say
CS 161 10:00AM

___PSEUDO__

request for downloaded html with provided link
scrape the site and parse it into a readable format
search for tags to gather data

data frame:
    input each row from beautifulsoup
    create a list of lists
    create each row in data frame
    parse data
    creata data frame
    return data frame to graph

'''

from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime as dt


# litecoin_link = 'https://coinmarketcap.com/currencies/litecoin/historical-data/?start=20190101&end=20190305'
# ethereum_link = 'https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20190101&end=20190305'
# bitcoin_link = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20190101&end=20190305'


def bitcoin(link):
    '''
    Request the site with a link and scrape it with beautifulsoup.
    Find all tags with 'tr' which will give us the data we need from the site.
    Return all the rows we find with the tag 'tr' in the html of the site.
    '''
    bitcoin_r = requests.get(link)
    bitcoin_soup = BeautifulSoup(bitcoin_r.text, 'html.parser')
    bitcoin_table = bitcoin_soup.find('div', attrs={'class':'table-responsive'})
    rows = bitcoin_table.find_all('tr')
    return(rows)

def ethereum(link):
    '''
    Request the site with a link and scrape it with beautifulsoup.
    Find all tags with 'tr' which will give us the data we need from the site.
    Return all the rows we find with the tag 'tr' in the html of the site.
    '''
    ethereum_r = requests.get(link)
    ethereum_soup = BeautifulSoup(ethereum_r.text, 'html.parser')
    ethereum_table = ethereum_soup.find('div', attrs={'class':'table-responsive'})
    rows = ethereum_table.find_all('tr')
    return(rows)

def litecoin(link):
    '''
    Request the site with a link and scrape it with beautifulsoup.
    Find all tags with 'tr' which will give us the data we need from the site.
    Return all the rows we find with the tag 'tr' in the html of the site.
    '''
    litecoin_r = requests.get(link)
    litecoin_soup = BeautifulSoup(litecoin_r.text, 'html.parser')
    litecoin_table = litecoin_soup.find('div', attrs={'class':'table-responsive'})
    rows = litecoin_table.find_all('tr')
    return(rows)
    

def data(input_rows):
    '''
    Create a list from the rows of data we gather using the parent node 'div' which
    is the tag 'tr'. This is the data we want. Append the data onto another list to
    export as a pandas data frame.
    '''

    data = []
    
    i = 0 # begin count
    for row in input_rows: # iterate through each row with tag 'tr' (table read)
        data_org = [] # make a list of lists
        find_children = row.findChildren() # find child nodes of parent node 'div' class='table'

        for children in find_children:
            data_org.append(children.text) # append all the 'child nodes'. data for each day.

        if(i > 0):
            data_org[0] = data_org[0].replace(',','') # remove comma in date string
            data_org[5] = data_org[5].replace(',','') # remove comma in total volume
            data_org[6] = data_org[6].replace(',','') # remove comma in market cap
            data.append({'date':dt.strptime(data_org[0], '%b %d %Y'), # format the date
                        'open':float(data_org[1]), # turn string in list into floats, append to main list
                        'high':float(data_org[2]), # make data into a dictionary
                        'low':float(data_org[3]),
                        'close':float(data_org[4]),
                        'volume':float(data_org[5]),
                        'marketcap':float(data_org[6])})

        i = i + 1 # counter
    
    data_frame = pd.DataFrame(data)
    return(data_frame)
    # data_frame.to_csv('somefile.csv', sep='\t', index=False)
    






    