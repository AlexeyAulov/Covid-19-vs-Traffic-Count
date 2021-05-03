# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:32:02 2021

@author: Alexv
"""

"""Alexey Aulov"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_COVID_19 = pd.read_csv('COVID_19.csv')
df_VOL_19 = pd.read_csv('CC_Volume_Data_R01_2019.csv')
df_VOL_20 = pd.read_csv('CC_Volume_Data_R01_2020.csv')

# I added column DID to represent Date ID in all of them 

df_FIL_COVID_19 =df_COVID_19[['DID','DATE_OF_INTEREST','CASE_COUNT','YEAR','MONTH','DAY','RCSTA']].head(260)

df_FIL_VOL_19 = df_VOL_19[['DID','RCSTA','INTERVAL_19_A','YEAR','MONTH','DAY']].head(260)

df_FIL_VOL_20 = df_VOL_20[['DID','RCSTA','INTERVAL_19_B','YEAR','MONTH','DAY']].head(260)

print("Printing filtered Volume Count 2019\n",df_FIL_VOL_19)
print("")
print("")
print("Printing filtered Volume Count 2020\n",df_FIL_VOL_20)

    
print("Printing COVID 19 DATA\n",df_FIL_COVID_19)

Merged_Data=pd.merge(pd.merge(df_FIL_VOL_19,df_FIL_VOL_20,on=['DID']),df_FIL_COVID_19, on=['DID'])


#print(df_FIL_VOL_19.info())
#print(df_FIL_VOL_20.info())

#print what information on rows and columns of the website

print(Merged_Data.info())


#Interval_19 represents the time slot of that day which is 7pm and represents the volume count. 
#print("The A:",Merged_Data.loc[0:258, 'INTERVAL_19_A'])
#print("The A:",Merged_Data.loc[0:258, 'INTERVAL_19_B'])



Compare1=Merged_Data.iloc[0:258:1, 2]
Compare2=Merged_Data.iloc[0:258:1, 7]

print("Interval A")
print(Compare1)
print("Interval B")
print(Compare2)

Comparison=(Compare1>Compare2)
Result=sum(Comparison)
print(Result)

#Results shows that 2020 has a greater traffic count than 2019



"""
x=Merged_Data['DID']
y1=Merged_Data['CASE_COUNT']
y2=Merged_Data['INTERVAL_19_A']
y3=Merged_Data['INTERVAL_19_B']

#Line graph to show the correlation between Covid 19 and Traffic Count 2020 and 





plt.title('Covid 19 vs Traffic Count')
plt.xlabel('DID(Date ID) for 2020')
plt.ylabel('Count')

#plt.xlim(0,90)#Zoomed in Version of the first 91 days (delete comment to look)
#plt.xlim(100,200)#Zoomed in Version of 100 to 200 days (delete comment to look)

plt.plot(x,y1,color='red', label='Covid 19 Case Count') 
plt.plot(x,y2, color='blue', label='7pm Traffic Count')
plt.legend()
plt.show()
"""


#Line graph to show differences in traffic count of 2019 and 2020 at 7pm every day

"""
Uncomment line 90 until 100

plt.title('Traffic Count 2019 vs Traffic Count 2020')
plt.xlabel('DID(Date ID) for 2019/2020')
plt.ylabel('Traffic Count')
plt.plot(x,y2,color='orange', label='Traffic Count 2019') 
plt.plot(x,y3,color='green', label='Traffic Count 2020')
plt.legend()
plt.show()
"""





