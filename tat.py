""" Tweet Annotation Tool 
	Version: 0.1a
    Author: Kris Bolton
	GitHub: github.com/krisbolton
	Description: CLI tool to annotate tweets with sentiment to create sentiment analysis datasets.

	License: 

"""

import sys
import os.path
import click

@click.command()
@click.option('--file', prompt='Enter file name', help='Then name of the CSV file to read.')
def get_file_name(file):
    try:
        assert file.endswith('.csv')
    except AssertionError:
        print('Error: file suffix not .csv. Please provide the correct file type.')
        sys.exit()
    try:
        assert os.path.isfile(file)
    except AssertionError:    
        print ('Error: %s file does not exist.' % file)
        sys.exit()
    else:
        print('File %s selected.' % file)
    file_name = file
    return file_name


# TODO

#def make_CSV_copy():
	# chekc if a copy exists. make a copy of the CSV file?

# Mesages (printed to the screen)

#def banner_message():

#def instructions_message():


def main():
    get_file_name()

if __name__ == '__main__':
    main()
