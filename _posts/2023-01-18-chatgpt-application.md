---
layout: page
title: "ChatGPT and its application for me in writing post"
subtitle: "you.com"
date: 2023-01-18 11:55:10 
categories: ["tips"]
---

This is a sample of how I using chatGPT AI for creating a markdown file. This process gonna shortern a lot of time for me. 

Here is what I put in you.com AI:

write a python script that create a .md file and name it follow format: year-month-day-hello. In the file include these lines: --- layout: page title: "Name of the post" subtitle: "Subtitle of the post." date: 2020-01-10 21:21:21 +0530 categories: ["general"] --- The file created would be putted into a previous folder.


Here is the code: 

import os
import datetime

# Get the current date
now = datetime.datetime.now()

# Generate the file name
filename = '{:%Y-%m-%d}-hello.md'.format(now)

# Create the file in the current directory
with open(filename, 'w') as f:
    # Write the lines to the file
    f.write('---\n')
    f.write('layout: page\n')
    f.write('title: "Name of the post"\n')
    f.write('subtitle: "Subtitle of the post."\n')
    f.write('date: {:%Y-%m-%d %H:%M:%S %z}\n'.format(now))
    f.write('categories: ["general"]\n')
    f.write('---\n')