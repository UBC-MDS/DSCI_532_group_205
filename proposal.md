# Proposal 

## Section 1: Motivation and Purpose

>In today’s world, we are overwhelmed by so many choices everywhere. It even applies to things we do for entertainment. For example, if we want to watch a movie, we could easily waste several minutes trying to find a right one. To save those precious minutes, we plan to create an app that in no time can help us find the perfect movie. This app will allow us to search for movies based on their genres, ratings and release years. Based on these settings, the app will show us the top 10 highest grossing movies. We can then interactively pick a movie from that list to see its viewer rating in comparison to the other similar movies. Briefly, with few clicks, this app will search hundreds of movies to find a perfect movie for us.  

## Section 2: Description of the data

> The dataset contains the record of around 3200 movies. For each movie, we have different types of information available, starting from basic information (`Title`, `Major_Genre`, `Release_Date`, `Running_Time_min`, `Director`) to some miscellaneous data (`Distributor`, `Creative_Type`, `Source`). The data also includes the cost and revenue (`US_Gross`, `Worldwide_Gross`, `Production_Budget`, `US_DVD_Sales`) along with the ratings (`MPAA_Rating`, `Rotten_Tomatoes_Rating`, `IMDB_Rating`, `IMDB_Votes`) for each movie. For the app, the movies will be searched based on `Major_Genre`, `MPAA_Rating` and `Release_Date`, and the results will be displayed based on `Worldwide_Gros Interactively, the viewer rating for each movie will be displayed based on a new variable called `overall_rating` using the information from `Rotten_Tomatoes_Rating` and `IMDB_Rating`. 

