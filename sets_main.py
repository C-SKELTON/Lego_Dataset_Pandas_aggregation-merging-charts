import pandas as pd
import matplotlib.pyplot as plt
sets = pd.read_csv("/content/data/sets.csv")

print(sets.head(5))

first_year_released = sets.sort_values('year').head(1)['year']
first_year_products =sets[sets['year']==1949].count()['name']
print(first_year_released)
print(first_year_products)

largest_sets = sets.sort_values('num_parts', ascending=False).head(5)[['year', 'name', 'num_parts']]
print(largest_sets)

sets_by_year = sets.groupby('year').nunique()
sets_by_year['set_num'].head(5)
ax1 = plt.gca()
ax2 = ax1.twinx()


#number of unique themes y year
themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns = {'theme_id':'num_themes'}, inplace=True)
print(themes_by_year.head(5))

#2  line graph with 2 axes, commented out for the scatter plot

# ax1.plot(sets_by_year.index[:-2], sets_by_year.set_num[:-2], 'g')
# ax2.plot(themes_by_year.index[:-2], themes_by_year.num_themes[:-2], 'r')

# ax1.set_xlabel('Year')
# ax1.set_ylabel('Number of Sets', color='green')
# ax2.set_ylabel('Number of Themes', color='red')


parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})
print(parts_per_set.tail())

#scatter plot
plt.scatter(parts_per_set.index[:-2], parts_per_set[:-2])

#number of sets per logo theme, returns in descending order
set_theme_count = sets['theme_id'].value_counts()
print(set_theme_count[:10])


#number of sets for theme id 18
sets[sets.theme_id == 18 ].head(5)

set_theme_count = pd.DataFrame({'id':set_theme_count.index,
                               'set_count': set_theme_count.values})
set_theme_count.head(5)

#creating a merged table, inner join set_theme_count variable to themes dataset on id
merged_df = pd.merge(set_theme_count, themes, on='id')
print(merged_df[:15])

#bar chart
plt.figure(figsize=(14,8))
plt.xticks(fontsize=14, rotation = 45)
plt.yticks(fontsize=14)
plt.ylabel('Number of Sets', fontsize=14)
plt.xlabel('Theme Name', fontsize=14)
plt.bar(merged_df.name[:10], merged_df.set_count[:10],color='g')
