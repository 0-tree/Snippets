#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 31 12:22:22 2018

@author: arthur

"""

import pandas as pd


#%%

def openpyxl_write_df(sheet,r,c,df,styleIndex=None,styleColumn=None,styleValue=None,dropIndex=False,dropColumn=False):
    '''
    wrapper to print a whole pandas dataframe to an openpyxl worksheet,
    because the only available functions are either a mono-cell printer [cell()],
    or a shitty unplayablewith row appender [append()] :)

    Parameters
    ----------
    sheet: openpyxl.worksheet.Worksheet
        instance of sheet to print in
    r,c: int
        0-based position where to print the df
    df: pd.DataFrame
        DataFrame to print
    styleX: TBW, None, default None
        will be applied to all values in X. If None, use default
    dropX: bool, default False
        whether not to print X
    '''
    
    if not isinstance(df,pd.DataFrame):
        raise TypeError('df not of type pd.DataFrame: {}'.format(type(df)))
    
    for x in (styleIndex,styleColumn,styleValue):
        if x is None: x = None # IAH: manage this
          
    n,m = df.shape
    if dropIndex:
        _c = c-1
    else:
        _c = c
    if dropColumn:
        _r = r-1
    else:
        _r = r
       
    # write index
    if not dropIndex:
        if not dropColumn:
            sheet.cell(_r,_c,df.index.name)
            # handle style
        for i in range(n):
            sheet.cell(_r+1+i,_c,df.index[i])
            # handle style
            
    # write columns
    if not dropColumn:
        for j in range(m):
            sheet.cell(_r,_c+1+j,df.columns[j])
            # handle style
            
    # write values
    for i in range(n):
        for j in range(m):
            sheet.cell(_r+1+i,_c+1+j,df.values[i,j])
            # handle style

      