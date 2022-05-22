import pandas as pd
# For question 1
df1 = pd.DataFrame({'Name' : ['Noa','Ayala','Tal','Lea'],
                   'Gender' : ['F','F','M','F'],
                   'Age' : [18,19,23,30]})

# For question 2
df2 = df1['Name']

# For question 3
df3 = df1.loc[(df1['Gender'] == "F")]


# For question 4
df4 = df1.loc[(df1['Age'] >= 19)]



# For question 5
df5 = df1.loc[(df1['Name'] != 'Tal')]


#For question 6
df6 = df1.loc[(df1['Name'] == 'Tal') | (df1['Age'] < 20)]


# For question 7
df7 = df1.loc[(df1['Gender'] == 'F') & (df1['Age'] < 20)]

# For question 8
df8 = df1.loc[(df1['Name'] == 'Tal') | (df1['Age'] < 20)]
#df8.to_excel('df6.xlsx')


# For question 9
df9 = df1.loc[(df1['Gender'] == 'F') & (df1['Age'] < 20)]
#df9.to_csv('df7.csv')

# For question 10
df10 = pd.read_excel("people.xlsx")

#For question 11
df11 = df10.loc[(df10['age'] == 95)]

#For question 12
df12 = df10.loc[(df10['name'] == 'Tal')]

#For question 13
df13 = df10.loc[(df10['name'] == 'Tal')]

#For question 14
df14 = df10.loc[(df10['age'] == 22)]

#For question 15
df15 = df10.loc[(df10['name'] == 'Tal') | (df10['name'] == 'Maya')]

#For question 16
df16 =  df10.loc[(df10['name'] == 'Nadav') | (df10['age'] == 6)]

#For question 17
df17 = df10.loc[(df10['age'] == 21) | (df10['age'] == 23)]

#For question 18
df18 = df10.loc[(df10['age'] >= 21) & (df10['age'] <= 23)]


#For question 19
df19 = df10.loc[(df10['name'] != 'Noa') & (df10['gender'] == 'F')]


#For question 20
df20 = df10.loc[(df10['age'] != 15) & (df10['age'] != 20)]


#For question 21
df21 = df10.loc[(df10['age'] != 30) & (df10['age'] != 35)]

#For question 22
df22 = df10.loc[(df10['age'] == 21) & (df10['gender'] == 'M')]


#For question 23
df23 = df10.loc[(df10['name'] == 'Tal') & (df10['gender'] == 'M')]


#For question 24
df24 = df10.loc[(df10['age'] >= 6) & (df10['age'] <= 20) & (df10['gender'] == 'F')]

#For question 25
df25 = df10.loc[(df10['birth_date'].isnull())]

#For question 26

df26 = df10.loc[(df10['name'] == 'Tal') | (df10['name'] == 'Noa') | (df10['name'] == 'Shlomi') &  (df10['age'] >= 50) & (df10['gender'] == 'F')]

#For question 27

df27 = df10.loc[(df10['age'] == 5) & (df10['gender'] == 'M') & (df10['name'] == 'Ido') | (df10['gender'] == 'F') & (df10['name'] == 'Shani') | (df10['name'] == 'Inbar') | (df10['name'] == 'Talia')]
