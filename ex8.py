# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:25:07 2019

@author: Hadeel
"""
import pandas as pd
import numpy as np
#exercise 1
print("------- EX 1 -----------------------")
data=[2, 4, 6, 8, 10]
d2 = pd.Series(data)
print(data)

#**************************************************
#exercise 2
print("------- EX 2 -----------------------")
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
d2 = pd.Series(d1)
print (d2)

#**************************************************
#exercise 3
print("------- EX 3 -----------------------")
data = [20, 10, 150, 110, 100, 50]
d2 = pd.Series(data)
print ( d2.describe() )
d2.plot(kind="bar",color=['red','black','green','blue','yellow','cyan'])


#**************************************************
#exercise 4
print("------- EX 4 -----------------------")
Data = {'d1':[100,200,5,400,700,100,200,50,400,700],'d2':[140,0,300,400,200,140,0,700,400,200] }
d2 = pd.DataFrame(Data)
print ( d2.describe() )
d2.plot()


#**************************************************
#exercise 5
print("------- EX 5 -----------------------")
SampleData={'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
d2 = pd.DataFrame(SampleData)
print(d2)


#**************************************************
#exercise 6
print("------- EX 6 -----------------------")
data={"names":['Bob','Jessica','Mary','John','Mel'],"birth": [968, 155, 77, 578, 973]}
d2 = pd.DataFrame(data)
print(d2)
"""
d2.plot(kind="pie")
"""
d2.plot.pie(y='birth', figsize=(5, 5))
#**************************************************
#exercise 7
print("------- EX 7 -----------------------")
data = [100, 2200, 300, 400, 500, 600,700,800,900]
d2 = pd.Series(data)
print(d2.describe())
d2.to_csv('myDataFrame.csv', sep='\t')
d2.to_csv('myDataFrame.csv', sep=',')


#**************************************************
#exercise 8
print("------- EX 8 -----------------------")

dates = pd.date_range('20000101', periods=4)
df= pd.DataFrame(np.random.randn(4, 2), index=dates,columns=["A","B"])
print(df)

"""
                   A         B
2000-01-01 -0.582069 -0.934476
2000-01-02 -0.431116  1.146147
2000-01-03 -0.285202 -0.288402
2000-01-04 -0.611363  0.894425
"""
print(df.head(2))
"""
                   A         B
2000-01-01 -0.582069 -0.934476
2000-01-02 -0.431116  1.146147
"""
print(df[["A"]])
"""
                   A
2000-01-01 -0.582069
2000-01-02 -0.431116
2000-01-03 -0.285202
2000-01-04 -0.611363
"""
print(df[0:1])
"""
                   A         B
2000-01-01 -0.582069 -0.934476
"""
print(df["20000102":"20000104"])
"""
                   A         B
2000-01-02 -0.431116  1.146147
2000-01-03 -0.285202 -0.288402
2000-01-04 -0.611363  0.894425
"""
print(df.loc['20000102':'20000104', ['A']])
"""
                   A
2000-01-02 -0.431116
2000-01-03 -0.285202
2000-01-04 -0.611363
"""

print(df.iloc[:, 1:2])
"""
                   B
2000-01-01 -0.934476
2000-01-02  1.146147
2000-01-03 -0.288402
2000-01-04  0.894425
"""

print(df[df> 0])
"""
             A         B
2000-01-01 NaN       NaN
2000-01-02 NaN  1.146147
2000-01-03 NaN       NaN
2000-01-04 NaN  0.894425
"""
print(df[df.B> 0])
"""
                   A         B
2000-01-02 -0.431116  1.146147
2000-01-04 -0.611363  0.894425
"""
df['A'] = [100,200,300,100]
print (df)
"""
              A         B
2000-01-01  100 -0.934476
2000-01-02  200  1.146147
2000-01-03  300 -0.288402
2000-01-04  100  0.894425
"""
print(df[df['A'].isin([200, 300])])
"""
              A         B
2000-01-02  200  1.146147
2000-01-03  300 -0.288402
"""