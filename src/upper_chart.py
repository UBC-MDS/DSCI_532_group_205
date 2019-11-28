import altair as alt
from src import theme

def create_upper_chart(df, genres, ratings, year_from, year_to):
    """Create upper chart.

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

    filtered_df = df.query(f"{year_from} <= Release_Date <= {year_to}")

    return alt.Chart(filtered_df).mark_line().encode(
        alt.X("year(Release_Date):T"),
        alt.Y("US_Gross:Q")
    ).properties(
        width=540,
        height=200
    )
