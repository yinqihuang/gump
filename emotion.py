import pandas as pd

df1 = pd.read_csv('av1o01.csv')
df2 = pd.read_csv('av1o02.csv')
df3 = pd.read_csv('av1o03.csv')
df4 = pd.read_csv('av1o04.csv')
df5 = pd.read_csv('av1o05.csv')
df6 = pd.read_csv('av1o06.csv')
df7 = pd.read_csv('av1o07.csv')
df8 = pd.read_csv('av1o08.csv')
df9 = pd.read_csv('av1o09.csv')

df1.insert(loc=0, column='observer', value='av1o01')
df2.insert(loc=0, column='observer', value='av1o02')
df3.insert(loc=0, column='observer', value='av1o03')
df4.insert(loc=0, column='observer', value='av1o04')
df5.insert(loc=0, column='observer', value='av1o05')
df6.insert(loc=0, column='observer', value='av1o06')
df7.insert(loc=0, column='observer', value='av1o07')
df8.insert(loc=0, column='observer', value='av1o08')
df9.insert(loc=0, column='observer', value='av1o09')


# df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9], axis=1)

dfs = [df1, df2, df3, df4, df5, df6, df7, df8, df9]

for df in dfs:
    if df.equals(df1):
        pass
    else:
        common = pd.merge(df1, df, how='inner', on='start')
        common_start = common['start']
        for index, row in df.iterrows():
            df_start = int(row.loc['start'])
            if df_start in common_start:
                df_sum = df1.insert(column=str(row['index']),value=str(row.iloc[0]))
            else: df_sum = df1.iloc[:,-1].append(row)
            

# df = df1.set_index('start').combine_first(df2.set_index('start')).reset_index()
