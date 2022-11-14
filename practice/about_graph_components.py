import pandas as pd
import numpy as np
import plotly
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df = px.data.gapminder()
external_style_sheet = ['assets/drop_down.css']
app = Dash(__name__, external_stylesheets=external_style_sheet)

app.layout = html.Div([
    dcc.Dropdown(
        id="drop1",
        multi=True,
        options=[
            {'label': x, 'value': x} for x in df.country.unique()
        ],
        value=["Germany", "Brazil"],
    ),

    html.Div([
        dcc.Graph(
            id='Pie-Graph',
            figure={},
            config={
                'staticPlot': False,             # True, False
                'scrollZoom': True,              # True, False
                'doubleClick': 'reset',           # 'reset', 'autosize' or 'reset+autosize',False
                'showTips': False,               # True, False
                'displayModeBar': False,           # True, False
                'watermark': False,
                # 'modeBatButtonsToRemove':['pan2d','select2d'],
            },
            className='six columns'
        ),
        dcc.Graph(
            id='Line-Graph',
            figure={},
            clickData=None,
            hoverData=None,

            config={
                'staticPlot': False,             # True, False
                'scrollZoom': True,              # True, False
                'doubleClick': 'reset',           # 'reset', 'autosize' or 'reset+autosize',False
                'showTips': False,               # True, False
                'displayModeBar': False,           # True, False
                'watermark': False,
                # 'modeBatButtonsToRemove':['pan2d','select2d'],
            },
            className='six columns'
        )
    ])

])


@app.callback(
    Output(component_id='Line-Graph', component_property='figure'),
    Input(component_id="drop1", component_property="value")
)
def update_line(selected_country):
    dff = df[df.country.isin(selected_country)]
    fig = px.line(
        data_frame=dff,
        x='year',
        y='pop',
        color='country',
        custom_data=['country', 'continent', 'lifeExp', 'pop'])
    fig.update_traces(mode='lines+markers')
    return fig


@app.callback(
    Output(component_id='Pie-Graph', component_property='figure'),
    Input(component_id="Line-Graph", component_property='hoverData'),
    Input(component_id="Line-Graph", component_property='clickData'),
    Input(component_id="Line-Graph", component_property='selectedData'),
    Input(component_id='drop1', component_property='value')
)
def update_pie(hov_data, clk_data, selc_data, drop_data):
    if hov_data is None:
        dff2 = df[df.country.isin(drop_data)]
        dff2 = dff2[dff2.year == 1952]
        print(dff2)

        fig2 = px.pie(
            data_frame=dff2,
            values='pop',
            names='country',
            title='Population for 1952')
        return fig2

    else:
        print(f'hover data :{hov_data}')
        print(hov_data['points'][0]['customdata'][0])
        print(hov_data['points'][0]['x'])
        dff2 = df[df.country.isin(drop_data)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.year == hov_year]
        # print(dff2)
        fig2 = px.pie(
            data_frame=dff2,
            values='pop',
            names='country',
            title=f'Population for {hov_year}'
        )
        return fig2

app.run_server(debug=True)