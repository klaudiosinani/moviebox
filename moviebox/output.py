import re

from colorama import init
from termcolor import colored

init()  # Termcolor support for win32

red = 'red'  # Red-colored text
green = 'green'  # Green-colored text
yellow = 'yellow'  # Yellow-colored text
magenta = 'magenta'  # Magenta colored text

helpMessage = '''
  🎥  Machine learning movie recommender

  Usage
    $ moviebox [<options> ...]

  Options
    --help, -h              Display help message
    --search, -s            Search movie by ID
    --movie, -m <int>       Input movie ID [Can be any integer 0-4999]
    --plot, -p              Display movie plot
    --interactive, -i       Display process info
    --list, -l              List available movie titles
    --recommend, -r <int>   Number of recommendations [Can be any integer 1-30]
    --version, -v           Display installed version

  Examples
    $ moviebox --help
    $ moviebox --search
    $ moviebox --movie 2874
    $ moviebox -m 2874 --recommend 3
    $ moviebox -m 2874 -r 3 --plot
    $ moviebox -m 2874 -r 3 -p --interactive
'''


def printYellow(msg):
    # Print a yellow-colored text message
    print(colored(msg, yellow))


def printGreen(msg):
    # Print a green-colored text message
    print(colored(msg, green))


def printMagenta(msg):
    # Print a magenta-colored text message
    print(colored(msg, magenta))


def printRed(msg):
    # Print a red-colored text message
    print(colored(msg, red))


def prettyPrint(movieID, title, category, plot, color, showPlots):
    # Clean-up movie category
    prettyCategory = re.sub('  ', ' ', category)
    prettyCategory = re.sub('[\"]', '', prettyCategory)
    # Pretty print the info
    print(colored('• Title: ' + title + ' - ID: ' + str(movieID), color))
    print(colored('  Categories: ' + prettyCategory + '\n', color))
    if (showPlots):
        print(colored('  Plot:\n' + plot + '\n', color))


def displayHelpMessage():
    # Display cli help message
    print(helpMessage)


def displayVersion(version):
    # Display installed version
    print('Moviebox ' + version)
