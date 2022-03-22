import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from django.forms import formset_factory
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn import linear_model, tree, neighbors
from sklearn.ensemble import RandomForestRegressor

df = px.data.tips()
list_of_options = df['column_name'].sort_values().unique().to_list()
dropdown = [{'label': x,  'value': x} for x in list_of_options ]
X = df.total_bill.values[:, None]
X_train, X_test, y_train, y_test = train_test_split(
    X, df.tip, random_state=42)

models = {'Regression': linear_model.LinearRegression,
          'Decision Tree': tree.DecisionTreeRegressor,
          'k-NN': neighbors.KNeighborsRegressor,
          'Random Forest': RandomForestRegressor}


app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Select Model:"),
    dcc.Dropdown(
        id='model-name',
        options=[{'label': x, 'value': x} 
                 for x in models],
        value='Regression',
        clearable=False
    ),
    # html.P("Select Dataset:"),
    # dcc.Dropdown(
    #     id='dataset-name',
    #     options=[{'label': x, 'value': x} 
    #              for x in datasets],
    #     value='Regression',
    #     clearable=False
    # ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input('model-name', "value")])
def train_and_display(name):
    model = models[name]()
    model.fit(X_train, y_train)

    x_range = np.linspace(X.min(), X.max(), 100)
    y_range = model.predict(x_range.reshape(-1, 1))

    # fig = go.Figure([
    #     go.Scatter(x=X_train.squeeze(), y=y_train, 
    #                name='train', mode='markers'),
    #     go.Scatter(x=X_test.squeeze(), y=y_test, 
    #                name='test', mode='markers'),
    #     go.Scatter(x=x_range, y=y_range, 
    #                name='prediction')
    #    ])
    fig = go.Figure()

    fig.add_traces(go.Scatter(x=X_train.squeeze(), y=y_train, 
                   name='train', mode='markers'))
    fig.add_traces(go.Scatter(x=X_test.squeeze(), y=y_test, 
                   name='test', mode='markers'))
    # fig.add_traces(go.Scatter(x=x_range, y=y_range, 
    #                name='prediction'))

    return fig

app.run_server(debug=True)