import sys
import click

from .recommender import recommender
from .data import searchMovie, listMovies
from .output import displayHelpMessage, displayVersion

movieboxVersion = '0.2.1'


@click.command(add_help_option=False)
@click.option('-m', '--movie', default=2874, help='Input movie ID')
@click.option(
    '-r', '--recommend', default=3, help='Number of movie recommendations')
@click.option(
    '-p', '--plot', is_flag=True, default=False, help='Display movie plot')
@click.option(
    '-i',
    '--interactive',
    is_flag=True,
    default=False,
    help='Display progress info')
@click.option(
    '-v',
    '--version',
    is_flag=True,
    default=False,
    help='Display installed version')
@click.option(
    '-h', '--help', is_flag=True, default=False, help='Display help message')
@click.option(
    '-s', '--search', is_flag=True, default=False, help='Search movie by ID')
@click.option(
    '-l', '--list', is_flag=True, default=False, help='List movie titles')
def main(movie, recommend, plot, interactive, help, version, search, list):
    if (help):
        displayHelpMessage()
        sys.exit(0)
    else:
        if (version):
            displayVersion(movieboxVersion)
        else:
            if (search):
                searchID = click.prompt('❯ Please enter a Movie ID', type=int)
                searchMovie(movieID=searchID)
            else:
                if (list):
                    listLength = click.prompt(
                        '❯ Number of Movies to list', type=int)
                    listMovies(length=listLength)
                else:
                    recommender(
                        movieID=movie,
                        recommendationsNumber=recommend,
                        showPlots=plot,
                        interactive=interactive)


if __name__ == '__main__':
    main()
