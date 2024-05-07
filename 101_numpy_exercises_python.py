#%% 1. How to import pandas and check the version?
import pandas as pd # type: ignore
import numpy as np # type: ignore
print(pd.__version__)
print(pd.show_versions(as_json=True))

# %% 2. How to create a series from a list, numpy array and dict?
myList = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(myList, myarr))

series1 = pd.Series(myList)
series2 = pd.Series(myarr)
series3 = pd.Series(mydict)

# %% 3. How to convert the index of a series into a column of a dataframe?
myList = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(myList, myarr))
ser = pd.Series(mydict)

df = ser.to_frame().reset_index()
print(df.head())
# %% 4. How to combine many series to form a dataframe?
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df = pd.concat([ser1, ser2], axis=1)
print(df.head())

# %% 5. How to assign name to the series’ index?
ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))

ser.name = 'alphabets'
ser.head()
# %% 6. How to get the items of series A not present in series B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ser1[~ser1.isin(ser2)]

# %% 7. How to get the items not common to both series A and series B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ser_u = pd.Series(np.union1d(ser1, ser2))
ser_i = pd.Series(np.intersect1d(ser1, ser2))
ser_u[~ser_u.isin(ser_i)]
# %% 8. How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
ser = pd.Series(np.random.normal(10, 5, 25))

np.percentile(ser, q=[0, 25, 50, 75, 100])

# %% 9. How to get frequency counts of unique items of a series?
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))

ser.value_counts()
# %% 10. How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

print("Top 2 Freq:", ser.value_counts())
ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'
ser

# %% 11. How to bin a numeric series to 10 groups of equal size?
ser = pd.Series(np.random.random(20))

bin = pd.qcut(ser, q=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1], labels=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th'])
bin
# %% 12. How to convert a numpy array to a dataframe of given shape?
ser = pd.Series(np.random.randint(1, 10, 35))

df = pd.DataFrame(ser.values.reshape(7,5))
df

df = pd.DataFrame(np.random.randint(1,10,35).reshape(7,5))
df
# %% 13. How to find the positions of numbers that are multiples of 3 from a series?
ser = pd.Series(np.random.randint(1, 10, 7))

print(ser)
print(ser[ser%3 == 0].index)

np.argwhere(ser%3==0)
# %% 14. How to extract items at given positions from a series?
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]

s1 = ser.take(pos)
print(s1)

s2 = ser[ser.index.isin(pos)]
print(s2)
# %% 15. How to stack two series vertically and horizontally ?
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

v = pd.concat([ser1, ser2], axis=0)
h = pd.concat([ser1, ser2], axis=1)
print(v)
print(h)
# %%
