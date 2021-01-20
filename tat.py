""" Tweet Annotation Tool 
	Version: 0.2.0-alpha
    Author: Kris Bolton
	GitHub: github.com/krisbolton
	Description: CLI tool to annotate tweets with sentiment to create sentiment analysis datasets.

	License: 

"""

import sys
import os.path
import click
import pyfiglet
import pandas as pd

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
        print ('Error: %s does not exist.' % file)
        sys.exit(1)
    else:
        print('%s selected.' % file)
        file_name = file
        annotate(file_name)

def annotate(file_name):
    """ Read tweet id and tweet column from csv file """
    col_list = ['id', 'tweet']
    input_csv = pd.read_csv(file_name, usecols=col_list)
    # create pandas dataframe from those two cols
    input_csv['sentiment'] = ""
    # add sentiment col
    for i, row in input_csv.iterrows():
        # iterate over rows, asking for sentiment for each row
        print(row[1])
        sentiment = input('Enter sentiment: ')
        sentiment = int(sentiment)
        input_csv.at[i, 'sentiment'] = sentiment

# TODO add save func

#def save_dataframe(dataframe):
#    """ Save dataframe to CSV """
#    dataframe.to_csv('annotated_dataset', index=False)

def welcome_and_instruct():
    """ Prints welcome and instructions upon program start """
    for x in range(5):
        print('\r\n')
    figlet = pyfiglet.figlet_format('Tweet Annotation Tool', font='slant')
    print(figlet)
    print('by Kris Bolton')
    print('v0.2.0-alpha')
    print('\r\n')
    print('INFORMATION')
    print('A new CSV file will be created with three columns: tweet ID, tweet and sentiment annotation.')
    print('Sentiment annotations are: negative (1), neutral (2) or positive (3).')
    print('Input the corresponding number to annotate the sentiment and press enter.')
    print('Entries are appended to the new CSV file.')
    print('\r\n')

def main():
    welcome_and_instruct()
    get_file_name()

if __name__ == '__main__':
    main()
