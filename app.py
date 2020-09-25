import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from apps import climate, covid, real_estate, weather

import base64
import dash

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

banner = 'banner_crop.jpg'
banner_base64 = base64.b64encode(open(banner, 'rb').read()).decode('ascii')

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/climate':
        return climate.layout
    elif pathname == '/apps/covid':
        return covid.layout
    elif pathname == '/apps/real_estate':
        return real_estate.layout
    elif pathname == '/apps/weather':
        return weather.layout
    else:
        return covid.layout

# if you want to run locally
if __name__ == '__main__':
    app.run_server(debug=True, port=5000)
