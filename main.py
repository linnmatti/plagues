import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
dir = 'C:/Users/linn_/Dropbox/Locusts/Data/Raw Locusts/Cleaned/'
outdir = 'C:/Users/linn_/Dropbox/Locusts/Data/Python exports/'
df = pd.read_csv(dir + 'all_locusts.csv', index_col=0)
df.rename(columns={'CAT':'Type'}, inplace=True)
df.describe()
d = {'SWARM':'Swarm'}
df = df.replace(d)
print(df.head())
sns.set_theme(style='darkgrid')
sns.set_style({'axes.facecolor':'white'})
sns.histplot(x='startyear', palette='ch: .25', hue='Type', bins=50, binwidth=1, data=df)
plt.xlabel('Year')
plt.ylabel('Count')

plt.savefig(outdir + 'locusthist.png')