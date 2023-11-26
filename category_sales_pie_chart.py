import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the dataset
data = pd.read_excel("C:/Users/Chandru/OneDrive/Desktop/Python Visuals/Sample - Superstore.xls", sheet_name="Orders")

# Create a Dash application
app = dash.Dash(__name__)

# Define the app layout
app.layout = html.Div([
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in data['Order Date'].dt.year.unique()],
        value=data['Order Date'].dt.year.unique()[0],
        multi=False
    ),
    dcc.Graph(id='pie-chart')
])

@app.callback(
    Output('pie-chart', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_graph(selected_year):
    filtered_data = data[data['Order Date'].dt.year == selected_year]
    category_data = filtered_data.groupby('Category')['Sales'].sum().reset_index()
    return px.pie(category_data, names='Category', values='Sales', title=f'Total Sales by Product Category for {selected_year}')

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
