import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import base64

from apps import real_estate

import requests
import pandas as pd

banner = 'banner_crop.jpg'
banner_base64 = base64.b64encode(open(banner, 'rb').read()).decode('ascii')

#def chicago_count
#https://www.dph.illinois.gov/sitefiles/COVIDZip.json

url = "https://www.dph.illinois.gov/sitefiles/COVIDHistoricalTestResults.json"

response = requests.get(url)

data = response.json()
data = data['state_testing_results']['values']

d = {'date':[], 'total_tested':[], 'confirmed_cases':[], 'total_deaths':[]}
for v in data:
    d['date'].append(v['testDate'])
    d['total_tested'].append(v['total_tested'])
    d['confirmed_cases'].append(v['confirmed_cases'])
    d['total_deaths'].append(v['deaths'])

df = pd.DataFrame(d)
df['tested'] = df['total_tested'].shift(1)
df['tested'] = df['total_tested'] - df['tested']

df['deaths_by_day'] = df['total_deaths'].shift(1)
df['deaths_by_day'] = df['total_deaths'] - df['deaths_by_day']

df['confirmed_cases_by_day'] = df['confirmed_cases'].shift(1)
df['confirmed_cases_by_day'] = df['confirmed_cases'] - df['confirmed_cases_by_day']

df['date'] = df['date'].map(lambda x: pd.to_datetime(x))


fig = go.Figure()

fig.add_trace(
                go.Scatter(
                            x = df['date'],
                            y = df['confirmed_cases_by_day'],
                            mode='lines',
                            opacity=0.7,
                            marker={'size':5.5}
                            )
                )

fig.update_layout(
                title="Illinois Confirmed COVID-19 Cases by Day", 
                title_x=0,
                xaxis={"title":"Date",
                        "titlefont":dict(
                                            size = 13
                                        )},
                yaxis={"title":"Confirmed Cases",
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
                    dcc.Link('Weather', href='/apps/weather')
                ], style={'padding': 10}),

                html.Div([
                    dcc.Link('Real Estate', href='/apps/real_estate')
                ], style={'padding': 10}),
                dcc.Graph(id='covid_graph',
                          style={'height': '400px', 'width': '75%'},
                          figure=fig),
                html.H6('Source: dph.illinois.gov')
])
