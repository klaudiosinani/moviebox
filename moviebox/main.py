from .recommender import recommender


def main():
    recommender(
        movieID=2874,
        recommendationsNumber=3,
        showPlots=False,
        interactive=True)


if __name__ == '__main__':
    main()
