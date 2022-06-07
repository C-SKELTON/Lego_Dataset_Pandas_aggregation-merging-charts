import pandas as pd
colors = pd.read_csv("/content/data/colors.csv")
print(colors.head(5))
#grouping by translucent
is_transperant=colors.groupby('is_trans').count()
print(is_transperant['id'])
#is translucent color
is_trans_t = colors[colors['is_trans']=='t'].count()['id']
print(is_trans_t)
#is not translucent color
is_trans_f = colors[colors['is_trans']=='f'].count()['id']
print(is_trans_f)
#viewing table unique rows
unique=colors.nunique()
print(unique)