## GOLD STANDARD
# import data
import pandas as pd

# df = pd.read_csv('/Users/jimmypark/OneDrive - cumc.columbia.edu/Race extraction/US_race.csv')
df = pd.read_csv('your data.csv')
list(df.columns)

# Check race distribution
df['race_type'].value_counts()
df[df['race_type'].apply(lambda x: 'white' in x)].shape # (1492, 18)
df[df['race_type'].apply(lambda x: 'black' in x)].shape # (734, 18)
df[df['race_type'].apply(lambda x: 'latino' in x)].shape # (413, 18)
df[df['race_type'].apply(lambda x: 'asian' in x)].shape # (351, 18)
df[df['race_type'].apply(lambda x: 'islander' in x)].shape # (5, 18)
df[df['race_type'].apply(lambda x: 'ameindian' in x)].shape # (16, 18)

# Check Journal distribution
df['source'].value_counts()
df.source_title.value_counts()

# Group by Year
all_count = 0
print('year\ttotal_count\tno_race_count\trace_count\twhite_count\tblack_count\tasian_count\tlatino_count\tameindian_count\tislander_count')
for year in range(1960,2023):
    total_count = df[(df.pubdate >= f'{year}-01-01') &
                     (df.pubdate <= f'{year}-12-31')
                     ].shape[0]    
    no_race_count = df[(df.pubdate >= f'{year}-01-01') &
                     (df.pubdate <= f'{year}-12-31') &
                     (df.no_race == True)
                     ].shape[0]    
    race_count = df[(df.pubdate >= f'{year}-01-01') &
                     (df.pubdate <= f'{year}-12-31') &
                     (df.no_race == False)
                     ].shape[0]
    white_count = df[(df.pubdate >= f'{year}-01-01') &
                     (df.pubdate <= f'{year}-12-31') &
                     (df.race_type.apply(lambda x: 'white' in x))
                     ].shape[0]    
    black_count = df[(df.pubdate >= f'{year}-01-01') &
                     (df.pubdate <= f'{year}-12-31') &
                     (df.race_type.apply(lambda x: 'black' in x))
                     ].shape[0]    
    asian_count = df[(df.pubdate >= f'{year}-01-01') &
                     (df.pubdate <= f'{year}-12-31') &
                     (df.race_type.apply(lambda x: 'asian' in x))
                     ].shape[0]    
    latino_count = df[(df.pubdate >= f'{year}-01-01') &
                     (df.pubdate <= f'{year}-12-31') &
                     (df.race_type.apply(lambda x: 'latino' in x))
                     ].shape[0]
    ameindian_count = df[(df.pubdate >= f'{year}-01-01') &
                     (df.pubdate <= f'{year}-12-31') &
                     (df.race_type.apply(lambda x: 'ameindian' in x))
                     ].shape[0]
    islander_count = df[(df.pubdate >= f'{year}-01-01') &
                     (df.pubdate <= f'{year}-12-31') &
                     (df.race_type.apply(lambda x: 'islander' in x))
                     ].shape[0]    
    print(f'{year}\t{total_count}\t{no_race_count}\t{white_count}\t{black_count}\t{asian_count}\t{latino_count}\t{ameindian_count}\t{islander_count}')
    all_count += total_count
print(all_count)

df[(df.pubdate <= f'1960-01-01') | (df.pubdate >= f'2022-12-31')] # none

# Group by JOURNALs
df.source.value_counts()[:20]
df.source_title.value_counts()[:20]

# Group by MeSH tags
mesh_freq = pd.Series([x for items in df.mesh_list.dropna() for x in items]).value_counts(dropna=False)
print(mesh_freq[:20])

def get_stats_by_mesh(mesh_tag):    
    all_count = 0
    print('year\ttotal_count\tno_race_count\trace_count\twhite_count\tblack_count\tasian_count\tlatino_count\tameindian_count\tislander_count')
    for year in range(1960,2023):
        year_limit = (df['pubdate'] >= f'{year}-01-01')  & (df['pubdate'] <= f'{year}-12-31')
        journal_limit = (df['mesh_list'].astype(str).str.contains(f'({disease_mesh})', regex=True))
        
        total_count = df[year_limit & journal_limit].shape[0]
        no_race_count = df[year_limit & journal_limit & (df['no_race']==True)].shape[0]
        race_count = df[year_limit & journal_limit & (df['no_race']==False)].shape[0]
        white_count = df[year_limit & journal_limit & (df['race_type'].apply(lambda x: 'white' in x))].shape[0]
        black_count = df[year_limit & journal_limit & (df['race_type'].apply(lambda x: 'black' in x))].shape[0]
        asian_count = df[year_limit & journal_limit & (df['race_type'].apply(lambda x: 'asian' in x))].shape[0]
        latino_count = df[year_limit & journal_limit & (df['race_type'].apply(lambda x: 'latino' in x))].shape[0]
        ameindian_count = df[year_limit & journal_limit & (df['race_type'].apply(lambda x: 'ameindian' in x))].shape[0]
        islander_count = df[year_limit & journal_limit & (df['race_type'].apply(lambda x: 'islander' in x))].shape[0]

        print(f'{year}\t{total_count}\t{no_race_count}\t{race_count}\t{white_count}\t{black_count}\t{asian_count}\t{latino_count}\t{ameindian_count}\t{islander_count}')
        all_count += total_count
    print(all_count)

# Stats by condition
# (D000086382, COVID-19)                                        300
# (D011247, Pregnancy)                                          89
# (D008175, Lung Neoplasms)                                     61
# (D011024, Pneumonia, Viral)                                   3
# (D009364, Neoplasm Recurrence, Local)                         47
# (D000230, Adenocarcinoma)                                     47
# (D008113, Liver Neoplasms)                                    34

disease_mesh = 'D000086382|COVID-19'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D011247|Pregnancy'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D008175|Lung Neoplasms'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D010024|Pneumonia, Viral'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D009364|Neoplasm Recurrence, Local'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D000230|Adenocarcinoma'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D008113|Liver Neoplasms'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

# stats by gender, and age
# (D006801, Humans)                                            2652
# (D008297, Male)                                              1452
# (D005260, Female)                                            1365
# (D000328, Adult)                                             911
# (D002648, Child)                                             308
# (D000293, Adolescent)                                        189

disease_mesh = 'D006801|Humans'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D008297|Male'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)


disease_mesh = 'D005260|Female'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D000328|Adult'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D002648|Child'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D000293|Adolescent'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

# Stats by study types
# Follow-Up Studies [N05.715.360.330.500.750.350]
# Longitudinal Studies [N05.715.360.330.500.750.500] 
# Prospective Studies [N05.715.360.330.500.750.650]
# Retrospective Studies [N05.715.360.330.500.750.825]
# (D005500, Follow-Up Studies)                                  55
# (D012189, Retrospective Studies)                              47
# (D008137, Longitudinal Studies)                               7
# (D011446, Prospective Studies)                                9
disease_mesh = 'D005500|Follow-Up Studies'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D012189|Retrospective Studies'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D008137|Longitudinal Studies'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D011446|Prospective Studies'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

# stats by Geographic Locations [Z01] 

# D002681, China                    3
# D007723, Korea                    4
# D007564, Japan                    3
# D000349, Africa                   29
# D001208, Asia                     12
# D005060, Europe                   1
# D000569, Americas                 0

disease_mesh = 'D002681|China'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D007723|Korea'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D007564|Japan'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D000349|Africa'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D001208|Asia'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D005060|Europe'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

disease_mesh = 'D000569|Americas'
print(f'Results for {disease_mesh}')
get_stats_by_mesh(disease_mesh)
print('='*20)

# Visualization
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def get_stats_by_mesh_single_df(mesh_tag):
    result_list = []
    all_count = 0

    result_list.append('year\ttotal_count\tno_race_count\trace_count\tsingle_race_count\trace_type'.split('\t'))
    print('year\ttotal_count\tno_race_count\trace_count\twhite_count\tblack_count\tasian_count\tlatino_count\tameindian_count\tislander_count')
    
    for year in range(1960,2023):
        year_limit = (df['pubdate'] >= f'{year}-01-01')  & (df['pubdate'] <= f'{year}-12-31')
        journal_limit = (df['mesh_list'].astype(str).str.contains(f'({disease_mesh})', regex=True))
        
        total_count = df[year_limit & journal_limit].shape[0]
        no_race_count = df[year_limit & journal_limit & (df['no_race']==True)].shape[0]
        race_count = df[year_limit & journal_limit & (df['no_race']==False)].shape[0]
        white_count = df[year_limit & journal_limit & (df['race_type'].apply(lambda x: 'white' in x))].shape[0]
        black_count = df[year_limit & journal_limit & (df['race_type'].apply(lambda x: 'black' in x))].shape[0]
        asian_count = df[year_limit & journal_limit & (df['race_type'].apply(lambda x: 'asian' in x))].shape[0]
        latino_count = df[year_limit & journal_limit & (df['race_type'].apply(lambda x: 'latino' in x))].shape[0]
        ameindian_count = df[year_limit & journal_limit & (df['race_type'].apply(lambda x: 'ameindian' in x))].shape[0]
        islander_count = df[year_limit & journal_limit & (df['race_type'].apply(lambda x: 'islander' in x))].shape[0]
        
        print(f'{year}\t{total_count}\t{no_race_count}\t{race_count}\t{white_count}\t{black_count}\t{asian_count}\t{latino_count}\t{ameindian_count}\t{islander_count}')
        result_list.append([year,total_count,no_race_count,race_count,white_count,'white'])
        result_list.append([year,total_count,no_race_count,race_count,black_count,'black'])
        result_list.append([year,total_count,no_race_count,race_count,asian_count,'asian'])
        result_list.append([year,total_count,no_race_count,race_count,latino_count,'latino'])
        result_list.append([year,total_count,no_race_count,race_count,ameindian_count,'ameindia'])
        result_list.append([year,total_count,no_race_count,race_count,islander_count,'islander'])

        all_count += total_count
    print(all_count)
#     print(result_list[:5])
    result_df = pd.DataFrame(result_list[1:], columns=result_list[0])
    result_df['MESH'] = disease_mesh
    return result_df

disease_mesh = 'D006801|Humans'
print(f'Results for {disease_mesh}')
test_df = get_stats_by_mesh_single_df(disease_mesh)
print('='*20)
# test_df.head()

sns.set_style("darkgrid")
sns.set(rc={'figure.figsize':(10,10)})
ax = sns.lineplot(data=test_df, x ='year', y = 'single_race_count',
                  hue='race_type', palette='bright',   # colorblind  deep, muted, pastel, bright, dark, viridis
                  legend='full', lw=3)

ax.xaxis.set_major_locator(ticker.MultipleLocator(4))
plt.legend(bbox_to_anchor=(1, 1), prop={'size':20})
plt.ylabel('Race count')
plt.xlabel('Year')
plt.show()

df_pivot = pd.pivot_table(test_df,
                          values='single_race_count',
                          index='race_type',
                          columns='year')
# df_pivot

plt.figure(figsize = (40,20))
plt.title('Case report count per race')
sns.heatmap(df_pivot, annot=True, cmap='RdYlBu_r', fmt= '.4g',)
plt.xlabel('Year')
plt.ylabel('Race type')
plt.show()

g = sns.relplot(data = test_df, x = "year", y = "single_race_count",
                col = "race_type", hue = "race_type",
                kind = "line", palette = "Spectral",   
                linewidth = 4, zorder = 5,
                col_wrap = 3, height = 3, aspect = 1.5, legend = False
               )
#add text and silhouettes
for time, ax in g.axes_dict.items():
    ax.text(.1, .85, time,
            transform = ax.transAxes, fontweight="bold"
           )
    sns.lineplot(data = test_df, x = "year", y = "single_race_count", units="race_type",
                 estimator = None, color= ".7", linewidth=1, ax=ax
                )
# ax.set_xticks('')
# # get the values we want displayed as tick labels
# tick_labels = tuple(df['Line'])
# # get the positions for the maximum xtick label
# x_max = int(max(plt.xticks()[0]))  # int() to convert numpy.int32 => int
# # manually set you xtick labels
# plt.xticks(range(0, x_max + 1), tick_labels, rotation=45)
g.set_titles("Case report distribution by race")
g.set_axis_labels("year", "Case report count")
g.tight_layout()
