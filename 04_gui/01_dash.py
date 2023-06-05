import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go

import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State
from dash.exceptions import PreventUpdate

TITLE_STYLE={
    'display': 'flex',
    'flexDirection': 'column',
    'justifyContent': 'center',
    'alignItems': 'center',
    'marginTop': '1rem',
    'marginBottom': '1rem'
}

ROW_BUTTON_STYLE = {
    'display': 'flex',
    'justifyContent': 'space-evenly',
    'alignItems': 'center',
    'marginTop': '1rem',
    'marginBottom': '1rem'
}


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.UNITED])

app.title = 'PCS-Example'

app.layout = html.Div(
    [
        html.Div(
            [
                html.H3('Python per il Calcolo Scientifico - GUI con Dash'),
                html.H4('Pulsanti')
            ],
            style=TITLE_STYLE
        ),
        html.Div(
            [
                html.H5('Pulsante con DCC'),
                dcc.Input(id='submit-input-dcc', type='text'),
                html.Button(
                    'Scrivi qualcosa!',
                    id='submit-button-dcc',
                    n_clicks=0),
                html.H5('Scrivi qualcosa', id='container-button-dcc'),
            ],
            style=ROW_BUTTON_STYLE
        ),
        html.Div(
            [
                html.H5('Pulsante con DBC'),
                dcc.Input(id='submit-input-dbc', type='text'),
                dbc.Button(
                    'Scrivi qualcosa!',
                    id='submit-button-dbc',
                    n_clicks=0),
                html.H5('Scrivi qualcosa', id='container-button-dbc'),
            ],
            style=ROW_BUTTON_STYLE
        ),
        html.Div(
            html.H4('Grafici'),
            style=TITLE_STYLE
        ),
        html.Div(
            [
                html.Div(id='graph'),
                dbc.Button(
                    'Premi per mostrare il grafico!',
                    id='button-graph',
                    n_clicks=0)
            ],
            style={
                'display': 'flex',
                'justifyContent': 'center'
            }
        )
    ]
)


@app.callback(Output('container-button-dcc', 'children'),
              Input('submit-button-dcc', 'n_clicks'),
              State('container-button-dcc', 'children'),
              State('submit-input-dcc', 'value'))
def update_value_dcc(n_clicks, initial_value, value):
    if n_clicks > 0 and value is not None:
        n_clicks = 0
        return f'Hai scritto: {value}'
    else:
        return initial_value


@app.callback(Output('container-button-dbc', 'children'),
              Input('submit-button-dbc', 'n_clicks'),
              State('container-button-dbc', 'children'),
              State('submit-input-dbc', 'value'))
def update_value_dbc(n_clicks, initial_value, value):
    if n_clicks > 0 and value is not None:
        n_clicks = 0
        return f'Hai scritto: {value}'
    else:
        return initial_value


@app.callback(Output('graph', 'children'),
              Output('button-graph', 'style'),
              Input('button-graph', 'n_clicks'))
def linear_analysis(n_clicks):
    if n_clicks > 0:
        # This code is taken directly from the Scikit Learn example.
        X, y = load_diabetes(return_X_y=True)
        X = X[:, np.newaxis, 2]
        X_train = X[:-20]
        X_test = X[-20:]
        y_train = y[:-20]
        y_test = y[-20:]
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        y_pred = lr.predict(X_test)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=X_test.flatten(), y=y_test.flatten(), mode='markers', name='Dati'))
        fig.add_trace(go.Scatter(x=X_test.flatten(), y=y_pred.flatten(), mode='lines', name='Predizioni'))
        return [dcc.Graph(figure=fig), {'display': 'none'}]
    raise PreventUpdate


if __name__ == '__main__':
    app.run_server(debug=True)
