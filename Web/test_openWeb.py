#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 10:19:08 2018

@author: arthur
"""

#%%

import webbrowser

#%%

urlBank = {
        'persoAdmin': ('https://lastpass.com/',
                       'https://todoist.com/',
                       'https://mail.yahoo.com/',
                       'http://lespoches.noomad.org:8065/login/?id=js7ezjm8nfru3y3yeqtdisbwqy',
                       ),
                        
        'news': ('https://openmined.slack.com/',
                 'https://octeam.slack.com/',
                 'https://byteball.slack.com',
                 'https://discordapp.com/channels/378030344374583298/378030537916547072') # Augur
}


#%%

if __name__ == '__main__':
    
    new = 2

    for k in urlBank.keys():

        # ideally each key in different pages...
        for url in urlBank[k]:
            webbrowser.open(url,new)
    
        
        
        

