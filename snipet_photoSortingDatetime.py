'''

rename photos in a folder according
to the time they were shot

inspired from
https://paulbreslin.blogspot.fr/2008/07/python-script-to-rename-and-sort.html

'''


#%% imports

import exifread # install with pip
import os

#%% target folder
# must contain all and only photos to be renamed

ARG_pathMixDir = '/Users/arthur/Documents/Time/Moi/B/Reportage/PhotoAClasser/2018/20180503_AndalousieMimi/PhotoMix'


#%% list all {datetime:filename}

dateDict = {}

for filename in os.listdir(ARG_pathMixDir):
   try:
       file = open(os.path.join(ARG_pathMixDir,filename), 'rb')
   except:
       print('{}: Cannot open for reading.\n'.format(filename))
       continue

   # get the tags
   data = exifread.process_file(file, details=False, debug=False)
   if not data:
       print('{}: No EXIF data found'.format(filename))
       continue

   date = data['Image DateTime']
#   date = data['EXIF DateTimeOriginal']

   key = str(date)
   if key in dateDict.keys():
       print('{}: Duplicate datestamp with {}'.format(filename, dateDict[key]))
       key += '_dupl'
   dateDict[key] = filename

   file.close()


#%% rename after sorting by datetime
   
datestamps = list(dateDict.keys())
datestamps.sort()
for datestamp in datestamps:
   suffix = os.path.splitext(dateDict[datestamp])[1]
   newName = datestamp.replace(':', '_')
   newName = newName.replace(' ', '_')
   newName = "pic_" + newName + suffix
   try:
       os.rename(os.path.join(ARG_pathMixDir,dateDict[datestamp]), os.path.join(ARG_pathMixDir,newName))
       print(dateDict[datestamp] + ' -> ' + newName)
   except:
       print('{}: Could not rename'.format(dateDict[datestamp]))
    
