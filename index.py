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

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src = app.get_asset_url('financial-profit.png'),
                     style = {'height': '30px'},
                     className = 'title_image'),
            html.H6('DH SENSOR REAL TIME DATA',
                    style = {'color': 'white'},
                    className = 'title'),

        ], className = 'logo_title'),
        html.H6(id = 'get_date_time',
                style = {'color': 'white'},
                className = 'adjust_date_time'),
    ], className = 'title_date_time_container'),

    html.Div([
        dcc.Interval(id = 'update_date_time',
                     interval = 500,
                     n_intervals = 0)
    ]),

    html.Div([
        dcc.Interval(id = 'update_value',
                     interval = 500,
                     n_intervals = 0)
    ]),

    html.Div([
        html.Div([
            html.Div([
                html.Div(id = 'text_row1'),
                html.Div(id = 'text_row2')
            ], className = 'card_column')
        ], className = 'adjust_card'),
        html.Div([
            html.Div([
                html.Div(id = 'text_row3'),
                html.Div(id = 'text_row4')
            ], className = 'card_column')
        ], className = 'adjust_card'),
        html.Div([
            html.Div([
                html.Div(id = 'text_row5'),
                html.Div(id = 'text_row6')
            ], className = 'card_column')
        ], className = 'adjust_card'),
        html.Div([
            html.Div([
                html.Div(id = 'text_row7'),
                html.Div(id = 'text_row8')
            ], className = 'card_column')
        ], className = 'adjust_card')
    ], className = 'flexbox_container'),

    html.Div([
        html.Div(id = 'table_data',
                 className = 'table_width'),
        html.Div([
            dcc.Graph(id = 'bitcoin_chart',
                      animate = True,
                      config = {'displayModeBar': False, 'responsive': True},
                      className = 'chart_width'),
            html.Div(id = 'text_on_chart')
        ], className = 'over_ride_text_on_chart')
    ], className = 'table_chart_container'),

])

@app.callback(Output('get_date_time', 'children'),
              [Input('update_date_time', 'n_intervals')])
def live_date_time(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

    return [
        html.Div(dt_string)
    ]

@app.callback(Output('text_row1', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        bitcoin_df = pd.read_csv('data.csv', names = header_list)
        bitcoin_rank = bitcoin_df['Rank'][0]
        bitcoin_df['price_difference'] = bitcoin_df['Price'].diff()
        bitcoin_price_difference = bitcoin_df['price_difference'].tail(1).iloc[0]
        bitcoin_price = bitcoin_df['Price'].tail(1).iloc[0]

    if bitcoin_price_difference > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src = app.get_asset_url('bitcoin.png'),
                                 style = {'height': '30px'},
                                 className = 'coin'),
                        html.P('Bitcoin',
                               style = {'color': 'white',
                                        'fontSize': 17},
                               className = 'coin_name')
                    ], className = 'coin_image'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bitcoin_rank),
                           style = {'color': 'white',
                                    'fontSize': 14},
                           className = 'rank')
                ], className = 'coin_rank'),
                html.Div([
                    html.Div([
                    html.H6('{0:,.2f}'.format(bitcoin_price),
                            style = {'color': '#00cc00',
                                     'font-weight': 'bold'},
                            className = 'coin_price'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-up',
                           style = {
                               'color': '#00cc00',
                               'font-size': '120%'
                           }),
                        ], className = 'price_indicator'),
                        ], className = 'adjust_price_and_coin'),
                    html.H6('${0:,.0f}'.format(bitcoin_price),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 14},
                            className = 'right_price_value')
                ], className = 'adjust_price_indicator_and_right_value')
            ], className = 'coin_price_column'),

        ]

    if bitcoin_price_difference < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src = app.get_asset_url('bitcoin.png'),
                                 style = {'height': '30px'},
                                 className = 'coin'),
                        html.P('Bitcoin',
                               style = {'color': 'white',
                                        'fontSize': 17},
                               className = 'coin_name')
                    ], className = 'coin_image'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bitcoin_rank),
                           style = {'color': 'white',
                                    'fontSize': 14},
                           className = 'rank')
                ], className = 'coin_rank'),
                html.Div([
                    html.Div([
                    html.H6('{0:,.2f}'.format(bitcoin_price),
                            style = {'color': '#EC1E3D',
                                     'font-weight': 'bold'},
                            className = 'coin_price'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-down',
                           style = {
                               'color': '#EC1E3D',
                               'font-size': '120%'
                           }),
                        ], className = 'price_indicator'),
                        ], className = 'adjust_price_and_coin'),
                    html.H6('${0:,.0f}'.format(bitcoin_price),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 14},
                            className = 'right_price_value')
                ], className = 'adjust_price_indicator_and_right_value')
            ], className = 'coin_price_column'),

        ]

    elif bitcoin_price_difference == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src = app.get_asset_url('bitcoin.png'),
                                 style = {'height': '30px'},
                                 className = 'coin'),
                        html.P('Bitcoin',
                               style = {'color': 'white',
                                        'fontSize': 17},
                               className = 'coin_name')
                    ], className = 'coin_image'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bitcoin_rank),
                           style = {'color': 'white',
                                    'fontSize': 14},
                           className = 'rank')
                ], className = 'coin_rank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(bitcoin_price),
                            style = {'color': 'white',
                                     'font-weight': 'bold'},
                            className = 'coin_price'),
                    html.H6('${0:,.0f}'.format(bitcoin_price),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 14},
                            className = 'right_price_value')
                ], className = 'adjust_price_and_right_value')
            ], className = 'coin_price_column'),

        ]

@app.callback(Output('text_row2', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        bitcoin_df = pd.read_csv('data.csv', names = header_list)
        change_24h = bitcoin_df['Change (24h) %'].tail(1).iloc[0]
        market_cap = bitcoin_df['Market Cap.'].tail(1).iloc[0]

    if change_24h > 0:
        return [
                html.Div([
                    html.Div([
                    html.H6('+{0:,.2f}%'.format(change_24h),
                            style = {'color': '#00cc00',
                                     'font-size': 12,
                                     'font-weight': 'bold'},
                            className = 'price_difference'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-up',
                           style = {
                               'color': '#00cc00',
                               'font-size': '80%'
                           }),
                        ], className = 'difference_indicator'),
                        ], className = 'difference_row'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 12},
                            className = 'cap_price_value')
                ], className = 'diff_cap_row')

        ]

    elif change_24h < 0:
        return [
                html.Div([
                    html.Div([
                    html.H6('{0:,.2f}%'.format(change_24h),
                            style = {'color': '#EC1E3D',
                                     'font-size': 12,
                                     'font-weight': 'bold'},
                            className = 'price_difference'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-down',
                           style = {
                               'color': '#EC1E3D',
                               'font-size': '80%'
                           }),
                        ], className = 'difference_indicator'),
                        ], className = 'difference_row'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 12},
                            className = 'cap_price_value')
                ], className = 'diff_cap_row')

        ]

    elif change_24h == 0:
        return [
                html.Div([
                    html.H6('{0:,.2f}%'.format(change_24h),
                            style = {'color': 'white',
                                     'font-size': 12,
                                     'font-weight': 'bold'},
                            className = 'price_difference'),

                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 12},
                            className = 'cap_price_value')
                ], className = 'zero_diff_row_cap')

        ]

@app.callback(Output('text_row3', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        ethereum_df = pd.read_csv('ethereum_data.csv', names = header_list)
        ethereum_rank = ethereum_df['Rank'][0]
        ethereum_df['price_difference'] = ethereum_df['Price'].diff()
        ethereum_price_difference = ethereum_df['price_difference'].tail(1).iloc[0]
        ethereum_price = ethereum_df['Price'].tail(1).iloc[0]

    if ethereum_price_difference > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src = app.get_asset_url('ethereum.png'),
                                 style = {'height': '30px'},
                                 className = 'coin'),
                        html.P('Ethereum',
                               style = {'color': 'white',
                                        'fontSize': 17},
                               className = 'coin_name')
                    ], className = 'coin_image'),
                    html.P('Rank: ' + '{0:,.0f}'.format(ethereum_rank),
                           style = {'color': 'white',
                                    'fontSize': 14},
                           className = 'rank')
                ], className = 'coin_rank'),
                html.Div([
                    html.Div([
                    html.H6('{0:,.2f}'.format(ethereum_price),
                            style = {'color': '#00cc00',
                                     'font-weight': 'bold'},
                            className = 'coin_price'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-up',
                           style = {
                               'color': '#00cc00',
                               'font-size': '120%'
                           }),
                        ], className = 'price_indicator'),
                        ], className = 'adjust_price_and_coin'),
                    html.H6('${0:,.0f}'.format(ethereum_price),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 14},
                            className = 'right_price_value')
                ], className = 'adjust_price_indicator_and_right_value')
            ], className = 'coin_price_column'),

        ]

    if ethereum_price_difference < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src = app.get_asset_url('ethereum.png'),
                                 style = {'height': '30px'},
                                 className = 'coin'),
                        html.P('Ethereum',
                               style = {'color': 'white',
                                        'fontSize': 17},
                               className = 'coin_name')
                    ], className = 'coin_image'),
                    html.P('Rank: ' + '{0:,.0f}'.format(ethereum_rank),
                           style = {'color': 'white',
                                    'fontSize': 14},
                           className = 'rank')
                ], className = 'coin_rank'),
                html.Div([
                    html.Div([
                    html.H6('{0:,.2f}'.format(ethereum_price),
                            style = {'color': '#EC1E3D',
                                     'font-weight': 'bold'},
                            className = 'coin_price'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-down',
                           style = {
                               'color': '#EC1E3D',
                               'font-size': '120%'
                           }),
                        ], className = 'price_indicator'),
                        ], className = 'adjust_price_and_coin'),
                    html.H6('${0:,.0f}'.format(ethereum_price),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 14},
                            className = 'right_price_value')
                ], className = 'adjust_price_indicator_and_right_value')
            ], className = 'coin_price_column'),

        ]

    elif ethereum_price_difference == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src = app.get_asset_url('ethereum.png'),
                                 style = {'height': '30px'},
                                 className = 'coin'),
                        html.P('Ethereum',
                               style = {'color': 'white',
                                        'fontSize': 17},
                               className = 'coin_name')
                    ], className = 'coin_image'),
                    html.P('Rank: ' + '{0:,.0f}'.format(ethereum_rank),
                           style = {'color': 'white',
                                    'fontSize': 14},
                           className = 'rank')
                ], className = 'coin_rank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(ethereum_price),
                            style = {'color': 'white',
                                     'font-weight': 'bold'},
                            className = 'coin_price'),
                    html.H6('${0:,.0f}'.format(ethereum_price),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 14},
                            className = 'right_price_value')
                ], className = 'adjust_price_and_right_value')
            ], className = 'coin_price_column'),

        ]

@app.callback(Output('text_row4', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        ethereum_df = pd.read_csv('ethereum_data.csv', names = header_list)
        change_24h = ethereum_df['Change (24h) %'].tail(1).iloc[0]
        market_cap = ethereum_df['Market Cap.'].tail(1).iloc[0]

    if change_24h > 0:
        return [
                html.Div([
                    html.Div([
                    html.H6('+{0:,.2f}%'.format(change_24h),
                            style = {'color': '#00cc00',
                                     'font-size': 12,
                                     'font-weight': 'bold'},
                            className = 'price_difference'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-up',
                           style = {
                               'color': '#00cc00',
                               'font-size': '80%'
                           }),
                        ], className = 'difference_indicator'),
                        ], className = 'difference_row'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 12},
                            className = 'cap_price_value')
                ], className = 'diff_cap_row')

        ]

    elif change_24h < 0:
        return [
                html.Div([
                    html.Div([
                    html.H6('{0:,.2f}%'.format(change_24h),
                            style = {'color': '#EC1E3D',
                                     'font-size': 12,
                                     'font-weight': 'bold'},
                            className = 'price_difference'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-down',
                           style = {
                               'color': '#EC1E3D',
                               'font-size': '80%'
                           }),
                        ], className = 'difference_indicator'),
                        ], className = 'difference_row'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 12},
                            className = 'cap_price_value')
                ], className = 'diff_cap_row')

        ]

    elif change_24h == 0:
        return [
                html.Div([
                    html.H6('{0:,.2f}%'.format(change_24h),
                            style = {'color': 'white',
                                     'font-size': 12,
                                     'font-weight': 'bold'},
                            className = 'price_difference'),

                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 12},
                            className = 'cap_price_value')
                ], className = 'zero_diff_row_cap')

        ]


@app.callback(Output('text_row5', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        binance_df = pd.read_csv('binance_data.csv', names = header_list)
        binance_rank = binance_df['Rank'][0]
        binance_df['price_difference'] = binance_df['Price'].diff()
        binance_price_difference = binance_df['price_difference'].tail(1).iloc[0]
        binance_price = binance_df['Price'].tail(1).iloc[0]

    if binance_price_difference > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src = app.get_asset_url('binance.png'),
                                 style = {'height': '30px'},
                                 className = 'coin'),
                        html.P('Binance',
                               style = {'color': 'white',
                                        'fontSize': 17},
                               className = 'coin_name')
                    ], className = 'coin_image'),
                    html.P('Rank: ' + '{0:,.0f}'.format(binance_rank),
                           style = {'color': 'white',
                                    'fontSize': 14},
                           className = 'rank')
                ], className = 'coin_rank'),
                html.Div([
                    html.Div([
                    html.H6('{0:,.2f}'.format(binance_price),
                            style = {'color': '#00cc00',
                                     'font-weight': 'bold'},
                            className = 'coin_price'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-up',
                           style = {
                               'color': '#00cc00',
                               'font-size': '120%'
                           }),
                        ], className = 'price_indicator'),
                        ], className = 'adjust_price_and_coin'),
                    html.H6('${0:,.0f}'.format(binance_price),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 14},
                            className = 'right_price_value')
                ], className = 'adjust_price_indicator_and_right_value')
            ], className = 'coin_price_column'),

        ]

    if binance_price_difference < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src = app.get_asset_url('binance.png'),
                                 style = {'height': '30px'},
                                 className = 'coin'),
                        html.P('Binance',
                               style = {'color': 'white',
                                        'fontSize': 17},
                               className = 'coin_name')
                    ], className = 'coin_image'),
                    html.P('Rank: ' + '{0:,.0f}'.format(binance_rank),
                           style = {'color': 'white',
                                    'fontSize': 14},
                           className = 'rank')
                ], className = 'coin_rank'),
                html.Div([
                    html.Div([
                    html.H6('{0:,.2f}'.format(binance_price),
                            style = {'color': '#EC1E3D',
                                     'font-weight': 'bold'},
                            className = 'coin_price'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-down',
                           style = {
                               'color': '#EC1E3D',
                               'font-size': '120%'
                           }),
                        ], className = 'price_indicator'),
                        ], className = 'adjust_price_and_coin'),
                    html.H6('${0:,.0f}'.format(binance_price),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 14},
                            className = 'right_price_value')
                ], className = 'adjust_price_indicator_and_right_value')
            ], className = 'coin_price_column'),

        ]

    elif binance_price_difference == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src = app.get_asset_url('binance.png'),
                                 style = {'height': '30px'},
                                 className = 'coin'),
                        html.P('Binance',
                               style = {'color': 'white',
                                        'fontSize': 17},
                               className = 'coin_name')
                    ], className = 'coin_image'),
                    html.P('Rank: ' + '{0:,.0f}'.format(binance_rank),
                           style = {'color': 'white',
                                    'fontSize': 14},
                           className = 'rank')
                ], className = 'coin_rank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(binance_price),
                            style = {'color': 'white',
                                     'font-weight': 'bold'},
                            className = 'coin_price'),
                    html.H6('${0:,.0f}'.format(binance_price),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 14},
                            className = 'right_price_value')
                ], className = 'adjust_price_and_right_value')
            ], className = 'coin_price_column'),

        ]

@app.callback(Output('text_row6', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        binance_df = pd.read_csv('binance_data.csv', names = header_list)
        change_24h = binance_df['Change (24h) %'].tail(1).iloc[0]
        market_cap = binance_df['Market Cap.'].tail(1).iloc[0]

    if change_24h > 0:
        return [
                html.Div([
                    html.Div([
                    html.H6('+{0:,.2f}%'.format(change_24h),
                            style = {'color': '#00cc00',
                                     'font-size': 12,
                                     'font-weight': 'bold'},
                            className = 'price_difference'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-up',
                           style = {
                               'color': '#00cc00',
                               'font-size': '80%'
                           }),
                        ], className = 'difference_indicator'),
                        ], className = 'difference_row'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 12},
                            className = 'cap_price_value')
                ], className = 'diff_cap_row')

        ]

    elif change_24h < 0:
        return [
                html.Div([
                    html.Div([
                    html.H6('{0:,.2f}%'.format(change_24h),
                            style = {'color': '#EC1E3D',
                                     'font-size': 12,
                                     'font-weight': 'bold'},
                            className = 'price_difference'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-down',
                           style = {
                               'color': '#EC1E3D',
                               'font-size': '80%'
                           }),
                        ], className = 'difference_indicator'),
                        ], className = 'difference_row'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 12},
                            className = 'cap_price_value')
                ], className = 'diff_cap_row')

        ]

    elif change_24h == 0:
        return [
                html.Div([
                    html.H6('{0:,.2f}%'.format(change_24h),
                            style = {'color': 'white',
                                     'font-size': 12,
                                     'font-weight': 'bold'},
                            className = 'price_difference'),

                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 12},
                            className = 'cap_price_value')
                ], className = 'zero_diff_row_cap')

        ]

@app.callback(Output('text_row7', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        bitcoinCash_df = pd.read_csv('bitcoinCash_data.csv', names = header_list)
        bitcoinCash_rank = bitcoinCash_df['Rank'][0]
        bitcoinCash_df['price_difference'] = bitcoinCash_df['Price'].diff()
        bitcoinCash_price_difference = bitcoinCash_df['price_difference'].tail(1).iloc[0]
        bitcoinCash_price = bitcoinCash_df['Price'].tail(1).iloc[0]

    if bitcoinCash_price_difference > 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src = app.get_asset_url('bitcoincash.png'),
                                 style = {'height': '30px'},
                                 className = 'coin'),
                        html.P('Bitcoin Cash',
                               style = {'color': 'white',
                                        'fontSize': 17},
                               className = 'coin_name')
                    ], className = 'coin_image'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bitcoinCash_rank),
                           style = {'color': 'white',
                                    'fontSize': 14},
                           className = 'rank')
                ], className = 'coin_rank'),
                html.Div([
                    html.Div([
                    html.H6('{0:,.2f}'.format(bitcoinCash_price),
                            style = {'color': '#00cc00',
                                     'font-weight': 'bold'},
                            className = 'coin_price'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-up',
                           style = {
                               'color': '#00cc00',
                               'font-size': '120%'
                           }),
                        ], className = 'price_indicator'),
                        ], className = 'adjust_price_and_coin'),
                    html.H6('${0:,.0f}'.format(bitcoinCash_price),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 14},
                            className = 'right_price_value')
                ], className = 'adjust_price_indicator_and_right_value')
            ], className = 'coin_price_column'),

        ]

    if bitcoinCash_price_difference < 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src = app.get_asset_url('bitcoincash.png'),
                                 style = {'height': '30px'},
                                 className = 'coin'),
                        html.P('Bitcoin Cash',
                               style = {'color': 'white',
                                        'fontSize': 17},
                               className = 'coin_name')
                    ], className = 'coin_image'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bitcoinCash_rank),
                           style = {'color': 'white',
                                    'fontSize': 14},
                           className = 'rank')
                ], className = 'coin_rank'),
                html.Div([
                    html.Div([
                    html.H6('{0:,.2f}'.format(bitcoinCash_price),
                            style = {'color': '#EC1E3D',
                                     'font-weight': 'bold'},
                            className = 'coin_price'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-down',
                           style = {
                               'color': '#EC1E3D',
                               'font-size': '120%'
                           }),
                        ], className = 'price_indicator'),
                        ], className = 'adjust_price_and_coin'),
                    html.H6('${0:,.0f}'.format(bitcoinCash_price),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 14},
                            className = 'right_price_value')
                ], className = 'adjust_price_indicator_and_right_value')
            ], className = 'coin_price_column'),

        ]

    elif bitcoinCash_price_difference == 0:
        return [
            html.Div([
                html.Div([
                    html.Div([
                        html.Img(src = app.get_asset_url('bitcoincash.png'),
                                 style = {'height': '30px'},
                                 className = 'coin'),
                        html.P('Bitcoin Cash',
                               style = {'color': 'white',
                                        'fontSize': 17},
                               className = 'coin_name')
                    ], className = 'coin_image'),
                    html.P('Rank: ' + '{0:,.0f}'.format(bitcoinCash_rank),
                           style = {'color': 'white',
                                    'fontSize': 14},
                           className = 'rank')
                ], className = 'coin_rank'),
                html.Div([
                    html.H6('{0:,.2f}'.format(bitcoinCash_price),
                            style = {'color': 'white',
                                     'font-weight': 'bold'},
                            className = 'coin_price'),
                    html.H6('${0:,.0f}'.format(bitcoinCash_price),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 14},
                            className = 'right_price_value')
                ], className = 'adjust_price_and_right_value')
            ], className = 'coin_price_column'),

        ]

@app.callback(Output('text_row8', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        bitcoinCash_df = pd.read_csv('bitcoinCash_data.csv', names = header_list)
        change_24h = bitcoinCash_df['Change (24h) %'].tail(1).iloc[0]
        market_cap = bitcoinCash_df['Market Cap.'].tail(1).iloc[0]

    if change_24h > 0:
        return [
                html.Div([
                    html.Div([
                    html.H6('+{0:,.2f}%'.format(change_24h),
                            style = {'color': '#00cc00',
                                     'font-size': 12,
                                     'font-weight': 'bold'},
                            className = 'price_difference'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-up',
                           style = {
                               'color': '#00cc00',
                               'font-size': '80%'
                           }),
                        ], className = 'difference_indicator'),
                        ], className = 'difference_row'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 12},
                            className = 'cap_price_value')
                ], className = 'diff_cap_row')

        ]

    elif change_24h < 0:
        return [
                html.Div([
                    html.Div([
                    html.H6('{0:,.2f}%'.format(change_24h),
                            style = {'color': '#EC1E3D',
                                     'font-size': 12,
                                     'font-weight': 'bold'},
                            className = 'price_difference'),
                    html.Div([
                    html.I(className = 'fas fa-arrow-down',
                           style = {
                               'color': '#EC1E3D',
                               'font-size': '80%'
                           }),
                        ], className = 'difference_indicator'),
                        ], className = 'difference_row'),
                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 12},
                            className = 'cap_price_value')
                ], className = 'diff_cap_row')

        ]

    elif change_24h == 0:
        return [
                html.Div([
                    html.H6('{0:,.2f}%'.format(change_24h),
                            style = {'color': 'white',
                                     'font-size': 12,
                                     'font-weight': 'bold'},
                            className = 'price_difference'),

                    html.P('Cap:' + '${0:,.0f}'.format(market_cap),
                            style = {'color': '#e6e6e6e6',
                                     'fontSize': 12},
                            className = 'cap_price_value')
                ], className = 'zero_diff_row_cap')

        ]


@app.callback(Output('table_data', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        bitcoin_df = pd.read_csv('data.csv', names = header_list)
        bitcoin_price = bitcoin_df['Price'].tail(1).iloc[0]
        bitcoin_change_24h = bitcoin_df['Change (24h) %'].tail(1).iloc[0]
        bitcoin_market_cap = bitcoin_df['Market Cap.'].tail(1).iloc[0]

        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        ethereum_df = pd.read_csv('ethereum_data.csv', names = header_list)
        ethereum_price = ethereum_df['Price'].tail(1).iloc[0]
        ethereum_change_24h = ethereum_df['Change (24h) %'].tail(1).iloc[0]
        ethereum_market_cap = ethereum_df['Market Cap.'].tail(1).iloc[0]

        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        binance_df = pd.read_csv('binance_data.csv', names = header_list)
        binance_price = binance_df['Price'].tail(1).iloc[0]
        binance_change_24h = binance_df['Change (24h) %'].tail(1).iloc[0]
        binance_market_cap = binance_df['Market Cap.'].tail(1).iloc[0]

        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        bitcoinCash_df = pd.read_csv('bitcoinCash_data.csv', names = header_list)
        bitcoinCash_price = bitcoinCash_df['Price'].tail(1).iloc[0]
        bitcoinCash_change_24h = bitcoinCash_df['Change (24h) %'].tail(1).iloc[0]
        bitcoinCash_market_cap = bitcoinCash_df['Market Cap.'].tail(1).iloc[0]

        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        chainLink_df = pd.read_csv('chainLink_data.csv', names = header_list)
        chainLink_price = chainLink_df['Price'].tail(1).iloc[0]
        chainLink_change_24h = chainLink_df['Change (24h) %'].tail(1).iloc[0]
        chainLink_market_cap = chainLink_df['Market Cap.'].tail(1).iloc[0]

    return [
        html.Table([
           html.Thead([
               html.Tr([
                   html.Th('#', style = {'width': '30px', 'textAlign': 'center'}),
                   html.Th('Crypto Currency', style = {'width': '120px', 'textAlign': 'left'},
                           className = 'crypto_column'),
                   html.Th('Price', style = {'width': '30px', 'textAlign': 'left'}),
                   html.Th('Change 24h', style = {'width': '90px', 'textAlign': 'left'}),
                   html.Th('Market Cap.', style = {'width': '150px', 'textAlign': 'left'})
               ], className = 'header_hover')
           ]),
            html.Tbody([

                html.Tr([
                    html.Td(html.P('1', style = {'textAlign': 'center',
                                                 'color': 'white',
                                                 'fontSize': 12,
                                                 'margin-top': '10px'})),
                    html.Td([html.Div([
                        html.Img(src = app.get_asset_url('bitcoin.png'),
                                 style = {'height': '30px'},
                                 className = 'image'),
                        html.P('Bitcoin', className = 'logo_text')
                    ], className = 'logo_image')
                    ]),
                    html.Td(html.H6('${0:,.2f}'.format(bitcoin_price),
                            style = {'color': 'white',
                                     'fontSize': 12})),
                    html.Td(html.H6('{0:,.2f}%'.format(bitcoin_change_24h),
                                    style = {'color': 'white',
                                             'fontSize': 12})),
                    html.Td(html.H6('${0:,.0f}'.format(bitcoin_market_cap),
                                    style = {'color': 'white',
                                             'fontSize': 12}))
                ], className = 'hover_row'),

                html.Tr([
                    html.Td(html.P('2', style = {'textAlign': 'center',
                                                 'color': 'white',
                                                 'fontSize': 12,
                                                 'margin-top': '10px'})),
                    html.Td([html.Div([
                        html.Img(src = app.get_asset_url('ethereum.png'),
                                 style = {'height': '30px'},
                                 className = 'image'),
                        html.P('Ethereum', className = 'logo_text')
                    ], className = 'logo_image')
                    ]),
                    html.Td(html.H6('${0:,.2f}'.format(ethereum_price),
                                    style = {'color': 'white',
                                             'fontSize': 12})),
                    html.Td(html.H6('{0:,.2f}%'.format(ethereum_change_24h),
                                    style = {'color': 'white',
                                             'fontSize': 12})),
                    html.Td(html.H6('${0:,.0f}'.format(ethereum_market_cap),
                                    style = {'color': 'white',
                                             'fontSize': 12}))
                ], className = 'hover_row'),

                html.Tr([
                    html.Td(html.P('3', style = {'textAlign': 'center',
                                                 'color': 'white',
                                                 'fontSize': 12,
                                                 'margin-top': '10px'})),
                    html.Td([html.Div([
                        html.Img(src = app.get_asset_url('binance.png'),
                                 style = {'height': '30px'},
                                 className = 'image'),
                        html.P('Binance', className = 'logo_text')
                    ], className = 'logo_image')
                    ]),
                    html.Td(html.H6('${0:,.2f}'.format(binance_price),
                                    style = {'color': 'white',
                                             'fontSize': 12})),
                    html.Td(html.H6('{0:,.2f}%'.format(binance_change_24h),
                                    style = {'color': 'white',
                                             'fontSize': 12})),
                    html.Td(html.H6('${0:,.0f}'.format(binance_market_cap),
                                    style = {'color': 'white',
                                             'fontSize': 12}))
                ], className = 'hover_row'),

                html.Tr([
                    html.Td(html.P('4', style = {'textAlign': 'center',
                                                 'color': 'white',
                                                 'fontSize': 12,
                                                 'margin-top': '10px'})),
                    html.Td([html.Div([
                        html.Img(src = app.get_asset_url('bitcoincash.png'),
                                 style = {'height': '30px'},
                                 className = 'image'),
                        html.P('Bitcoin Cash', className = 'logo_text')
                    ], className = 'logo_image')
                    ]),
                    html.Td(html.H6('${0:,.2f}'.format(bitcoinCash_price),
                                    style = {'color': 'white',
                                             'fontSize': 12})),
                    html.Td(html.H6('{0:,.2f}%'.format(bitcoinCash_change_24h),
                                    style = {'color': 'white',
                                             'fontSize': 12})),
                    html.Td(html.H6('${0:,.0f}'.format(bitcoinCash_market_cap),
                                    style = {'color': 'white',
                                             'fontSize': 12}))
                ], className = 'hover_row'),

                html.Tr([
                    html.Td(html.P('5', style = {'textAlign': 'center',
                                                 'color': 'white',
                                                 'fontSize': 12,
                                                 'margin-top': '10px'})),
                    html.Td([html.Div([
                        html.Img(src = app.get_asset_url('chainlink.png'),
                                 style = {'height': '30px'},
                                 className = 'image'),
                        html.P('Chainlink', className = 'logo_text')
                    ], className = 'logo_image')
                    ]),
                    html.Td(html.H6('${0:,.2f}'.format(chainLink_price),
                                    style = {'color': 'white',
                                             'fontSize': 12})),
                    html.Td(html.H6('{0:,.2f}%'.format(chainLink_change_24h),
                                    style = {'color': 'white',
                                             'fontSize': 12})),
                    html.Td(html.H6('${0:,.0f}'.format(chainLink_market_cap),
                                    style = {'color': 'white',
                                             'fontSize': 12}))
                ], className = 'hover_row')
            ])
        ], className = 'table_style')
    ]

@app.callback(Output('bitcoin_chart', 'figure'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        bitcoin_df = pd.read_csv('data.csv', names = header_list)
        time_interval = bitcoin_df['Time'].tail(30)
        bitcoin_price = bitcoin_df['Price'].tail(30)

    return {
        'data': [go.Scatter(
            x = time_interval,
            y = bitcoin_price,
            fill = 'tonexty',
            fillcolor = 'rgba(255, 0, 255, 0.1)',
            line = dict(width = 2, color = '#ff00ff'),
            mode = 'lines',
            hoverinfo = 'text',
            hovertext =
            '<b>Time</b>: ' + time_interval.astype(str) + '<br>' +
            '<b>Bitcoin Price</b>: ' + [f'${x:,.2f}' for x in bitcoin_price] + '<br>'
        )],

        'layout': go.Layout(
            margin = dict(t = 25, r = 10, l = 70),
            hovermode = 'x unified',
            plot_bgcolor = 'rgba(50, 53, 70, 0)',
            paper_bgcolor = 'rgba(50, 53, 70, 0)',
            xaxis = dict(range = [min(time_interval), max(time_interval)],
                         title = '<b>Time</b>',
                         color = 'white',
                         showspikes = True,
                         showline = True,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white'
                         )),
            yaxis = dict(range = [min(bitcoin_price) - 3, max(bitcoin_price) + 5],
                         color = 'white',
                         showspikes = False,
                         showline = True,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white'
                )),

            font = dict(
                family = 'sans-serif',
                size = 12,
                color = 'white'
            )
        )
    }

@app.callback(Output('text_on_chart', 'children'),
              [Input('update_value', 'n_intervals')])
def update_card(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    else:
        header_list = ['Time', 'Rank', 'CryptoCurrncy', 'Price', 'Change (24h) %', 'Market Cap.']
        bitcoin_df = pd.read_csv('data.csv', names = header_list)
        bitcoin_price = bitcoin_df['Price'].tail(1).iloc[0]
        time_value = bitcoin_df['Time'].tail(1).iloc[0]

    return [
        html.Div([
            html.Div([
                html.P('Bitcoin Price - ',
                       style = {'color': 'white',
                                'fontSize': 15,
                                'font-weight': 'bold'},
                       className = 'text_value'),

                html.P('${0:,.2f}'.format(bitcoin_price),
                       style = {'color': '#ff00ff',
                                'font-weight': 'bold',
                                'fontSize': 15},
                       className = 'numeric_value'),
            ], className = 'adjust_text_and_numeric'),

            html.P('(' + time_value + ')',
                   style = {'color': 'white',
                            'fontSize': 14},
                   className = 'time_value'),
        ], className = 'adjust_text_numeric_and_time'),

    ]

if __name__ == "__main__":
    app.run_server(debug = True, port = 4040)