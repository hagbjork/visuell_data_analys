from dash import Dash, dcc, html, dcc, Input, Output, State
from dash.exceptions import PreventUpdate

options = [
    {"label": "New York City", "value": "NYC"},
    {"label": "Montreal", "value": "MTL"},
    {"label": "San Francisco", "value": "SF"},
]

app = Dash(__name__)
app.layout = html.Div([
    html.Div([
        "Single dynamic Dropdown",
        dcc.Dropdown(id="my-dynamic-dropdown")
    ]),
    html.Div([
        "Multi dynamic Dropdown",
        dcc.Dropdown(id="my-multi-dynamic-dropdown", multi=True),
    ]),
])


@app.callback(
    Output("my-dynamic-dropdown", "options"),
    Input("my-dynamic-dropdown", "search_value")
)
def update_options(search_value):
    if not search_value:
        raise PreventUpdate
    return [o for o in options if search_value in o["label"]]


@app.callback(
    Output("my-multi-dynamic-dropdown", "options"),
    Input("my-multi-dynamic-dropdown", "search_value"),
    State("my-multi-dynamic-dropdown", "value")
)
def update_multi_options(search_value, value):
    if not search_value:
        raise PreventUpdate
    # Make sure that the set values are in the option list, else they will disappear
    # from the shown select list, but still part of the `value`.
    return [
        o for o in options if search_value in o["label"] or o["value"] in (value or [])
    ]


if __name__ == "__main__":
    app.run_server(debug=True)