#!/usr/bin/env python3
#AuthorID  = lakshay2@myseneca.ca
#Author = lakshay2

import os
import subprocess

def free_space():
    # Corrected the command string
    p = subprocess.Popen("df -h / | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = p.communicate() #.communicate is used to read the stdout and stderror
    final = stdout.decode('utf-8').strip() # Decode the output and strip any extra whitespace
    
    return  final 

if __name__ == "__main__":
    print(free_space()) # this prints the final result