import altair as alt
from src import theme

def create_lower_chart(df, genres, ratings, year_from, year_to):
    """Create lower chart.

    Parameters
    ----------
    df : DataFrame
       Source data
    genres : list
       List of genres
    ratings : list
       List of MPAA ratings
    year_from : string
       Starting year
    year_to : string
       Ending year

    Returns
    -------
    Chart :
        Altair chart
    """
   
    # register the custom theme under a chosen name
    alt.themes.register('mds_special', theme.mds_special)

    # enable the newly registered theme
    alt.themes.enable('mds_special')

    # Filter data as per user preference
    df["year"] = df.Release_Date.apply(lambda x: x.year)
    release_years = list(range(int(year_from), int(year_to) + 1))

    q = "Major_Genre in @genres & MPAA_Rating in @ratings & year in @release_years"
    df_filtered = df.copy().query(q)

    # Get top 20 grossing movies
    top_us_gross_df = df_filtered.sort_values("US_Gross", ascending=False)
    top_10 = top_us_gross_df.head(10).reset_index().drop(columns="index")
    top_10["rank"] = top_10.index + 1


    p1 = alt.Chart(df).mark_circle(opacity=0.4).encode(
	    alt.X("IMDB_Rating:Q", title="IMDB Rating"),
	    alt.Y("Rotten_Tomatoes_Rating:Q", title="Rotten Tomatoes Rating"),
	     alt.Tooltip(["IMDB_Rating", "Rotten_Tomatoes_Rating"])).interactive().properties(
	    title = "Movie Ratings",
	    width=340,
	    height=200)

    p2 = alt.Chart(top_10).mark_circle(size = 200,
                                  opacity=1).encode(
	    alt.X("IMDB_Rating:Q"),
	    alt.Y("Rotten_Tomatoes_Rating:Q"),
	    alt.Color("Title:O", scale=alt.Scale(scheme="set1")),
	    alt.Tooltip(["IMDB_Rating", "Rotten_Tomatoes_Rating", "Title"])).interactive().properties(
	    width=340,
	    height=200)

    combined_scatter = (p1 + p2).configure_axis(
                        titleFontSize = 20,
                        ).configure_title(
                        fontSize = 20,
                        ).configure_legend(titleFontSize = 20, labelFontSize = 15, labelLimit=1000)

    return  combined_scatter
