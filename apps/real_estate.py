import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import base64

import pandas as pd

banner = 'banner_crop.jpg'
banner_base64 = base64.b64encode(open(banner, 'rb').read()).decode('ascii')

sample = pd.read_csv("chicago-luxury-real-estate.csv")

fig = go.Figure()

fig.add_trace(
                go.Scatter(
                            x = sample['date_seen'],
                            y = sample['pct_vacant'],
                            mode='lines',
                            opacity=0.7,
                            marker={'size':5.5}
                            )
                )

fig.update_layout(
                title="Chicago Class A Buildings Vacancy Activity", 
                title_x=0,
                xaxis={"title":"Date",
                        "titlefont":dict(
                                            size = 13
                                        )},
                yaxis={"title":"Mean Vacancy Rate",
                        "titlefont":dict(
                                            size = 13
                                        ),
                        "showticklabels": True}
                 )

fig_rent = go.Figure()

fig_rent.add_trace(
                go.Scatter(
                            x = sample['date_seen'],
                            y = sample['mean_rent'],
                            mode='lines',
                            opacity=0.7,
                            marker={'size':5.5}
                            )
                )

fig_rent.update_layout(
                title="Chicago Class A Buildings Rent Activity", 
                title_x=0,
                xaxis={"title":"Date",
                        "titlefont":dict(
                                            size = 13
                                        )},
                yaxis={"title":"Mean One Bedroom Rent",
                        "titlefont":dict(
                                            size = 13
                                        ),
                        "showticklabels": True}
                 )

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

                dcc.Graph(id='real_estate_graph_vac',
                          style={'height': '400px', 'width': '40%'},
                          figure=fig),
                dcc.Graph(id='real_estate_graph_rent',
                          style={'height': '400px', 'width': '40%'},
                          figure=fig_rent),
])
