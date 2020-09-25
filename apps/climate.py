import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import plotly.graph_objs as go
import base64

from apps import real_estate

import requests
import pandas as pd

banner = 'banner_crop.jpg'
banner_base64 = base64.b64encode(open(banner, 'rb').read()).decode('ascii')

# Source NOAA

df = pd.DataFrame({
                'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
                'Low °F': [22, 26, 34, 43, 53, 63, 70, 70, 62, 50, 39, 27],
                'High °F': [32, 36, 45, 56, 66, 77, 82, 81, 74, 62, 50, 37],
                'Days of Rain': [5, 7, 5, 7, 7, 9, 6, 6, 5, 7, 4, 7]
                })

layout = html.Div([

                html.Div([
                            html.Img(src='data:image/png;base64,{}'.format(banner_base64), style={'width': '100%'}),
                            ]),
                html.H3('Choose Category'),
                html.Div([
                    dcc.Link('Climate', href='/apps/climate')
                ], style={'padding': 10}),
                html.Div([
                    dcc.Link('COVID-19', href='/apps/covid')
                ], style={'padding': 10}),
                html.Div([
                    dcc.Link('Real Estate', href='/apps/real_estate')
                ], style={'padding': 10}),
                html.Div([
                    dcc.Link('Weather', href='/apps/weather')
                ], style={'padding': 10}),

                html.H4('Temperature by Month'),
                dash_table.DataTable(
                                            data=df.to_dict('records'),
                                            id='climate_datatable',
                                            columns=[
                                                    {"name": i, "id": i} for i in ['Month', 'Low °F', 'High °F', 'Days of Rain']
                                                    ],
                                                    page_current=0,
                                            style_table={
                                                            'maxHeight': '500px',
                                                            'width': '50%',
                                                            'minWidth': '75%',
                                                        },
                                            style_cell={
                                                        'whiteSpace': 'normal',
                                                        'fontSize':12, 'font-family':'sans-serif',
                                                        'textAlign': 'right',
                                                        'text': 'black'
                                                    },
                                            style_cell_conditional=[
                                                            {'if': {'column_id': 'Month'},
                                                             'width': '10%'},
                                                            {'if': {'column_id': 'Low °F'},
                                                             'width': '10%'},
                                                            {'if': {'column_id': 'High °F'},
                                                             'width': '10%'},
                                                            {'if': {'column_id': 'Days of Rain'},
                                                             'width': '10%'},
                                                        ]
                                        ),
                html.H6('Source: NOAA')
                  ])
