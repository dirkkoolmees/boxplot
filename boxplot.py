import pandas as pd
import plotly.express as px


url = 'https://raw.githubusercontent.com/dirkkoolmees/CO2_emissions_per-region/master/CO2%20Emissions%20per%20region%20-%20Sheet2.csv'
df = pd.read_csv(url)

df = pd.read_csv(url, index_col = 'Year').transpose()

df['Sum'] = df.sum(axis=1)

df = df.sort_values('Sum', ascending = False)

df.drop(['Sum'], axis=1, inplace = True)

df = df.transpose()

fig = px.box(df, y=df.columns, color_discrete_sequence=px.colors.sequential.RdBu, points = False)

fig.update_traces(quartilemethod="inclusive") # or "exclusive", or "linear" by default

fig.update_layout(
    title='CO2 Emissions from fossil fuels and cement production',
    yaxis_title='Thousand metric tons of C',
    xaxis_title=' '
    )
