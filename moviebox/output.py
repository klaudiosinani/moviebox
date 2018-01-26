import re
import sys

from colorama import init
from termcolor import colored

init()  # Termcolor support for win32

red = 'red'  # Red-colored text
green = 'green'  # Green-colored text
yellow = 'yellow'  # Yellow-colored text
magenta = 'magenta'  # Magenta colored text

helpMessage = '''
  🎥 Machine learning movie recommender

  Usage
  $ moviebox [<options> ...]

  Options
    --help, -h               Display help message
    --movie, -m              Input movie ID
    --plot, -p               Display movie plot
    --interactive, -i        Display progress info
    --recommendations, -r    Number of movie recommendations
    --version, -v            Display installed version

   Examples
    $ moviebox --help
    $ moviebox --movie 2874
    $ moviebox -m 2874 --recommendations 3
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


def validateInput(movieID, recommendationsNumber):
    if not (isinstance(movieID, int) and movieID >= 0 and movieID <= 4999):
        printRed('Invalid value for movie ID: "' + str(movieID) + '"')
        printRed('Input is not a valid Natural number between [0, 4999]')
        sys.exit(1)
    if not (isinstance(recommendationsNumber, int)
            and recommendationsNumber >= 1 and recommendationsNumber <= 30):
        printRed('Invalid value for recommendations number: "' +
                 str(recommendationsNumber) + '"')
        printRed('Input is not a valid Natural number between [1, 30]')
        sys.exit(1)
    return 0


def displayHelpMessage():
    # Display cli help message
    print(helpMessage)


def displayVersion(version):
    # Display installed version
    print('Moviebox ' + version)
