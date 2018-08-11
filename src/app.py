import dash
import dash_core_components as dcc
import dash_html_components as html 
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('../data/returns_all.csv')

available_tickers = df.columns[1:]

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='ticker',
                options=[{'label': i, 'value': i} for i in available_tickers],
                value='label'
            )
        ],
        style={'width': '48%', 'display': 'inline-block'}),
    ]),

    dcc.Graph(id='indicator-graphic', animate=True),

])

@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('ticker', 'value')])
def update_graph(ticker):

    return {
        'data': [go.Scatter(
            x=df['time'],
            y=df[ticker],
            mode='lines+markers',
            name="'spline'",
            line=dict(
                shape='spline'
            )
        )],
        'layout': go.Layout(
            xaxis={
                'title': 'Date',
            },
            yaxis={
                'title': 'Levels',
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
	app.run_server(debug=True)