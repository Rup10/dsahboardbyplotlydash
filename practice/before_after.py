from dash import Dash, dcc, html, Input, Output
from dash_extensions import BeforeAfter
import dash_bootstrap_components as dbc

app = Dash(__name__)

app.layout = html.Div([
    BeforeAfter(before=dict(src="/assets/goku-ssj.jpg"), after=dict(src="/assets/goku.png"), width='256', height='256')
])

app.run_server(debug=True)
