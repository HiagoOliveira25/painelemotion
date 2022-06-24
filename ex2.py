import dash
from dash import html, dcc
import dash_daq as daq
from dash.dependencies import Input, Output
import pandas as pd
from dash.exceptions import PreventUpdate
import dash_bootstrap_components as dbc

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

header_list = ['Time', 'Estado de Carga', 'Velocidade', 'Temperatura1', 'Temperatura2', 'Temperatura3', 'Temperatura4', 'RPM1', 'RPM2', 'RPM3', 'RPM4', 'TEMPERATURA MOTOR']
arq = pd.read_csv('data.csv', names=header_list)

# *************************************************************************
app.layout = html.Div(
    [
        html.Div(
            [
                html.Div([
                    dcc.Interval(id = 'update_value',
                        interval = 500,
                        n_intervals = 0)
                ]),
            ],
            className="row",
        ),
        html.Div(
            [
                html.Div(
                    daq.LEDDisplay(
                        id="my-leddisplay",
                        label = 'DISPLAY',
                        value="40",
                        color='white',
                        backgroundColor="black"
                    ),
                ),
            ],
            className="row",
        ),

        dbc.Row([
            dbc.Col([
                html.Div(
                    daq.LEDDisplay(
                        id="my-leddisplay",
                        label = 'DISPLAY',
                        value="40",
                        color='white',
                        backgroundColor="black"
                    )
                ),
            ])
        ])
    ]
)


# *************************************************************************
# must have Dash 1.16.0 or higher for this to work
@app.callback(
    Output("my-leddisplay", "value"),
    Input('update_value', 'n_intervals')
)
def update(n_intervals):
    if n_intervals == 0:
        raise PreventUpdate
    arq2 = pd.read_csv('data.csv', names=header_list)
    t1_r1 = arq2['Temperatura1'].tail(1).iloc[0]
    if t1_r1 > 60:
        return t1_r1

if __name__ == "__main__":
    app.run_server(port=3040, debug=True)