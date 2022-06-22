import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from datetime import datetime
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SUPERHERO])

card_style = {
    'padding':'10px'
}
app.layout = html.Div([

    dbc.Row([
        dbc.Col([
            dbc.Card(
                dbc.CardBody(
                     dbc.CardImg(
                     src = "assets/logo_branco.png",
                     style = {'height':'67px',
                        'width':'135px',
                        'padding-left':'1vh'}
                        )
                    ), color = 'dark'
                ),
            ],
        ),
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H1('este é o1 titulo')),
                dbc.CardBody('este é o corpo')
            ], color='success', style = card_style)
        ], width= 4),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H1('este é o titulo')),
                dbc.CardBody('este é o corpo')
            ], color='success', style = card_style)
        ], width= 4),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H1('este é o titulo')),
                dbc.CardBody('este é o corpo')
            ], color='success', style = card_style)
        ], width = 4)
    ], className="mb-4"),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H1('este é o1 titulo')),
                dbc.CardBody('este é o corpo')
            ], color='success', style = card_style)
        ], width= 4),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H1('este é o titulo')),
                dbc.CardBody('este é o corpo')
            ], color='success', style = card_style)
        ], width= 4),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H1('este é o titulo')),
                dbc.CardBody('este é o corpo')
            ], color='success', style = card_style)
        ], width = 4)
    ], className="mb-4"),
])




if __name__ == '__main__':
    app.run_server(debug = True, port = 4080)