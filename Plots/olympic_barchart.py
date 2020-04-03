import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')

# Removing empty spaces from State column to avoid errors
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by State Column
new_df = df.groupby(['NOC'])['Gold'].sum().reset_index()

# Sorting values and select first 20 states
new_df = new_df.sort_values(by=['Gold'], ascending=[False]).head(20)

# Preparing data
data = [go.Bar(x=new_df['NOC'], y=new_df['Gold'])]

# Preparing layout
layout = go.Layout(title='Total Gold Medals by Country in 2016 Olympics', xaxis_title="States",
                   yaxis_title="Gold Medals")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='barchart.html')
