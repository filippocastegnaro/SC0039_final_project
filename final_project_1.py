#import os, re and argparse modules
import os
import re
import argparse

#here you can change the name of the CARA file you want to modify
filename = 'test.cara' #old CARA file name
new_filename = 'proc_test.cara' #new CARA file name

old_list = []

#module to change path from command line
parser = argparse.ArgumentParser(
                    prog='CARA_conv',
                    description='convert path in cara file')

parser.add_argument("-p",'--new_path')
parser.add_argument("-in",'--input')
parser.add_argument("-out",'--output')

args = parser.parse_args()
filename = args.input
new_filename = args.output

with open (new_filename, 'w') as new_file: #open the CARA file for writing

    with open(filename, 'r') as file: #open the same CARA file for reading the path you wnat to change
    
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
                    new_line = line.replace(path, args.new_path + spectrum_name) #replace all the directories with the new path and add the filenames
                    new_file.write(new_line) #write the new file names

                    
            else:
                new_file.write(line) #write every other line in the CARA file that's now a path
                  
