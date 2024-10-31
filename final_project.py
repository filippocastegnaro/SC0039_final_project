#!/usr/bin/env python
# coding: utf-8

# In[6]:


#import os and re modules
import os
import re

#here you can change the name of the CARA file you want to modify
filename = 'test.cara' #old CARA file name
new_filename = 'proc_test.cara' #new CARA file name

#here you insert the path where your .ft3 files are located 
new_path = '/Users/xcasfi/DATA/Proc_spectra/3Ds/' #your new path
old_list = []


with open (new_filename, 'w') as new_file: #open the CARA file for writing

    with open(filename, 'r') as file:#open the same CARA file for reading the path you wnat to change
    
        for line in file:
        
            path_match = re.search(r"path='([^']+)'", line) #research all the paths in the CARA file and save them as paths
            if path_match:
                path = path_match.group(1)
                
    
                if os.path.exists(path): #write every path that already exist
                    new_file.write(line)
                    
    
                else:
                    
                    spectrum_name = os.path.basename(path) #extract the filename from the existing path
                   
                    if  spectrum_name == '2rr': #exclude the filenames called 2rr
                        new_file.write(line)
                        continue
                    new_line = line.replace(path, new_path + spectrum_name) #replace all the directories with the new path and add the filenames
                    new_file.write(new_line) #write the new file names

                    
            else:
                new_file.write(line) #write every other line in the CARA file that's now a path
                    



