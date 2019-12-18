import pandas as pd
import plotly.express as px
import glob
import imgkit as img
import os

file=glob.glob("Onion_20*.csv")

for filename in file:
    df = pd.read_csv(filename,usecols=range(0, 8), low_memory=False) 
    dataframe = df.loc[df['District'] == 'Kurnool']
    dataframe['Arrival_Date'] = pd.to_datetime(dataframe['Arrival_Date'])
    dframe = dataframe.sort_values(by='Arrival_Date', ascending=True)
    fig = px.bar(dframe, x = 'Arrival_Date', y = 'Max', hover_data=['Min', 'Market', 'Commodity', 'Variety'], color='Market', title='Onion quintal(100kgs) Price over time', labels={'Max':'Maximum Price/100Kg'}, width=1800,height=400)
    file_name = os.path.splitext(filename)[0] 
    html = "figure_%s"%file_name + ".html"
    file_image = file_name + ".jpeg"
    fig.write_html(html, auto_open=False)
    img.from_file(html, file_image )
