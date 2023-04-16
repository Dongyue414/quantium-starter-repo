from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_table('new_data.csv',sep=',')
df = df.sort_values(by='date')

fig = px.line(df, x='date', y="sales")

app.layout = html.Div(children=[
    html.H1(children='data visiualization for Sales vs. Date'),


    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
