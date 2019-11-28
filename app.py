import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import altair as alt
import vega_datasets

app = dash.Dash(__name__, assets_folder='assets')
server = app.server

app.title = "Seek-a-Movie"

genres = ['Action', 'Adventure', 'Black Comedy', 'Comedy', 'Concert/Performance', 'Documentary', 'Drama', 'Horror', 'Musical', 'Romantic Comedy', 'Thriller/Suspense', 'Western']
ratings = ["G", "PG", "PG-13", "R", "NC-17", "Open", "None"]

app.layout = html.Div([
    html.H1("Seek-a-Movie"),
    html.Div([
        html.Div([
            html.Div([
                html.P("Genre", className="app-main--container-title"),
                dcc.Checklist(
                    className="app-main--genre-cb-container",
                    inputClassName="app-main--cb-input",
                    labelClassName="app-main--cb-label",
                    options=[{"label": genre, "value": genre} for genre in genres],
                    value=[]
                )
            ], className="app-main--genre-container app-main--filter-panel"),
            html.Div([
                html.P("MPAA Rating", className="app-main--container-title"),
                dcc.Checklist(
                    className="app-main--rating-cb-container",
                    inputClassName="app-main--cb-input",
                    labelClassName="app-main--cb-label",
                    options=[{"label": rating, "value": rating} for rating in ratings],
                    value=[]
                )
            ], className="app-main--rating-container  app-main--filter-panel"),
            html.Div([
                html.P("Release Year", className="app-main--container-title"),
                html.Div([
                    html.Div([
                        html.P("from", className="app-main--dropdown-title"),
                        dcc.Dropdown(options=[{'label':x, 'value': x} for x in range(1999, 2018)],
                                     className="app-main--dropdown")
                    ], className="app-main--dropdown-wrapper"),
                    html.Div([
                        html.P("to", className="app-main--dropdown-title"),
                        dcc.Dropdown(options=[{'label':x, 'value': x} for x in range(1999, 2018)],
                                     className="app-main--dropdown")
                    ], className="app-main--dropdown-wrapper")
                ], className="app-main--year-selector")
            ], className="app-main--year-container app-main--filter-panel")
        ], className="app-main--panel-left"),
        html.Div([
            html.Div([
                html.P("Chart (Furqan)")
            ], className="app-main--panel-right-upper"),
            html.Div([
                html.P("Chart (Sree)")
            ], className="app-main--panel-right-lower")
        ], className="app-main--panel-right")
    ], className="app-main--container")
], className="wrapper")

if __name__ == '__main__':
    app.run_server(debug=True)
