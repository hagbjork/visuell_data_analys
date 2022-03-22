import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from plot_utils import *

app = dash.Dash(__name__)

#Det som behöver läggas till - fler sliders, en dropdown m.m.
app.layout = html.Div([
    dcc.Graph(id="graph"),

    html.P("Gamma:"),
    dcc.Slider(
        id='gamma-slide',
        min=1   , max=15, step=1, value=50,
        marks={i: str(i) for i in range(2,15,1)}),

    html.P("Polynomial degree:"),
    dcc.Slider(
        id='degree-slide',
        min=1   , max=5, step=1, value=3,
        marks={i: str(i) for i in range(1,6,1)}),

    html.P("Regularization (C):"),
    dcc.Slider(
        id='c-slide',
        min=0.1   , max=3, step=0.1, value=50,
        marks={i: str(0.1*i) for i in range(1,30,1)}),

    html.P("Kernel type:"),
    dcc.Dropdown(id = 'Kernel', options = ['rbf', 'poly', 'linear'], value = 'linear')])

        

@app.callback(
    Output("graph", "figure"), 
    inputs = {
        'gamma':Input("gamma-slide", "value"),

        'degree' :Input("degree-slide", "value"),

        'c':Input('c-slide', 'value'),

        'kernel':Input('Kernel', 'value')})
        
def train_and_display_model(gamma, degree, c, kernel):#, gamma,degree, c, kernel):
    print(gamma)
    # Load and split data   
    X, y = make_moons(noise=0.3, random_state=0)
    xrange, yrange = build_range(X, y)
    xx, yy = np.meshgrid(xrange, yrange)
    test_input = np.c_[xx.ravel(), yy.ravel()]


    # Create classifier, run predictions on grid
    #kernel = kernel,degree = degree, gamma=gamma, C = c, 
    clf = SVC(gamma = gamma, degree = degree, C = c, kernel = kernel, probability= True)
    clf.fit(X, y)
    Z = clf.predict_proba(test_input)[:, 1]
    Z = Z.reshape(xx.shape)
    fig = build_figure(X, y, Z, xrange, yrange)

    return fig

app.run_server(debug=True)