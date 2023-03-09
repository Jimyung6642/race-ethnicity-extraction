import csv
import pandas as pd
import os
from IPython.display import display

# os.getcwd()
os.listdir(os.getcwd())

# open tsv file
# df = pd.read_csv('all_case_report_meta_with_affiliation_v2.tsv', sep='\t')
df = pd.read_csv('race_meta_df_date_v4.tsv', sep='\t')
# print(df)
# print(df.affiliations)

census = pd.read_csv('us census bureau regions and divisions.csv')
# print(census)
region = pd.DataFrame()
region["State"] = pd.concat([census["State"], census["State Code"]], axis=0)
region.loc[len(region.index)] = 'United State'
region.loc[len(region.index)] = 'United States'
# region.loc[len(region.index)] = 'US'
region.loc[len(region.index)] = 'USA'

# display(region["State"])
# del region

# Match US articles
df2 = df.loc[:, ["pmid","affiliations"]]

region.State = "(\W" + region.State + "\W)"
# region.loc[len(region.index)] = "^(\WBrazil\W)"
# region.loc[len(region.index)] = "^(\WItaly\W)"
# region.loc[len(region.index)] = "^(\WIndia\W)"
# region.loc[len(region.index)] = "^(\WChina\W)"

regionList = '|'.join(region.State)

USpmid_1 = df2[df2.affiliations.str.contains(regionList)]

# Exclude
# exclude = '(\WBrazil\W)|(\WItaly\W)|(\WIndia\W)|(\WChina\W)|(\WMexico\W)'
USpmid_2 = USpmid_1[~USpmid_1.affiliations.str.contains(exclude)]

US_race = pd.merge(df, USpmid_2, on = 'pmid')
nonUS_race = df[~df.pmid.isin(US_race.pmid)]
# Save file
US_race.to_csv('US_race.csv', index=False)
nonUS_race.to_csv('nonUS_race.csv', index=False)

