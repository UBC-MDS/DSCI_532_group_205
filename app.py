import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import altair as alt
import vega_datasets
import pandas as pd

from src import lower_chart
from src import upper_chart

app = dash.Dash(__name__, assets_folder='assets')
server = app.server


def get_data():
    """Create wrangled dataset for charts
    Returns
    -------
    DataFrame:
        Pandas DataFrame with wrangled Movies data
    """
    df = vega_datasets.data.movies()

    # Convert string dates to `datetime`
    df["Release_Date"] = pd.to_datetime(df["Release_Date"], format="%b %d %Y")

    # Fix invalid dates that are in wrong century
    df.loc[df["Release_Date"] > "2012", "Release_Date"] -= pd.DateOffset(years=100)

    # Having just the year separated from the full data will make charting and querying easier
    df["Release_Year"] = df["Release_Date"].dt.year

    return df


app.title = "Seek-a-Movie"

#
# Prepare movies DataFrame
#
movies_df = get_data()
genres = sorted(list(movies_df["Major_Genre"].dropna().unique()))
ratings = ["G", "PG", "PG-13", "R", "NC-17"]
years = sorted(list(movies_df["Release_Year"].dropna().astype(str).unique()))

#
# Default values for filters
#
default_genres = ["Action", "Adventure", "Comedy", "Drama", "Horror", "Romantic Comedy", "Thriller/Suspense"]
default_ratings = ["PG", "PG-13", "R"]

pts = alt.selection(type="single", encodings=['y'], fields=["Title"])

#
# App layout
#
app.layout = html.Div([
    dbc.Row(
        [html.H1("Seek-a-Movie", className="display-3"),
         html.P("Interactive Movie Selector",
                className="lead"),
         html.P("Displays the top 10 highest grossing US movies based on your taste.",
                className="lead"),
         html.P("Compare the IMDB and Rotten Tomatoes ratings to help you decide what to watch!",
                className="lead"),
         ],
        className="app-main--first-title",
    ),
    html.Div([
        html.Div([
            html.Div([
                html.P("Genres", className="app-main--container-title"),
                dcc.Checklist(
                    id="cb-genres",
                    className="app-main--genre-cb-container",
                    inputClassName="app-main--cb-input",
                    labelClassName="app-main--cb-label",
                    options=[{"label": genre, "value": genre} for genre in genres],
                    value=default_genres
                )
            ], className="app-main--genre-container app-main--filter-panel"),
            html.Div([
                html.P("MPAA Ratings", className="app-main--container-title"),
                dcc.Checklist(
                    id="cb-ratings",
                    className="app-main--rating-cb-container",
                    inputClassName="app-main--cb-input",
                    labelClassName="app-main--cb-label",
                    options=[{"label": rating, "value": rating} for rating in ratings],
                    value=default_ratings
                ),
                html.P("G: general audience", className="app-main--container-title"),
                html.P("PG: parental guidance suggested", className="app-main--container-title"),
                html.P("PG-13: parents strongly cautioned", className="app-main--container-title"),
                html.P("R: restricted", className="app-main--container-title"),
                html.P("NC-17: adults only", className="app-main--container-title")
            ], className="app-main--rating-container  app-main--filter-panel"),
            html.Div([
                html.P("Release Year", className="app-main--container-title"),
                html.Div([
                    html.Div([
                        html.P("from", className="app-main--dropdown-title"),
                        dcc.Dropdown(id="dd-year-from",
                                     options=[{"label": year, "value": year} for year in years],
                                     value=years[0],
                                     className="app-main--dropdown",
                                     clearable=False)
                    ], className="app-main--dropdown-wrapper"),
                    html.Div([
                        html.P("to", className="app-main--dropdown-title"),
                        dcc.Dropdown(id="dd-year-to",
                                     options=[{"label": year, "value": year} for year in years],
                                     value=years[-1],
                                     className="app-main--dropdown",
                                     clearable=False)
                    ], className="app-main--dropdown-wrapper")
                ], className="app-main--year-selector")
            ], className="app-main--year-container app-main--filter-panel")
        ], className="app-main--panel-left"),
        html.Div([
            html.Div([
                html.Iframe(sandbox="allow-scripts",
                            id="chart",
                            height="100%",
                            width="100%",
                            className="upper-chart--iframe",
                            srcDoc="")
            ], className="app-main--panel-right-upper")
        ], className="app-main--panel-right")
    ], className="app-main--container"),
], className="wrapper")


#
# Update charts when any of the filters are changed
#
@app.callback(dash.dependencies.Output("chart", "srcDoc"),
              [dash.dependencies.Input("cb-genres", "value"),
               dash.dependencies.Input("cb-ratings", "value"),
               dash.dependencies.Input("dd-year-from", "value"),
               dash.dependencies.Input("dd-year-to", "value")])
def update_charts(genre, rating, year_from, year_to):
    upper_chart_rendered = upper_chart.create_upper_chart(
        movies_df, pts, genre, rating, year_from, year_to
    ).properties(
        width=400,
        height=280
    )

    lower_chart_rendered = lower_chart.create_lower_chart(
        movies_df, pts, genre, rating, year_from, year_to
    ).properties(
        width=400,
        height=220
    )

    charts = alt.vconcat(upper_chart_rendered, lower_chart_rendered)

    charts.configure_axis(
        labelFontSize=15,
        titleFontSize=20
    ).configure_title(
        fontSize=20
    )

    return charts.to_html()


if __name__ == '__main__':
    app.run_server(debug=True)
