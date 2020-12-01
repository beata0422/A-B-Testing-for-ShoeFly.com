import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
#How many views (i.e., rows of the table) came from each utm_source?
ad_clicks.groupby('utm_source')\
    .user_id.count()\
    .reset_index()
#Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
#We want to know the percent of people who clicked on ads from each utm_source.
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id').reset_index()
print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)

print(ad_clicks.groupby('experimental_group').user_id.count().reset_index())

print(ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index().pivot(index='experimental_group', columns='is_click', values='user_id').reset_index())

a_clicks = ad_clicks[ad_clicks.experimental_group =='A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks_pivot = a_clicks.groupby(['is_click','day']).user_id.count().reset_index().pivot(index = 'day', columns = 'is_click', values = 'user_id').reset_index()
a_clicks_pivot['percent_clicked'] = a_clicks_pivot[True]/(a_clicks_pivot[True]+a_clicks_pivot[False])
print(a_clicks_pivot)

b_clicks_pivot = b_clicks.groupby(['is_click','day']).user_id.count().reset_index().pivot(index = 'day', columns = 'is_click', values = 'user_id').reset_index()
b_clicks_pivot['percent_clicked'] = b_clicks_pivot[True]/(b_clicks_pivot[True]+b_clicks_pivot[False])
print(b_clicks_pivot)