from authors_analysis import *

path_csv = "csv/covid_plus_2015_2020.csv"
path_json = "network_data_codiv/papers_covid.json"
create_id_papers_bool(path_json, path_csv, name='id_paper_covid_bool')

"""
create struct-authors (ALL)
"""

path = 'network_data_codiv/authors/'

list_of_json = os.listdir(path)

# authors_collaborators, authors_info = collaborations_and_info_extraction({}, {}, path, list_of_json)

# save_struct_authors(authors_collaborators, authors_info, 'authors_collaborators', 'authors_info')

authors_collaborators, authors_info = load_struct_authors('authors_collaborators', 'authors_info')

"""
create struct-authors (Yes covid)
"""
id_papers_yes_no = spark.read.option("header", True).csv('csv/id_paper_covid_bool.csv')

id_papers_yes_no = id_papers_yes_no.where("covid = 1")

ids_paper = [int(row.id_paper) for row in id_papers_yes_no.select('id_paper').collect()]

# authors_collaborators, authors_info=collaborations_and_info_extraction({},{}, path, list_of_json, ids_paper)

# save_struct_authors(authors_collaborators, authors_info, 'authors_collaborators', 'authors_info')

#authors_collaborators, authors_info = load_struct_authors('authors_collaborators_covid_yes', 'authors_info_covid_yes')


"""
create struct-authors (No covid)
"""
id_papers_yes_no = spark.read.option("header", True).csv('csv/id_paper_covid_bool.csv')

id_papers_yes_no = id_papers_yes_no.where("covid = 0")

ids_paper = [int(row.id_paper) for row in id_papers_yes_no.select('id_paper').collect()]

# authors_collaborators, authors_info=collaborations_and_info_extraction({},{}, path, list_of_json, ids_paper)

# save_struct_authors(authors_collaborators, authors_info, 'authors_collaborators', 'authors_info')

#authors_collaborators, authors_info = load_struct_authors('authors_collaborators_covid_no', 'authors_info_covid_no')


"""
create data
"""
list_couple_years =[(2015, 2016),
                   (2016, 2017),
                   (2017, 2018),
                   (2018, 2019),
                   (2019, 2020)]

data = create_data_authors_info(authors_collaborators, authors_info, list_couple_years)