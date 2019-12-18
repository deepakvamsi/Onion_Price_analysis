import pandas as pd
import plotly.express as px
import glob

#pandas_bokeh.output_file("Interactive Plot.html")


file=glob.glob("Onion_20*.csv")

for filename in file:
    df = pd.read_csv(filename,usecols=range(0, 8), low_memory=False) 
    dataframe = df.loc[df['District'] == 'Nashik']
    dataframe['Arrival_Date'] = pd.to_datetime(dataframe['Arrival_Date'])
    dframe = dataframe.sort_values(by='Arrival_Date', ascending=True)
    #dframe.to_csv('onion_data.csv')
    #daframe = pd.read_csv('onion_data.csv',usecols=range(0, 9),low_memory=False)
    #line_in = figure(df, values = 'Arrival_Date', title = "Onion Prices Comparsion between years", legend= "top_left", Ylabel= "Maximum")
    fig = px.bar(dframe, x = 'Arrival_Date', y = 'Max', hover_data=['Min', 'Market', 'Commodity', 'Variety'], color='Market', title='Onion quintal(100kgs) Price over time', labels={'Max':'Maximum Price/100Kg'}, width=1400,height=1000)
    fig.show()
