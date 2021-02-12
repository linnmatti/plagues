import pandas as pd
dir = 'C:/Users/linn_/LocustProj/Scripts/'
indir = 'C:/Users/linn_/Dropbox/Locusts/Data/Raw Locusts/Cleaned/'
outdir = 'C:/Users/linn_/Dropbox/Locusts/Data/modified/locustYYYY/'
## Practise:
#df = pd.read_table(dir + 'training.txt', header = 0, delimiter=' ')
#print(df.head())
#print(list(df.columns))

#df90 = df.loc[df['year'].between(1990,1999)]
#print(df90)
#df90.to_csv(dir + 'Nineties.csv', header=True, index=False)
#for i in range(1986,2001):
#    df2 = df.loc[df['year'].between(i - 2,i)]
#    print(df2['year'].unique())
#    df2.to_csv(dir + str(i) + '.csv', header=True, index=False)

#print('done')


# Separate by year
df = pd.read_csv(indir + 'all_locusts.csv', header = 0)
print(df.head())
for i in range (1986, 2019):
    df2 = df.loc[df['startyear'].between(i - 2,i)]
    print(df2['year'].unique())
    #df2.to_csv(dir + str(i) + '.csv', header=True, index=False)

print('done')