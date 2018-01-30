from .data import importData, splitData, validateInput
from .tfidf import trainEngine, getSimilarities
from .output import printYellow, printGreen, prettyPrint

green = 'green'  # Green colored text
yellow = 'yellow'  # Yellow-colored text


def recommender(movieID=2874,
                recommendationsNumber=3,
                showPlots=False,
                interactive=False):
    # Validate the user input
    validateInput(movieID, recommendationsNumber)
    # Import the data
    data = importData(interactive)
    # Get the metadatasets
    dataset = splitData(data, interactive)
    # Train the recommendation engine
    results = trainEngine(dataset['plots'], interactive)
    # Generate recommendations
    recomendedMovies = getSimilarities(movieID, recommendationsNumber, results,
                                       interactive)
    # Input movie
    printGreen('❯ Given Movie')
    prettyPrint(
        movieID=movieID,
        title=dataset['titles'][movieID],
        category=dataset['categories'][movieID],
        plot=dataset['plots'][movieID],
        color=green,
        showPlots=showPlots)
    # Display the recommended movies
    printYellow('★ Top ' + str(recommendationsNumber) + ' Recommendations')
    for i in recomendedMovies:
        prettyPrint(
            movieID=i,
            title=dataset['titles'][i],
            category=dataset['categories'][i],
            plot=dataset['plots'][i],
            color=yellow,
            showPlots=showPlots)
    return 0
