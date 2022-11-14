import pandas as pd
import plotly
import plotly.express as px


# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output

from dash import Dash, dcc, html, Input, Output

# print("hello world")

app = Dash(__name__)

df = pd.read_csv("Urban_Park_Ranger_Animal_Condition.csv")

# print(df)

app.layout = html.Div([
    dcc.Dropdown(
        id="my_dropdown",
        options=[
            {'label': "species", 'value': 'Animal Class'},
            {'label': 'Final Ranger Action', 'value': 'Final Ranger Action'},
            {'label': "age", 'value': 'Age', 'disabled': True},
            {'label': 'Borough', 'value': 'Borough'},
            {'label': 'Species status', 'value': 'Spicies Status'}
        ],
        optionHeight=20,
        value='Borough',
        disabled=False,
        multi=True,
        searchable=True,
        search_value="",
        placeholder="please select any option",
        clearable=True,
        # style={'width': '80%'},
        className='select_box',
        persistence=True,
        persistence_type='memory',
        # session and local are other values we can use instead of memory
    )
])

app.run_server(debug=True)