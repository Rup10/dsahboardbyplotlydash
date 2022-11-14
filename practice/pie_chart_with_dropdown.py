import pandas as pd
import numpy as np
import plotly
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

df = pd.read_csv("Urban_Park_Ranger_Animal_Condition.csv")

app.layout = html.Div([
    dcc.Dropdown(
        id="my_dropdown",
        options=[
            {'label': "species", 'value': 'Animal Class'},
            {'label': 'Final Ranger Action', 'value': 'Final Ranger Action'},
            {'label': "age", 'value': 'Age'},
            {'label': 'health', 'value': "Animal Condition"},
            {'label': 'Borough', 'value': 'Borough'},
            {'label': 'Species status', 'value': 'Species Status'}
        ],
        # dropdown other arguments
        # optionHeight=20,
        value='Animal Class',
        # disabled=False,
        # multi=False,
        # searchable=True,
        # search_value="",
        placeholder="please select any option",
        clearable=False,
        style={'width': '50%'},
        # className='select_box',
        # persistence=True,
        # persistence_type='memory',
        # session and local are other values we can use instead of memory
    ),

    html.Div([
        dcc.Graph(
            id='the_graph'
        )
    ]),
])



@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    Input(component_id="my_dropdown", component_property='value')
)
def update_graph(my_dropdown):
    dff = df
    dff_2 = df[df['Borough']=='Bronx']
    piechart = px.pie(
        data_frame=dff,
        names=my_dropdown, # first two lines of px.pie are similer to df["Age"], where Age is a column in the dataframe df
        hole=0.7,
    )
    return (piechart)


app.run_server(debug=True)
