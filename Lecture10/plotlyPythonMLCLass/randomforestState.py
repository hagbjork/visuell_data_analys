import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from plot_utils import *

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph"),
    html.P("Max depth:"),
    dcc.Slider(
        id='max-depth',
        min=1   , max=15, step=1, value=50,
        marks={i: str(i) for i in range(2,15,1)})
,html.P("Number of estimators:"),
    dcc.Slider(
        id='n_estimators',
        min=10   , max=100, step=10, value=50,
        marks={i: str(i) for i in range(10,101,10)})])

@app.callback(
    Output("graph", "figure"),
    [Input("max-depth", "value")], 
    [State("n_estimators", "value")])
def train_and_display_model(k, n):
    # Load and split data
    X, y = make_moons(noise=0.3, random_state=0)
    xrange, yrange = build_range(X, y)
    xx, yy = np.meshgrid(xrange, yrange)
    test_input = np.c_[xx.ravel(), yy.ravel()]

    # Create classifier, run predictions on grid
    clf = RandomForestClassifier(max_depth=k, n_estimators=n, max_features=1)
    clf.fit(X, y)
    Z = clf.predict_proba(test_input)[:, 1]
    Z = Z.reshape(xx.shape)
    fig = build_figure(X, y, Z, xrange, yrange)

    return fig



app.run_server(debug=True)