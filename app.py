import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import altair as alt
import vega_datasets

app = dash.Dash(__name__, assets_folder='assets')
server = app.server

app.title = 'Seek-A-Movie'

genres = ['Action', 'Adventure', 'Black Comedy', 'Comedy', 'Concert/Performance', 'Documentary', 'Drama', 'Horror', 'Musical', 'Romantic Comedy', 'Thriller/Suspense', 'Western']

app.layout = html.Div([
    html.H1("Seek-A-Movie"),
    html.Div([
        html.Div([
            html.Div([
                html.P("Genre", className="app-main--container-title"),
                dcc.Checklist(
                    className="app-main--genre-cb-container",
                    inputClassName="app-main--genre-input",
                    labelClassName="app-main--genre-label",
                    options=[{"label": genre, "value": genre} for genre in genres],
                    value=[]
                )
            ], className="app-main--genre-container"),
            html.Div([
                html.P("MPAA Rating", className="app-main--container-title"),
            ], className="app-main--rating-container"),
            html.Div([
                html.P("Release Year", className="app-main--container-title"),
            ], className="app-main--year-container")
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
])

if __name__ == '__main__':
    app.run_server(debug=True)
