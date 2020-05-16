import pandas as pd
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()

links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

def make_dashboard(x, gdp_change, unemployment, title, filename):
    output_file(filename)
    p = figure(title = title, x_axis_label = 'year', y_axis_label = '%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP Change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend= "% Unemployed")
    show(p)

gdp_df = pd.read_csv(links['GDP'])
unemp_df = pd.read_csv(links['unemployment'])

x = gdp_df['date']
gdp_change = gdp_df['change-current']
unemployment = unemp_df['unemployment']
title = "Analysis of US Economic Data"
filename = "index.html"

make_dashboard(x, gdp_change, unemployment, title, filename)
