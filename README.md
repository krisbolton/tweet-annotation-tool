# Tweet Annotation Tool
A simple CLI tool to annotate tweets with sentiment to create sentiment analysis datasets.

## Installation

Run the requirements.txt file

`pip install -r requirements.txt`

Requirements list:

* click
* pyfiglet
* pandas

## Usage Instructions

Navigate to the Tweet Annotation Tool (TAT) folder in your terminal and type:

`python tat.py --file [FILENAME]`

FILENAME is the name of the CSV file containing at least the tweet ID and tweet. You can use a CSV containing all 31 columns, only ID and tweet will be used.

You can also run the program without flags:

`python tat.py`

Once a file has been provided TAT will display the tweets to you and ask for the sentiment to annotate.

## Further Details

TODO
