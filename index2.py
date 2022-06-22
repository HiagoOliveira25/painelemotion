import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from datetime import datetime
import pandas as pd
import plotly.graph_objects as go

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                     style={'height': '40px',
                            'padding-top': '5px'},
                     className='tittle_image'),
            html.H6('FÓRMULA E.MOTION',
                    style={'color': 'white'},
                    className='title'),

        ], className='logo_title'),
        html.H6(id='get_date_time',
                style={'color': 'white'},
                className='adjust_date_time'),
    ], className='title_date_time_container'),

    html.Div([
        dcc.Interval(id='update_date_time',
                     interval=500,
                     n_intervals=0)
    ]),

    html.Div([
        dcc.Interval(id='update_value',
                     interval=500,
                     n_intervals=0)
    ]),
    ################3 Até aqui cabeçalho##################3
    html.Div([
        html.Div([
            html.Div([
                html.Div(id='text_row1'),
                # html.Div(id='text_row2')
            ], className='card_column')
        ], className='adjust_card'),
        html.Div([
            html.Div([
                html.Div(id='text_row3'),
                # html.Div(id='text_row4')
            ], className='card_column')
        ], className='adjust_card'),
        html.Div([
            html.Div([
                html.Div(id='text_row5'),
                # html.Div(id='text_row6')
            ], className='card_column')
        ], className='adjust_card'),
        html.Div([
            html.Div([
                html.Div(id='text_row6'),
                # html.Div(id='text_row8')
            ], className='card_column')
        ], className='adjust_card'),
        html.Div([
            html.Div([
                html.Div(id='text_row7'),
                # html.Div(id='text_row8')
            ], className='card_column')
        ], className='adjust_card'),
        html.Div([
            html.Div([
                html.Div(id='text_row8'),
                # html.Div(id='text_row8')
            ], className='card_column')
        ], className='adjust_card'),
    ], className='flexbox_container'),
])


@app.callback(Output('get_date_time', 'children'),
              [Input('update_date_time', 'n_intervals')])
def live_date_time(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        now = datetime.now()
        dt_string = now.strftime("HORA - %Y-%m-%d %H:%M:%S")

    return [
        html.Div(dt_string)
    ]

# A PARTIR DAQUI OS BLOCOS

@app.callback(Output('text_row1', 'children'), #t1
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3',
                       'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
        t1_df = pd.read_csv('bitcoin_data.csv', names=header_list)
        t1_ec = t1_df['Temperatura1'].tail(1).iloc[0]
        t2_ec = t1_df['Temperatura2'].tail(1).iloc[0]
        t1_df['velocidade'] = t1_df['Velocidade'].diff()
        t1_variacao_velocidade = t1_df['velocidade'].tail(1).iloc[0]
        t1_value = t1_df['Velocidade'].tail(1).iloc[0]

    if t1_ec > 60:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('Temperatura r1 e r2 > 60',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(t1_ec),
                                style={'color': 'red',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(t2_ec),
                                style={'color': 'red',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

    if 30 <= t1_ec <= 60:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('Temperatura r1 e r2 > 30 < 60',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(t1_ec),
                                style={'color': '#FF9900',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(t2_ec),
                                style={'color': '#FF9900',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

    elif t1_ec < 30:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('Temperatura r1 e r2 < 30',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(t1_ec),
                                style={'color': 'red',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(t2_ec),
                                style={'color': 'red',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

@app.callback(Output('text_row3', 'children'), #ec
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3',
                       'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
        b_df = pd.read_csv('bitcoin_data.csv', names=header_list)
        b_ec = b_df['Estado de Carga'].tail(1).iloc[0]
        b_df['velocidade'] = b_df['Velocidade'].diff()
        b_variacao_velocidade = b_df['velocidade'].tail(1).iloc[0]
        b_value = b_df['Velocidade'].tail(1).iloc[0]

    if b_ec > 60:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('Estado de Carga > 0',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f} %'.format(b_ec),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.Div([
                            html.I(className='fas fa-arrow-up',
                                   style={
                                       'color': '#00cc00',
                                       'font-size': '120%'
                                   }),
                        ], className='price_indicator'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

    if 30 <= b_ec <= 60:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('Estado de Carga > 30 < 60',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f} %'.format(b_ec),
                                style={'color': '#FF9900',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

    elif b_ec < 30:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('Estado de Carga < 0',
                               style={'color': 'red',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f} %'.format(b_ec),
                                style={'color': '#FF0000',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

@app.callback(Output('text_row5', 'children'), #t1
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3',
                       'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
        t1_df = pd.read_csv('bitcoin_data.csv', names=header_list)
        t3_ec = t1_df['Temperatura3'].tail(1).iloc[0]
        t4_ec = t1_df['Temperatura4'].tail(1).iloc[0]
        t1_df['velocidade'] = t1_df['Velocidade'].diff()
        t1_variacao_velocidade = t1_df['velocidade'].tail(1).iloc[0]
        t1_value = t1_df['Velocidade'].tail(1).iloc[0]

    if t3_ec > 60:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('Temperatura r3 e r4 > 0',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(t3_ec),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(t4_ec),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

    if 30 <= t3_ec <= 60:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('Temperatura r3 e r4 > 30 < 60',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(t3_ec),
                                style={'color': '#FF9900',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(t4_ec),
                                style={'color': '#FF9900',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

    elif t3_ec < 30:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('Temperatura r3 e r4 < 30',
                               style={'color': 'red',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(t3_ec),
                                style={'color': '#FF0000',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(t4_ec),
                                style={'color': '#FF0000',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

@app.callback(Output('text_row6', 'children'), #t1
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3',
                       'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
        t1_df = pd.read_csv('bitcoin_data.csv', names=header_list)
        rpm1_ec = t1_df['RPM1'].tail(1).iloc[0]
        rpm2_ec = t1_df['RPM2'].tail(1).iloc[0]
        t1_df['velocidade'] = t1_df['Velocidade'].diff()
        t1_variacao_velocidade = t1_df['velocidade'].tail(1).iloc[0]
        t1_value = t1_df['Velocidade'].tail(1).iloc[0]

    if rpm1_ec > 60:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('RPM 1 e 2 > 60',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(rpm1_ec),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(rpm2_ec),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

    if 30 <= rpm1_ec <= 60:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('RPM 1 e 2 > 30 < 60',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(rpm1_ec),
                                style={'color': '#FF9900',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(rpm2_ec),
                                style={'color': '#FF9900',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

    elif rpm1_ec < 30:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('RPM 1 e 2 < 30',
                               style={'color': 'red',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(rpm1_ec),
                                style={'color': '#FF0000',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(rpm2_ec),
                                style={'color': '#FF0000',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

@app.callback(Output('text_row7', 'children'), #veloc
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3',
                       'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
        a_df = pd.read_csv('bitcoin_data.csv', names=header_list)
        a_ec = a_df['Estado de Carga'].tail(1).iloc[0]
        a_df['velocidade'] = a_df['Velocidade'].diff()
        a_variacao_velocidade = a_df['velocidade'].tail(1).iloc[0]
        a_value = a_df['Velocidade'].tail(1).iloc[0]

    if a_variacao_velocidade > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('VELOCIDADE > 0',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                    html.P('Estado carga: ' + '{0:,.2f}'.format(a_ec),
                           style={'color': 'white',
                                  'fontSize': 14},
                           className='rank')
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(a_value),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.Div([
                            html.I(className='fas fa-arrow-up',
                                   style={
                                       'color': '#00cc00',
                                       'font-size': '120%'
                                   }),
                        ], className='price_indicator'),
                    ], className='adjust_price_and_coin'),
                    html.H6('Km/h',
                            style={'color': '#e6e6e6e6',
                                   'fontSize': 14},
                            className='unidade_velocidade')
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

    if a_variacao_velocidade < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px',
                                        'padding-right': '10px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('VELOCIDADE < 0',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                    html.P('Rank: ' + '{0:,.0f}'.format(a_ec),
                           style={'color': 'white',
                                  'fontSize': 14},
                           className='rank')
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(a_value),
                                style={'color': '#EC1E3D',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.Div([
                            html.I(className='fas fa-arrow-down',
                                   style={
                                       'color': '#EC1E3D',
                                       'font-size': '120%'
                                   }),
                        ], className='price_indicator'),
                    ], className='adjust_price_and_coin'),
                    html.H6('Km/h',
                            style={'color': '#e6e6e6e6',
                                   'fontSize': 14},
                            className='unidade_velocidade')
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

    elif a_variacao_velocidade == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('VELOCIDADE = 0',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                    html.P('Estado de Carga: ' + '{0:,.0f}'.format(a_ec),
                           style={'color': 'white',
                                  'fontSize': 14},
                           className='rank')
                ], className='coin_rank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(a_value),
                            style={'color': 'white',
                                   'font-weight': 'bold'},
                            className='coin_price'),
                    html.H6('Km/h',
                            style={'color': '#e6e6e6e6',
                                   'fontSize': 14},
                            className='unidade_velocidade')
                ], className='adjust_price_and_right_value')
            ], className='coin_price_column'),

        ]

@app.callback(Output('text_row8', 'children'), #t1
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3',
                       'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
        t1_df = pd.read_csv('bitcoin_data.csv', names=header_list)
        rpm3_ec = t1_df['RPM3'].tail(1).iloc[0]
        rpm4_ec = t1_df['RPM4'].tail(1).iloc[0]
        t1_df['velocidade'] = t1_df['Velocidade'].diff()
        t1_variacao_velocidade = t1_df['velocidade'].tail(1).iloc[0]
        t1_value = t1_df['Velocidade'].tail(1).iloc[0]

    if rpm3_ec > 60:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('RPM 3 e 4 > 60',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(rpm3_ec),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(rpm4_ec),
                                style={'color': '#00cc00',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

    if 30 <= rpm3_ec <= 60:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('RPM 3 e 4 > 60 > 30 < 60',
                               style={'color': 'white',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(rpm3_ec),
                                style={'color': '#FF9900',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(rpm4_ec),
                                style={'color': '#FF9900',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

    elif rpm3_ec < 30:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src=app.get_asset_url('logo_branco_edit.png'),
                                 style={'height': '30px'},
                                 className='logo_canto_superior_esquerdo'),
                        html.P('RPM 3 e 4 < 30',
                               style={'color': 'red',
                                      'fontSize': 17},
                               className='coin_name')
                    ], className='coin_image'),
                ], className='coin_rank'),
                html.Div([
                    html.Div([
                        html.H6('{0:,.2f}'.format(rpm3_ec),
                                style={'color': '#FF0000',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                        html.H6('{0:,.2f}'.format(rpm4_ec),
                                style={'color': '#FF0000',
                                       'font-weight': 'bold'},
                                className='coin_price'),
                    ], className='adjust_price_and_coin'),
                ], className='adjust_price_indicator_and_right_value')
            ], className='coin_price_column'),

        ]

if __name__ == "__main__":
    # app.run_server(debug = True, port = 4040)
    app.run_server(host='0.0.0.0', debug=True)
