from authors_analysis import *

"""
create csv - covid plus
"""
#create_table_papers('network_data_codiv/authors', name=covid_plus_2015_2020)

"""
AUTHORS GRAPH
vertex: author
edge: collaboration with another author, weight: number of collaborations
"""
"""
Create graph:
- df
- year (2015/2020)
- limit (example: first 30000 papers; limit:30000) 
if limit == 0, take all papers
"""

df = spark.read.option("header", True).csv("csv/covid_plus_2015_2020.csv")

list_g = dict()

list_g[2019] = steps(df, 2019, 30000)

"""
Save graph
"""
i=0
save_graph(list_g[2019], "30000_2019")

"""
Load graph
"""
#list_g[2019] = load_graph("30000_2019")

"""
View histograms
"""
#visualize_graphs(list_g)

