from flask import Flask, render_template
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

# Create Flask app
app = Flask(__name__)

# Create Dash app
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')

# Example Plotly chart (you can replace this with the charts you have)
fig = go.Figure(data=[go.Candlestick(
    x=[1, 2, 3, 4],
    open=[1, 2, 3, 4],
    high=[2, 3, 4, 5],
    low=[0, 1, 2, 3],
    close=[1, 2, 3, 4],
)])

# Dash layout (dashboard content)
dash_app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.H1("Cryptocurrency Dashboard", className="text-center"))
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig))
    ]),
])

# Flask route to serve the dashboard page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
