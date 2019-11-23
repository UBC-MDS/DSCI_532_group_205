# Proposal

## Motivation and Purpose

TBA

## Description of the Data

This "movies" dataset is from the [Vega Datasets][1] collection. There are about 3200 movies with release years between 1920 to 2016. For each movie, we have different types of information available, starting from basic information (`Title`, `Major_Genre`, `Release_Date`, `Running_Time_min`, `Director`) to some miscellaneous data (`Distributor`, `Creative_Type`, `Source`). Financial information includes US & worldwide gross income, US DVD sales and production budget. Movies are categorized by a single `Major_Genre` (e.g. Action, Comedy), a `Creative_Type` (e.g. Fantasy, Super Hero) and an `MPAA_Rating` which are [ratings by the Motion Picture Association of America][2] (e.g. G, PG, R). There are up to two ratings per movie in the variables `Rotten_Tomatoes_Rating` and `IMDB_Rating`.

## Research Questions and Usage Scenarios

- What are the top US grossing movies based on genre, MPAA rating and release year range?
- How do these movies rate among other movies (in the dataset)?

Bob is an avid movie watcher and would like to discover past movies that he may have missed or re-discover movies that he's enjoyed in the past. He wants an easy way to narrow down the vast selection of movies available so he can spend more time watching movies as opposed to searching for them.

When Bob uses this "Seek-a-Movie" app, he'll be presented with two charts and some filter controls. The main chart will be interactive and will display the top movies by US gross income, filtered by all the user filter controls. The secondary chart, a scatter plot, displays Rotten Tomatoes ratings vs. IMBD ratings for the entire database. The ratings for the top movies listed in the first chart will be highlighted. This allows bob to visualize where the ratings for the filtered movie selection fall among all other ratings.

The filter controls allow Bob to filter movies by genre, MPAA rating and release year. Hovering over a movie will display associated meta data and selecting a movie will highlight its rating. This allows for easy discovery of movies.

[1]: https://github.com/vega/vega-datasets
[2]: https://en.wikipedia.org/wiki/Motion_Picture_Association_of_America_film_rating_system
