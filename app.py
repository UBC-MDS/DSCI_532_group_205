import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import altair as alt
import vega_datasets
import pandas as pd

from dash.dependencies import Input, Output
from src import lower_chart
from src import upper_chart


app = dash.Dash(__name__, assets_folder='assets')
server = app.server

def get_data():
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
df = get_data()
genres = sorted(list(df["Major_Genre"].dropna().unique()))
ratings = ["G", "PG", "PG-13", "R", "NC-17", "Open", "None"]
years = sorted(list(df["Release_Year"].dropna().astype(str).unique()))

#
# Default values for filters
#
default_genres = ["Action", "Adventure", "Comedy", "Drama", "Horror", "Romantic Comedy", "Thriller/Suspense"]
default_ratings = ["PG", "PG-13", "R"]

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
                )
            ], className="app-main--rating-container  app-main--filter-panel"),
            html.Div([
                html.P("Release Year", className="app-main--container-title"),
                html.Div([
                    html.Div([
                        html.P("from", className="app-main--dropdown-title"),
                        dcc.Dropdown(id="dd-year-from",
                                     options=[{"label": year, "value": year} for year in years],
                                     value=years[0],
                                     className="app-main--dropdown")
                    ], className="app-main--dropdown-wrapper"),
                    html.Div([
                        html.P("to", className="app-main--dropdown-title"),
                        dcc.Dropdown(id="dd-year-to",
                                     options=[{"label": year, "value": year} for year in years],
                                     value=years[-1],
                                     className="app-main--dropdown")
                    ], className="app-main--dropdown-wrapper")
                ], className="app-main--year-selector")
            ], className="app-main--year-container app-main--filter-panel")
        ], className="app-main--panel-left"),
        html.Div([
            html.Div([
                html.Iframe(sandbox="allow-scripts",
                            id="chart_upper",
                            height="100%",
                            width="100%",
                            className="upper-chart--iframe",
                            srcDoc="")
            ], className="app-main--panel-right-upper"),
            html.Div([
                html.Iframe(sandbox="allow-scripts",
                            id="chart_lower",
                            height="100%",
                            width="100%",
                            className="lower-chart--iframe",
                            srcDoc="")
            ], className="app-main--panel-right-lower")
        ], className="app-main--panel-right")
    ], className="app-main--container"),
], className="wrapper")

#
# Update charts when any of the filters are changed
#
@app.callback([dash.dependencies.Output("chart_upper", "srcDoc"),
               dash.dependencies.Output("chart_lower", "srcDoc")],
              [dash.dependencies.Input("cb-genres", "value"),
               dash.dependencies.Input("cb-ratings", "value"),
               dash.dependencies.Input("dd-year-from", "value"),
               dash.dependencies.Input("dd-year-to", "value")])
def update_charts(genre, rating, year_from, year_to):
    return (upper_chart.create_upper_chart(df, genre, rating, year_from, year_to).to_html(),
            lower_chart.create_lower_chart(df, genre, rating, year_from, year_to).to_html())

if __name__ == '__main__':
    app.run_server(debug=True)
