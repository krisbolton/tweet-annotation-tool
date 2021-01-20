""" Tweet Annotation Tool 
	Version: 0.1.0-alpha
    Author: Kris Bolton
	GitHub: github.com/krisbolton
	Description: CLI tool to annotate tweets with sentiment to create sentiment analysis datasets.

	License: 

"""

import sys
import os.path
import click
import pyfiglet

@click.command()
@click.option('--file', prompt='Enter the csv file to annotate', help='The name of the CSV file to read.')
def get_file_name(file):
    """ Get file name from flag (--file) or request file name on start """
    try:
        assert file.endswith('.csv')
    except AssertionError:
        print('Error: file suffix not .csv. Please provide the correct file type.')
        sys.exit(1)
    try:
        assert os.path.isfile(file)
    except AssertionError:    
        print ('Error: %s file does not exist.' % file)
        sys.exit(1)
    else:
        print('File %s selected.' % file)
    file_name = file
    return file_name

def welcome_banner():
    """ Prints welcome banner upon program start """
    for x in range(5):
        print('\r\n')
    figlet = pyfiglet.figlet_format('Tweet Annotation Tool', font='slant')
    print(figlet)
    print('by Kris Bolton')
    print('v0.1.0-alpha')
    print('\r\n')

def main():
    welcome_banner()
    get_file_name()

if __name__ == '__main__':
    main()