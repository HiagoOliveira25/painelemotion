import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

card_style = {
    'radius':'2px',
    'padding':'10px'
}
app.layout = html.Div([
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
                dbc.CardHeader('este é o titulo'),
                dbc.CardBody('este é o corpo')
            ], color='success',style={'height':'52vh','font-size':'5vh'})
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader('este é o titulo'),
                dbc.CardBody('este é o corpo')
                    ], color='primary')
        ])
    ], className="mb-4")
],style={'padding-top':'2vh'})


if __name__ == '__main__':
    app.run_server(debug = True, port = 4040)