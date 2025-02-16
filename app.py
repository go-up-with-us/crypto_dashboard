from flask import Flask, render_template
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import os

# Create Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get PORT from environment variable
    app.run(host="0.0.0.0", port=port, debug=True)  # Bind to 0.0.0.0 for Render
