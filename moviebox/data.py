import sys
import time
import pandas as pd

from os.path import join, dirname
from .output import prettyPrint, printRed, printGreen

parentPath = dirname(__file__)  # Relative path to parent directory
moviesCSVPath = join(parentPath,
                     'dataset/movies.csv')  # Path to movies dataset

yellow = 'yellow'  # Yellow colored text


def importData(verbose):
    start = time.time()
    # Import movie dataset
    moviesDF = pd.read_csv(moviesCSVPath)
    if (verbose):
        printGreen('✔ Imported Data\t\t{0:.1f}s'.format(time.time() - start))
    # Return the imported datasets
    return moviesDF


def splitData(moviesDF, verbose):
    start = time.time()
    # Get movie titles
    titles = moviesDF[['Title']].values.flatten().tolist()
    # Get movie categories
    categories = moviesDF[['Category']].values.flatten().tolist()
    # Get movie plot summaries
    plots = moviesDF[['Plot']].values.flatten().tolist()
    if (verbose):
        printGreen('✔ Split Data\t\t{0:.1f}s'.format(time.time() - start))
    # Pack and return the split data
    return {'titles': titles, 'categories': categories, 'plots': plots}


def validateInput(movieID, recommendationsNumber):
    # Check whether the input ID is valid
    if not (isinstance(movieID, int) and movieID >= 0 and movieID <= 4999):
        printRed('Invalid value for movie ID: "' + str(movieID) + '"')
        printRed('Input is not a valid Natural number between [0, 4999]')
        sys.exit(1)
    # Check whether the recommendations number is valid
    if not (isinstance(recommendationsNumber, int)
            and recommendationsNumber >= 1 and recommendationsNumber <= 30):
        printRed('Invalid value for recommendations number: "' +
                 str(recommendationsNumber) + '"')
        printRed('Input is not a valid Natural number between [1, 30]')
        sys.exit(1)
    return 0


def searchMovie(movieID):
    # Search a movie title by ID
    data = importData(verbose=False)
    dataset = splitData(data, verbose=False)
    # Check whether the input ID is valid
    if not (isinstance(movieID, int) and movieID >= 0 and movieID <= 4999):
        printRed('Invalid value for movie ID: "' + str(movieID) + '"')
        printRed('Input is not a valid Natural number between [0, 4999]')
        sys.exit(1)
    else:
        # Display the search result
        prettyPrint(
            movieID=movieID,
            title=dataset['titles'][movieID],
            category=dataset['categories'][movieID],
            plot=dataset['plots'][movieID],
            color=yellow,
            showPlots=False)
