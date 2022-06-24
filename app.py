import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
import dash_daq as daq
from datetime import datetime
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
import pandas as pd


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3', 'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
arq = pd.read_csv('data.csv', names=header_list)


card_style = {
    'padding':'10px'
}
app.layout = html.Div([

    dbc.Row([
        dbc.Col([
            dbc.CardImg(src ="assets/logo_branco.png",
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
            dbc.CardImg(src ="assets/logoufpb.png",
                        className = 'align-self-right',
                        style = {'height':'64px',
                                'width':'45px',
                                })
                ], width=4),
        ], style = {'background-color':'#181a25'},
    ), # mb-4 aparentemente serve como um padding bot

    dbc.Row(html.Hr(),style = {'color':'white', 'background-color':'#000138'}),
    html.Div([
        dcc.Interval(id = 'update_value',
                     interval = 500,
                     n_intervals = 0)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H2('Roda Dianteira Esquerda', style = {'color':'white', 'textAlign':'center'}),
                dbc.CardBody(html.Div(id='card_1'))
            ], color='#112c38', style = card_style)
        ], width= 4),
        dbc.Col([
            dbc.Card([
                html.H2('VELOCIDADE', style = {'color':'white', 'textAlign':'center'}),
                dbc.CardBody(html.Div(id='card_2'))
            ], color='#112c38', style = card_style)
        ], width= 4),
        dbc.Col([
            dbc.Card([
                html.H2('Roda Dianteira Direita', style={'color': 'white', 'textAlign': 'center'}),
                dbc.CardBody(html.Div(id='card_3'))
            ], color='#112c38', style=card_style)
        ], width=4),
    ], style = {'background-color':'#000138'}, className="mb-4"),
])

@app.callback(Output('card_1','children'),
                [Input('update_value','n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        arq2 = pd.read_csv('data.csv', names=header_list)
        t1_r1 = arq2['Temperatura1'].tail(1).iloc[0]
        rpm1 = arq2['RPM1'].tail(1).iloc[0]
    if t1_r1 > 60:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA', style = {'color':'white'},
                                value=t1_r1,
                                color='white',
                                backgroundColor="orange"
                                    ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm1,
                                color='white',
                                backgroundColor="#112c38"
                                    )
                                ])
                            ]),
                    ])
            ]),
        ]
 
    if 30 <= t1_r1 <= 60:
        return [
                    html.Div([
                        dbc.Row([
                            dbc.Col([
                                html.H6('{0:,.2f}'.format(t1_r1),
                                        style={'color': 'orange',
                                                'font-weight': 'bold'},
                                        )
                                    ]),
                            dbc.Col([
                                html.H6('{0:,.2f}'.format(t1_r1),
                                        style={'color': 'orange',
                                                'font-weight': 'bold'},
                                        )
                                    ]),
                    ])]),     
        ]
    
    if t1_r1 < 30:
        return [
                    html.Div([
                        dbc.Row([
                            dbc.Col([
                                html.H6('{0:,.2f}'.format(t1_r1),
                                        style={'color': 'green',
                                                'font-weight': 'bold'},
                                        )
                                    ]),
                            dbc.Col([
                                html.H6('{0:,.2f}'.format(t1_r1),
                                        style={'color': 'green',
                                                'font-weight': 'bold'},
                                        )
                                    ]),
                    ])]),
                
        ]

@app.callback(Output('card_2', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        arq2 = pd.read_csv('data.csv', names=header_list)
        velo = arq2['Velocidade'].tail(1).iloc[0]
    if velo > 0:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.Gauge(
                                color={"gradient": True, "ranges": {"green": [0, 40], "yellow": [40, 80], "red": [80, 150]}},
                                showCurrentValue=True,
                                units="KMH",
                                value=velo,
                                label='VELOCIMETRO', style={'color': 'white'},
                                max=150,
                                min=0
                            ),
                            daq.LEDDisplay(
                                value=velo,
                                color='white',
                                backgroundColor="#112c38",
                                style = {'textAlign':'center'}
                            )
                        ])
                    ]),
                ])
            ]),
        ]


@app.callback(Output('card_3', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        arq2 = pd.read_csv('data.csv', names=header_list)
        t2_r2 = arq2['Temperatura2'].tail(1).iloc[0]
        rpm2 = arq2['RPM2'].tail(1).iloc[0]
    if t2_r2 > 60:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.Div([
                            daq.LEDDisplay(
                                label='TEMPERATURA', style={'color': 'white'},
                                value=t2_r2,
                                color='white',
                                backgroundColor="orange"
                            ),
                            html.Br(),
                            daq.LEDDisplay(
                                label='RPM', style={'color': 'white'},
                                value=rpm2,
                                color='white',
                                backgroundColor="#112c38"
                            )
                        ])
                    ]),
                ])
            ]),
        ]

    if 30 <= t2_r2 <= 60:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.H6('{0:,.2f}'.format(t2_r2),
                                style={'color': 'orange',
                                       'font-weight': 'bold'},
                                )
                    ]),
                    dbc.Col([
                        html.H6('{0:,.2f}'.format(t2_r2),
                                style={'color': 'orange',
                                       'font-weight': 'bold'},
                                )
                    ]),
                ])]),
        ]

    if t2_r2 < 30:
        return [
            html.Div([
                dbc.Row([
                    dbc.Col([
                        html.H6('{0:,.2f}'.format(t2_r2),
                                style={'color': 'green',
                                       'font-weight': 'bold'},
                                )
                    ]),
                    dbc.Col([
                        html.H6('{0:,.2f}'.format(t2_r2),
                                style={'color': 'green',
                                       'font-weight': 'bold'},
                                )
                    ]),
                ])]),

        ]
if __name__ == '__main__':
    app.run_server(debug = True, port = 2020)