import time
import pandas as pd

from .output import printGreen
from os.path import join, dirname

parentPath = dirname(__file__)  # Relative path to parent directory
moviesCSVPath = join(parentPath,
                     'dataset/movies.csv')  # Path to movies dataset


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
