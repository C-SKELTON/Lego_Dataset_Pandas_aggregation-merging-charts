import pandas as pd
themes = pd.read_csv("/content/data/themes.csv")
print(themes.head(5))

#how many ids correspond with to the 'Star Wars' name
themes[themes.name =='Star Wars'].count()['id']

themes[themes.id==158]
