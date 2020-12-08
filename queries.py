import san
import pandas as pd 
all_projects = san.get("projects/all")

all_projects.to_csv('all_projects.csv', header=True, encoding='utf-8')
#print(all_projects.head())
#pd.DataFrame(all_projects['projectBySlug'], index=[0])

