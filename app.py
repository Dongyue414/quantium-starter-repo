from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_table('new_data.csv',sep=',')
df = df.sort_values(by='date')

fig = px.line(df, x='date', y="sales",  title="Pink Morsel Sales")

app.layout = html.Div(children=[
    html.H1(children='data visiualization for Sales vs. Date'),

    dcc.RadioItems(
                ['north', 'east', 'south', 'west', 'all'],
                'all',
                id='region',
                inline=True
            ),

    dcc.Graph(
        id='graph',
        figure=fig
    )
])

@app.callback(
    Output('graph', 'figure'),
    Input('region', 'value'))

def update_graph(region):
    if region != 'all':
        dff = df[df['region'] == region]
    else:
        dff = df
    fig = px.line(dff, x='date', y="sales",  title="Pink Morsel Sales")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
