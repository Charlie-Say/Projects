#! /usr/bin/env python3
# # coding=utf-8
'''
This program will make the rows from cryptofuncs.py and turn it into a data frame
using the data function from cryptofuncs.py. It will convert the rows of data
into a data frame onto an offline graph on the web browser using a candlestick
chart provided by plotly graph module.

Charlie Say
CS 161 10:00AM

___PSEUDO__

create a class with buttons
make buttons graph charts in html
'''

import cryptofuncs as cf
import pandas as pd
import plotly.offline as pyo
from plotly.tools import FigureFactory as FF

def bitcoinchart():
    '''
    Use function from cryptofuncs.py to get rows and data frame to create
    a candlestick chart using plotly module.
    Creating the layout for the graph.
    '''

    rows = cf.bitcoin('https://coinmarketcap.com/currencies/bitcoin/historical-data/'
                        '?start=20180321&end=20190321')
    data_frame = cf.data(rows)

    fig = FF.create_candlestick(data_frame['open'],
                                data_frame['high'],
                                data_frame['low'],
                                data_frame['close'],
                                dates=data_frame['date'])

    fig['layout'].update({
        'title': 'Bitcoin Annual Price Development',
        'yaxis': {'title': 'Bitcoin in USD'}
    })

    pyo.offline.plot(fig)
    # pyo.offline.plot(fig, filename='graph', image='png')



def ethereumchart():
    '''
    Use function from cryptofuncs.py to get rows and data frame to create
    a candlestick chart using plotly module.
    Creating the layout for the graph.
    '''

    rows = cf.ethereum('https://coinmarketcap.com/currencies/ethereum/'
                    'historical-data/?start=20180306&end=20190306')
    data_frame = cf.data(rows)

    fig = FF.create_candlestick(data_frame['open'],
                                data_frame['high'],
                                data_frame['low'],
                                data_frame['close'],
                                dates=data_frame['date'])
    fig['layout'].update({
        'title': 'Ethereum price development',
        'yaxis': {'title': 'Ethereum in USD'}
    })

    pyo.offline.plot(fig)


def litecoin():
    '''
    Use function from cryptofuncs.py to get rows and data frame to create
    a candlestick chart using plotly module.
    Creating the layout for the graph.
    '''
    rows = cf.litecoin('https://coinmarketcap.com/currencies/litecoin/'
                   'historical-data/?start=20180306&end=20190306')
    data_frame = cf.data(rows)

    fig = FF.create_candlestick(data_frame['open'],
                                data_frame['high'],
                                data_frame['low'],
                                data_frame['close'],
                                dates=data_frame['date'])
    fig['layout'].update({
        'title': 'Litecoin price development',
        'yaxis': {'title': 'Litecoin in USD'}
    })

    pyo.offline.plot(fig)