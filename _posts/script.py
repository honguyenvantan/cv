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