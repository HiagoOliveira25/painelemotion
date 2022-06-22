import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from datetime import datetime
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
import pandas as pd

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3', 'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
arquivo = pd.read_csv('bitcoin_data.csv', names=header_list)


card_style = {
    'padding':'10px'
}
app.layout = html.Div([

    dbc.Row([
        dbc.Col([
            dbc.CardImg(src = "assets/logo_branco.png",
                     style = {'height':'67px',
                                'width':'135px',
                                'padding-left':'1vh'})
                ], width=4
        ),
        dbc.Col([
            html.Div("FÓRMULA E.MOTION UFPB", 
                    style = {'color': 'white', 'fontSize': 30, 'textAlign': 'center'})
                ], width=4
        ),
        dbc.Col([
            dbc.CardImg(src = "assets/logoufpb.png",
                    className = 'align-self-right',
                     style = {'height':'64px',
                                'width':'45px',
                                })
                ], width=4
        ),
    ]),

    dbc.Row(html.Hr(),style = {'padding-top':'1vh'}),
    html.Div([
        dcc.Interval(id = 'update_value',
                     interval = 500,
                     n_intervals = 0)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H1('card 1')),
                dbc.CardBody(html.Div(id='text_row1'))
            ], color='success', style = card_style)
        ], width= 4),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H1('card 2')),
                dbc.CardBody(html.Div(id='text_row2'))
            ], color='success', style = card_style)
        ], width= 4),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H1('card 3')),
                dbc.CardBody(html.Div(id='text_row3'))
            ], color='success', style = card_style)
        ], width= 4),
    ], className="mb-4"),
])

@app.callback(Output('text_row1','children'),
                [Input('update_value','n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        t1_r1 = arquivo['Temperatura1'].tail(1).iloc[0]
    if t1_r1 > 60:
        return [
                    html.Div([
                        html.H6('{0:,.2f}'.format(t1_r1),
                                style={'color': 'red',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(t1_r1),
                                style={'color': 'red',
                                       'font-weight': 'bold'},),
                    ]),
                
        ]

@app.callback(Output('text_row2','children'),
                [Input('update_value','n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        t2_r1 = arquivo['Temperatura2'].tail(1).iloc[0]
    if t2_r1 > 60:
        return [
                    html.Div([
                        html.H6('{0:,.2f}'.format(t2_r1),
                                style={'color': 'red',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(t2_r1),
                                style={'color': 'red',
                                       'font-weight': 'bold'},),
                    ]),
                
        ]

@app.callback(Output('text_row3','children'),
                [Input('update_value','n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        t3_r1 = arquivo['Temperatura3'].tail(1).iloc[0]
    if t3_r1 > 60:
        return [
                    html.Div([
                        html.H6('{0:,.2f}'.format(t3_r1),
                                style={'color': 'red',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(t3_r1),
                                style={'color': 'red',
                                       'font-weight': 'bold'},),
                    ]),
                
        ]
if __name__ == '__main__':
    app.run_server(debug = True, port = 2020)