#!/bin/python

#########################
#Python Script to create
#Executable file
########################

print ("This is a python script to create an executable file with permissions")

name_of_file = input ("Give your file a name\n")

match file_type:
    case "python":
        compiler = str ("#!/bin/python")
        file_ext = str (".py")
    case "bash":
        compiler = str ("#!/bin/bash")
        file_ext = str (".sh")
    case "perl":
        compiler = str ("#!/bin/perl")
        file_ext = str ("#!/bin/perl")
    case _:
        print ("File type not recognized")
        
file = name_of_file +file_ext
if file_type == "python":
    print (name_of_file + file_ext)
    print (compiler > name_of_file)
elif file_type == "bash":
    print (name_of_file + file_ext)
    print (compiler > n
