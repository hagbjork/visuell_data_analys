import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LassoCV

N_FOLD = 6

# Load and preprocess the data
df = px.data.gapminder()
X = df.drop(columns=['lifeExp', 'iso_num'])
X = pd.get_dummies(X, columns=['country', 'continent', 'iso_alpha'])
y = df['lifeExp']

# Train model to predict life expectancy
model = LassoCV(cv=N_FOLD, normalize=True)
model.fit(X, y)
mean_alphas = model.mse_path_.mean(axis=-1)

fig = go.Figure([
    go.Scatter(
        x=model.alphas_, y=model.mse_path_[:, i],
        name=f"Fold: {i+1}", opacity=.5, line=dict(dash='dash'),
        hovertemplate="alpha: %{x} <br>MSE: %{y}"
    )
    for i in range(N_FOLD)
])
fig.add_traces(go.Scatter(
    x=model.alphas_, y=mean_alphas,
    name='Mean', line=dict(color='black', width=3),
    hovertemplate="alpha: %{x} <br>MSE: %{y}",
))

fig.add_shape(
    type="line", line=dict(dash='dash'),
    x0=model.alpha_, y0=0,
    x1=model.alpha_, y1=1,
    yref='paper'
)

fig.update_layout(
    xaxis_title='alpha',
    xaxis_type="log",
    yaxis_title="Mean Square Error (MSE)"
)
fig.show()