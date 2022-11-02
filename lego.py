import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
#  2
df_s=pd.read_csv('sets.csv')
df_c=pd.read_csv('colors.csv')
print(df_s.head(10),'\n',df_c.head(10))
print('number of colors:',len(pd.unique(df_c['rgb'])))


'''#unique_colors_plt=sns.barplot(x=pd.unique(df_c['rgb']),y=     (df_c['name'].isnull()==False)

#yc=df_c.groupby('rgb')['name'].aggregate(len)
#xc=pd.unique(df_c['rgb'])

#df_cc=pd.DataFrame(xc,yc).copy()'''


uniquecollors=sns.barplot(x=pd.unique(df_c['rgb']),y=df_c.groupby('rgb')['name'].aggregate(len),data=df_c,palette='rocket',ci="sd").set_title('unique colors')
#  set labels
plt.show()
transdistribution=sns.barplot(x=pd.unique(df_c['is_trans']),y=df_c.groupby('is_trans')['name'].aggregate(len),data=df_c).set_title('trans distribution')
#  set labels  set_ylabel
plt.show()
#df_c.groupby('is_trans')['id'].aggregate(len)
#print(df_s.groupby(['name','year'])['num_parts'].aggregate(lambda x :sum(x)/len(x)))
#sns.lineplot(x=df_s.groupby('theme_id')['num_parts'].aggregate(lambda x: x.sum()),data=df_s,y=df_s['year'],hue=pd.unique(df_s['theme_id']))
plt.show()


a4_dims = (11.7, 8.27)
fig, ax = plt.subplots(figsize=a4_dims)

df_sh=df_s.groupby(['theme_id','year'])['num_parts'].aggregate(sum)
print('average num_parts by year : \n',df_s.groupby(['theme_id','year'])['num_parts'].aggregate(lambda x:x.sum()/len(x)),'\n','num_parts by year :\n ',df_s.groupby(['theme_id','year'])['num_parts'].aggregate(sum))
print('number of themes by year:\n',df_s.groupby(['year'])['theme_id'].count())
sns.scatterplot(data=df_sh,x='year',y='theme_id',hue=df_sh[:],ax=ax)
#plt.show()
#sns.lineplot(data=df_sh,x='theme_id',y=df_sh[:],hue='year',ax=ax)
plt.show()
