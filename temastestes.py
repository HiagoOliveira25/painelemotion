import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_daq as daq

app = dash.Dash(__name__)

theme = {
    'dark': True,
    'detail': '#007439',
    'primary': 'white',
    'secondary': '#6E6E6E',
}

rootLayout = html.Div([
    daq.LEDDisplay(
        value="3.0009",
        color=theme['primary'],
        id='darktheme-daq-leddisplay',
        className='dark-theme-control'
    ), html.Br(),
])

app.layout = html.Div(id='dark-theme-container', children=[
    html.Div(id='dark-theme-components-1', children=[
        daq.DarkThemeProvider(theme=theme, children=rootLayout)
    ], style={
        'border': 'solid 1px #A2B1C6',
        'border-radius': '5px',
        'padding': '50px',
        'margin-top': '20px'
    })
], style={'padding': '50px'})



if __name__ == '__main__':
    app.run_server(debug=True)