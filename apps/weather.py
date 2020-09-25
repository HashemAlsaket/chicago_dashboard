import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import requests
import urllib
from bs4 import BeautifulSoup
import base64

from PIL import Image
from io import BytesIO

banner = 'banner_crop.jpg'
banner_base64 = base64.b64encode(open(banner, 'rb').read()).decode('ascii')

page = requests.get("https://www.weather.gov/lot/weatherstory")
soup = BeautifulSoup(page.content, "html.parser")
for img in soup.find_all('img'):
    if '/images/lot/wxstory' in img['src']:
        img_url = img['src']

response = requests.get("https://www.weather.gov" + img_url)
weather_today = BytesIO(response.content)
weather_today_base64 = base64.b64encode(weather_today.read()).decode('ascii')

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

                html.Div([
                            html.Img(src='data:image/png;base64,{}'.format(weather_today_base64), style={'height': '50%', 'width': '50%'}),
                            ]),
])
