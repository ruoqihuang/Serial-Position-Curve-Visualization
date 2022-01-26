#!/usr/bin/env python
# coding: utf-8

# In[68]:


#Author: Ruoqi Huang
#Affliation: University of Toronto
#This is a part of the data analysis of the PSY379 Final Project


# In[69]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[70]:


#wl_dic_1 = ['Humble', 'Complete', 'Impulse', 'Moisture' ,'Reason' ,'Credit' ,'Twinkle' ,'Pupil' ,'Herald' ,'Early' 
            #,'Remove' ,'Instant' ,'County' ,'Refuse' ,'Candy' ,'Errand' ,'Upper' ,'Consult' ,'Button' ,'Trifle']
#wl_dic_2 = ['Plainly' ,'Shallow' ,'Candle' ,'Even' ,'Youthful' ,'Answer' ,'Rival' ,'Improve' ,'Table' ,'Distress' ,'Maintain' ,'Reveal'
 #,'Music' ,'Enter' ,'Shepard' ,'Charming' ,'Native' ,'Below' ,'Awake' ,'Mischief']


# In[71]:


wl_dic_1 = ['Humble', 'Complete', 'Impulse', 'Moisture' ,'Reason' ,'Credit' ,'Twinkle' ,'Pupil' ,'Herald' ,'Early']
wl_dic_2 = ['Plainly' ,'Shallow' ,'Candle' ,'Even' ,'Youthful' ,'Answer' ,'Rival' ,'Improve' ,'Table' ,'Distress']


# In[72]:


couter_dic12 = {}
for words in wl_dic_1:
    couter_dic12[words] = 0
for words in wl_dic_2:
    couter_dic12[words] = 0


# In[73]:


couter_dic21 = {}
for words in wl_dic_2:
    couter_dic21[words] = 0
for words in wl_dic_1:
    couter_dic21[words] = 0


# In[74]:


#make sure dictionaries are well set up
print(couter_dic12)
print(couter_dic21)


# In[75]:


import csv


# In[76]:


file = open('379_data_k.csv')
type(file)
csvreader = csv.reader(file)


# In[77]:


def serial_analysis(readerfile):
    rows = []
    participant1 = []
    participant2 = []
    
    for row in readerfile:
        rows.append(row)
#print(rows)
#sorting participant based on their id, 1256
    for participant in rows:
        for item in participant:
            if len(item) != 0:
                if item[1] in ['1', '2']:
                   participant1.append(participant)
#sorting participant based on their id, 3478
    for participant in rows:
        for item in participant:
            if len(item) != 0:
                if item[1] in ['3', '4']:
                   participant2.append(participant)
#counting appearance of each word, 1256
    for participant in participant1:
        for item in participant:
            title_item = item.title()
            if title_item in couter_dic12:
                couter_dic12[title_item] += 1
#counting appearance of each word, 3478
    for participant in participant2:
        for item in participant:
            title_item = item.title()
            if title_item in couter_dic21:
                couter_dic21[title_item] += 1
    return(couter_dic12, couter_dic21)


# In[78]:


serial_analysis(csvreader)


# In[79]:


list12 = []
for i in wl_dic_1:
    list12.append(couter_dic12[i])
for i in wl_dic_2:
    list12.append(couter_dic12[i])


# In[80]:


list21 = []
for i in wl_dic_2:
    list21.append(couter_dic21[i])
for i in wl_dic_1:
    list21.append(couter_dic21[i])


# In[83]:


avgcount = []
for i in range(0,20):
    avg = (list12[i]+list21[i])/2
    avgcount.append(avg)


# In[84]:


file = '379_data_y.csv'        
oscar_demographics = pd.read_csv(file)
#import chardet
#with open(file, 'rb') as rawdata:
#    result = chardet.detect(rawdata.read(100000))
#result
#oscar_demographics = pd.read_csv(file,encoding='ISO-8859-9')
#oscar_demographics.head()


# In[85]:


num_list = []
for i in range(1, len(couter_dic21)+1):
    num_list.append(i)
print(num_list)


# In[86]:


#plot
words_list = num_list
value_list = couter_dic12.values()
plt.plot(words_list,value_list, color='red', marker='o')
plt.title('Serial Position Cruve-Participants No. 1/2/5/6')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.show()


# In[87]:


words_list = num_list
value_list = couter_dic21.values()
plt.plot(words_list,value_list, marker='o')
plt.title('Serial Position Cruve-Participants No. 3/4/7/8')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.show()


# In[88]:


words_list = num_list
value_list = couter_dic21.values()
plt.plot(words_list,avgcount, marker='o')
plt.title('Serial Position Cruve-Participants Averaged')
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.show()


# In[89]:


numbers = avgcount
window_size = 5

i = 0
moving_averages = []
while i < len(numbers) - window_size + 1:
    this_window = numbers[i : i + window_size]
#get current window
    window_average = sum(this_window) / window_size
    moving_averages.append(window_average)
    i += 1

print(len(moving_averages))


# In[92]:


num_list1 = []
for i in range(1, len(couter_dic21)-3):
    num_list1.append(i)
print(num_list1)
print(moving_averages[15])


# In[95]:


words_list = num_list1
value_list = moving_averages
plt.plot(words_list,moving_averages, marker='o')
plt.title('Serial Position Cruve-Experiment Condition First')
plt.annotate('Attnetion Check',(10,1.4))
plt.annotate('Attnetion Check',(20,0.9))
plt.annotate('Attnetion Check',(30,1.2))
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.show()


# In[94]:


#test: one really easy way, the number of responses, uniformly distributed across time
#mark where the attentional check is


# In[ ]:




