import pandas as pd

dfs = []
for i in range(1, 10):
    # print('av1o0{}.csv'.format(i))
    filename = 'av1o0{}.csv'.format(i)
    df = pd.read_csv(filename)
    df.insert(loc=0, column='observer', value=f'av1o0{i}')
    dfs.append(df)

# df1 = pd.read_csv('av1o01.csv')
# df2 = pd.read_csv('av1o02.csv')
# df3 = pd.read_csv('av1o03.csv')
# df4 = pd.read_csv('av1o04.csv')
# df5 = pd.read_csv('av1o05.csv')
# df6 = pd.read_csv('av1o06.csv')
# df7 = pd.read_csv('av1o07.csv')
# df8 = pd.read_csv('av1o08.csv')
# df9 = pd.read_csv('av1o09.csv')

df_sum = pd.concat(dfs)
df_sum = df_sum.sort_values(by=['start'])
df_sum.insert(loc=0, column='event', value='')

# df1.insert(loc=0, column='observer', value='av1o01')
# df2.insert(loc=0, column='observer', value='av1o02')
# df3.insert(loc=0, column='observer', value='av1o03')
# df4.insert(loc=0, column='observer', value='av1o04')
# df5.insert(loc=0, column='observer', value='av1o05')
# df6.insert(loc=0, column='observer', value='av1o06')
# df7.insert(loc=0, column='observer', value='av1o07')
# df8.insert(loc=0, column='observer', value='av1o08')
# df9.insert(loc=0, column='observer', value='av1o09')

# --- row ---
df_sum = df1.append(df2)
df_sum = df_sum.append(df3)
df_sum = df_sum.append(df4)
df_sum = df_sum.append(df5)
df_sum = df_sum.append(df6)
df_sum = df_sum.append(df7)
df_sum = df_sum.append(df8)
df_sum = df_sum.append(df9)

df_sum = df_sum.sort_values(by=['start'])
df_sum.insert(loc=0, column='event', value='')

# --- col ---
# dfs = [df1, df2, df3, df4, df5, df6, df7, df8, df9]

# for df in dfs:
#     if df.equals(df1):
#         pass
#     else:
#         common = pd.merge(df1, df, how='inner', on='start')
#         common_start = common['start']
#         for row in df.iterrows():
#             df_start = int(row.loc['start'])
#             if df_start in common_start:
#                 df_sum = df1.insert(column=str(row['index']),value=str(row.iloc[0]))
#             else: df_sum = df1.iloc[:,-1].append(row)
            

# added two cols: eventOnset and eventOffset 
# rename df from df_sum to emotion

for observer in emotion.index:
    end = emotion.loc[observer,'end']
    off = str('eventOffset')
    if 0 < end <= 253:
        emotion.loc[observer, off] = 1
    elif 254 <= end <= 293:
        emotion.loc[observer, off] = 2
    elif 294 <= end <= 326:
        emotion.loc[observer, off] = 3
    elif 327 <= end <= 368:
        emotion.loc[observer, off] = 4
    elif 369 <= end <= 416:
        emotion.loc[observer, off] = 5
    elif 417 <= end <= 499:
        emotion.loc[observer, off] = 6
    elif 500 <= end <= 539:
        emotion.loc[observer, off] = 7
    elif 540 <= end <= 570:
        emotion.loc[observer, off] = 8
    elif 571 <= end <= 652:
        emotion.loc[observer, off] = 9
    elif 653 <= end <= 686:
        emotion.loc[observer, off] = 10
    elif 687 <= end <= 698:
        emotion.loc[observer, off] = 11
    elif 699 <= end <= 763:
        emotion.loc[observer, off] = 12
    elif 764 <= end <= 777:
        emotion.loc[observer, off] = 13
    elif 778 <= end <= 837:
        emotion.loc[observer, off] = 14
    elif 838 <= end <= 880:
        emotion.loc[observer, off] = 15
    elif 881 <= end <= 940:
        emotion.loc[observer, off] = 16
    elif 941 <= end <= 974:
        emotion.loc[observer, off] = 17
    elif 975 <= end <= 1107:
        emotion.loc[observer, off] = 18
    elif 1108 <= end <= 1126:
        emotion.loc[observer, off] = 19
    elif 1127 <= end <= 1177:
        emotion.loc[observer, off] = 20
    elif 1178 <= end <= 1224:
        emotion.loc[observer, off] = 21
    elif 1225 <= end <= 1275:
        emotion.loc[observer, off] = 22
    elif 1276 <= end <= 1367:
        emotion.loc[observer, off] = 23
    elif 1368 <= end <= 1508:
        emotion.loc[observer, off] = 24
    elif 1509 <= end <= 1611:
        emotion.loc[observer, off] = 25
    elif 1612 <= end <= 1619:
        emotion.loc[observer, off] = 26
    elif 1620 <= end <= 1644:
        emotion.loc[observer, off] = 27
    elif 1645 <= end <= 1718:
        emotion.loc[observer, off] = 28
    elif 1719 <= end <= 1744:
        emotion.loc[observer, off] = 29
    elif 1745 <= end <= 1782:
        emotion.loc[observer, off] = 30
    elif 1783 <= end <= 1854:
        emotion.loc[observer, off] = 31
    elif 1855 <= end <= 1897:
        emotion.loc[observer, off] = 32
    elif 1898 <= end <= 2013:
        emotion.loc[observer, off] = 33
    elif 2014 <= end <= 2133:
        emotion.loc[observer, off] = 34
    elif 2134 <= end <= 2207:
        emotion.loc[observer, off] = 35
    elif 2208 <= end <= 2343:
        emotion.loc[observer, off] = 36
    elif 2344 <= end <= 2505:
        emotion.loc[observer, off] = 37
    elif 2506 <= end <= 2627:
        emotion.loc[observer, off] = 38
    elif 2628 <= end <= 3043:
        emotion.loc[observer, off] = 39
    elif 3044 <= end <= 3157:
        emotion.loc[observer, off] = 40
    elif 3158 <= end <= 3236:
        emotion.loc[observer, off] = 41
    elif 3237 <= end <= 3255:
        emotion.loc[observer, off] = 42
    elif 3256 <= end <= 3278:
        emotion.loc[observer, off] = 43
    elif 3279 <= end <= 3318:
        emotion.loc[observer, off] = 44
    elif 3319 <= end <= 3419:
        emotion.loc[observer, off] = 45
    elif 3420 <= end <= 3630:
        emotion.loc[observer, off] = 46
    elif 3631 <= end <= 3684:
        emotion.loc[observer, off] = 47
    elif 3685 <= end <= 3736:
        emotion.loc[observer, off] = 48
    elif 3737 <= end <= 3896:
        emotion.loc[observer, off] = 49
    elif 3897 <= end <= 3923:
        emotion.loc[observer, off] = 50
    elif 3924 <= end <= 3947:
        emotion.loc[observer, off] = 51
    elif 3948 <= end <= 4004:
        emotion.loc[observer, off] = 52
    elif 4005 <= end <= 4062:
        emotion.loc[observer, off] = 53
    elif 4063 <= end <= 4096:
        emotion.loc[observer, off] = 54
    elif 4097 <= end <= 4197:
        emotion.loc[observer, off] = 55
    elif 4198 <= end <= 4290:
        emotion.loc[observer, off] = 56
    elif 4291 <= end <= 4358:
        emotion.loc[observer, off] = 57
    elif 4359 <= end <= 4393:
        emotion.loc[observer, off] = 58
    elif 4394 <= end <= 4530:
        emotion.loc[observer, off] = 59
    elif 4531 <= end <= 4614:
        emotion.loc[observer, off] = 60
    elif 4615 <= end <= 4674:
        emotion.loc[observer, off] = 61
    elif 4675 <= end <= 4788:
        emotion.loc[observer, off] = 62
    elif 4789 <= end <= 4902:
        emotion.loc[observer, off] = 63
    elif 4903 <= end <= 4959:
        emotion.loc[observer, off] = 64
    elif 4960 <= end <= 5000:
        emotion.loc[observer, off] = 65
    elif 5001 <= end <= 5050:
        emotion.loc[observer, off] = 66
    elif 5051 <= end <= 5151:
        emotion.loc[observer, off] = 67
    elif 5152 <= end <= 5193:
        emotion.loc[observer, off] = 68
    elif 5194 <= end <= 5243:
        emotion.loc[observer, off] = 69
    elif 5244 <= end <= 5293:
        emotion.loc[observer, off] = 70
    elif 5294 <= end <= 5416:
        emotion.loc[observer, off] = 71
    elif 5417 <= end <= 5507:
        emotion.loc[observer, off] = 72
    elif 5508 <= end <= 5839:
        emotion.loc[observer, off] = 73
    elif 5840 <= end <= 6002:
        emotion.loc[observer, off] = 74
    elif 6003 <= end <= 6032:
        emotion.loc[observer, off] = 75
    elif 6033 <= end <= 6121:
        emotion.loc[observer, off] = 76
    elif 6122 <= end <= 6176:
        emotion.loc[observer, off] = 77
    elif 6177 <= end <= 6186:
        emotion.loc[observer, off] = 78
    elif 6187 <= end <= 6406:
        emotion.loc[observer, off] = 79
    elif 6407 <= end <= 6461:
        emotion.loc[observer, off] = 80
    elif 6462 <= end <= 6588:
        emotion.loc[observer, off] = 81
    elif 6589 <= end <= 6727:
        emotion.loc[observer, off] = 82
    elif 6728 <= end <= 7071:
        emotion.loc[observer, off] = 83
    else:
        emotion.loc[observer, off] = str('NA')

for observer in emotion.index:
    start = emotion.loc[observer,'start']
    on = str('eventOnset')
    if 0 < start <= 253:
        emotion.loc[observer, on] = 1
    elif 254 <= start <= 293:
        emotion.loc[observer, on] = 2
    elif 294 <= start <= 326:
        emotion.loc[observer, on] = 3
    elif 327 <= start <= 368:
        emotion.loc[observer, on] = 4
    elif 369 <= start <= 416:
        emotion.loc[observer, on] = 5
    elif 417 <= start <= 499:
        emotion.loc[observer, on] = 6
    elif 500 <= start <= 539:
        emotion.loc[observer, on] = 7
    elif 540 <= start <= 570:
        emotion.loc[observer, on] = 8
    elif 571 <= start <= 652:
        emotion.loc[observer, on] = 9
    elif 653 <= start <= 686:
        emotion.loc[observer, on] = 10
    elif 687 <= start <= 698:
        emotion.loc[observer, on] = 11
    elif 699 <= start <= 763:
        emotion.loc[observer, on] = 12
    elif 764 <= start <= 777:
        emotion.loc[observer, on] = 13
    elif 778 <= start <= 837:
        emotion.loc[observer, on] = 14
    elif 838 <= start <= 880:
        emotion.loc[observer, on] = 15
    elif 881 <= start <= 940:
        emotion.loc[observer, on] = 16
    elif 941 <= start <= 974:
        emotion.loc[observer, on] = 17
    elif 975 <= start <= 1107:
        emotion.loc[observer, on] = 18
    elif 1108 <= start <= 1126:
        emotion.loc[observer, on] = 19
    elif 1127 <= start <= 1177:
        emotion.loc[observer, on] = 20
    elif 1178 <= start <= 1224:
        emotion.loc[observer, on] = 21
    elif 1225 <= start <= 1275:
        emotion.loc[observer, on] = 22
    elif 1276 <= start <= 1367:
        emotion.loc[observer, on] = 23
    elif 1368 <= start <= 1508:
        emotion.loc[observer, on] = 24
    elif 1509 <= start <= 1611:
        emotion.loc[observer, on] = 25
    elif 1612 <= start <= 1619:
        emotion.loc[observer, on] = 26
    elif 1620 <= start <= 1644:
        emotion.loc[observer, on] = 27
    elif 1645 <= start <= 1718:
        emotion.loc[observer, on] = 28
    elif 1719 <= start <= 1744:
        emotion.loc[observer, on] = 29
    elif 1745 <= start <= 1782:
        emotion.loc[observer, on] = 30
    elif 1783 <= start <= 1854:
        emotion.loc[observer, on] = 31
    elif 1855 <= start <= 1897:
        emotion.loc[observer, on] = 32
    elif 1898 <= start <= 2013:
        emotion.loc[observer, on] = 33
    elif 2014 <= start <= 2133:
        emotion.loc[observer, on] = 34
    elif 2134 <= start <= 2207:
        emotion.loc[observer, on] = 35
    elif 2208 <= start <= 2343:
        emotion.loc[observer, on] = 36
    elif 2344 <= start <= 2505:
        emotion.loc[observer, on] = 37
    elif 2506 <= start <= 2627:
        emotion.loc[observer, on] = 38
    elif 2628 <= start <= 3043:
        emotion.loc[observer, on] = 39
    elif 3044 <= start <= 3157:
        emotion.loc[observer, on] = 40
    elif 3158 <= start <= 3236:
        emotion.loc[observer, on] = 41
    elif 3237 <= start <= 3255:
        emotion.loc[observer, on] = 42
    elif 3256 <= start <= 3278:
        emotion.loc[observer, on] = 43
    elif 3279 <= start <= 3318:
        emotion.loc[observer, on] = 44
    elif 3319 <= start <= 3419:
        emotion.loc[observer, on] = 45
    elif 3420 <= start <= 3630:
        emotion.loc[observer, on] = 46
    elif 3631 <= start <= 3684:
        emotion.loc[observer, on] = 47
    elif 3685 <= start <= 3736:
        emotion.loc[observer, on] = 48
    elif 3737 <= start <= 3896:
        emotion.loc[observer, on] = 49
    elif 3897 <= start <= 3923:
        emotion.loc[observer, on] = 50
    elif 3924 <= start <= 3947:
        emotion.loc[observer, on] = 51
    elif 3948 <= start <= 4004:
        emotion.loc[observer, on] = 52
    elif 4005 <= start <= 4062:
        emotion.loc[observer, on] = 53
    elif 4063 <= start <= 4096:
        emotion.loc[observer, on] = 54
    elif 4097 <= start <= 4197:
        emotion.loc[observer, on] = 55
    elif 4198 <= start <= 4290:
        emotion.loc[observer, on] = 56
    elif 4291 <= start <= 4358:
        emotion.loc[observer, on] = 57
    elif 4359 <= start <= 4393:
        emotion.loc[observer, on] = 58
    elif 4394 <= start <= 4530:
        emotion.loc[observer, on] = 59
    elif 4531 <= start <= 4614:
        emotion.loc[observer, on] = 60
    elif 4615 <= start <= 4674:
        emotion.loc[observer, on] = 61
    elif 4675 <= start <= 4788:
        emotion.loc[observer, on] = 62
    elif 4789 <= start <= 4902:
        emotion.loc[observer, on] = 63
    elif 4903 <= start <= 4959:
        emotion.loc[observer, on] = 64
    elif 4960 <= start <= 5000:
        emotion.loc[observer, on] = 65
    elif 5001 <= start <= 5050:
        emotion.loc[observer, on] = 66
    elif 5051 <= start <= 5151:
        emotion.loc[observer, on] = 67
    elif 5152 <= start <= 5193:
        emotion.loc[observer, on] = 68
    elif 5194 <= start <= 5243:
        emotion.loc[observer, on] = 69
    elif 5244 <= start <= 5293:
        emotion.loc[observer, on] = 70
    elif 5294 <= start <= 5416:
        emotion.loc[observer, on] = 71
    elif 5417 <= start <= 5507:
        emotion.loc[observer, on] = 72
    elif 5508 <= start <= 5839:
        emotion.loc[observer, on] = 73
    elif 5840 <= start <= 6002:
        emotion.loc[observer, on] = 74
    elif 6003 <= start <= 6032:
        emotion.loc[observer, on] = 75
    elif 6033 <= start <= 6121:
        emotion.loc[observer, on] = 76
    elif 6122 <= start <= 6176:
        emotion.loc[observer, on] = 77
    elif 6177 <= start <= 6186:
        emotion.loc[observer, on] = 78
    elif 6187 <= start <= 6406:
        emotion.loc[observer, on] = 79
    elif 6407 <= start <= 6461:
        emotion.loc[observer, on] = 80
    elif 6462 <= start <= 6588:
        emotion.loc[observer, on] = 81
    elif 6589 <= start <= 6727:
        emotion.loc[observer, on] = 82
    elif 6728 <= start <= 7071:
        emotion.loc[observer, on] = 83
    else:
        emotion.loc[observer, on] = str('NA')
        
emotion.to_excel("emotion.xlsx")
