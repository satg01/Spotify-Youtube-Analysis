#!/usr/bin/env python
# coding: utf-8

# ### SPOTIFY & YOUTUBE DATA ANALYSIS

# 
# 

# #### The Dataset i will be work on consists of Various artists multiple songs ,with 20718 data entries with total 26 variable columns that consists columns like Track album, album type etc

# #### here i will be analysing the data based on different variables (columns) contributon

# database link(https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube)

# ### Importing the  required Libraries

# In[25]:


#visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# importing csv file using pandas

# In[26]:


#reading the data 
df=pd.read_csv("C:\Desktop\Data Analyst Project\spoify youtube\Spotify_Youtube.csv")


# In[27]:


df.describe()


# In[28]:


df.info()#get the information of dataset


# #### Based on the above data the following observation can be made:
# 

# 1.This dataset contains 28 columns and 20718 rows .

# 2.some columns contain null values as well
# further analysis can be performed by examining each column and taking necessary steps to perform the analysis.

# 3.Additionaly insights can be derived by investigating each column,which  may provide useful information about youtube or spotify data.

# In[29]:


df.shape


# here we have 28 columns and 20718 rows in this dataset

# In[30]:


#viewing the columns
df.columns


# # Clean Data

# ### Remove the unnecessary  columns from the dataset

# In[31]:


extra_cols=['Unnamed: 0','Title','Url_spotify','Uri','Url_youtube']
df.drop(extra_cols,axis=1,inplace=True)


# here we have  removed 'Unnamed: 0','Title','Url_spotify','Uri' and 'Url_youtube' columns
# from the dataset beacsuse they are not in need for analysis

# In[32]:


#viewing the number of unique value of the each column
df.nunique() 


# we can see here ,we  have the unique value of each columns as we have 2079 artist,17841 track ,3 album_type ,11232 album and other columns unique values

# In[33]:


#checking the number of null values  in each column
df.isna().sum()


# now we can see here the number of null values in each column we have more null values in channel:470,Views:470,Comments:470,Licensed:470 and Description:876 etc

# In[34]:


#removing all the null values from the columns
df.dropna(inplace=True)


# In[35]:


#now again rechecking the null value (if there any missing)
df.isnull().sum()


# In[36]:


df.shape # shape is the number of columns and rows 


# after removing the unnecessary columns and null values from columns ,now we have 19170 rows and 23 columns

# #### Changing the data type  of the columns as per need 

# In[49]:


df['Views']=df['Views'].astype('int')
df['Likes']=df['Likes'].astype('int')
df['Comments']=df['Comments'].astype('int')


# here we have successfuly changed the views and Comments columns float to int 

# # Exploratory Data Analysis

# In[38]:


#Processing the data
df.head(10)


# ### Determining the top 10 artists on the Spotify platform whose songs have more views.

# In[39]:


#df.groupby(['Artist'])['Views'].sum().reset_index().sort_values(by='Views',ascending=False).head(10)


# In[40]:


view=df.groupby('Artist')['Views'].agg('sum').reset_index().sort_values('Views',ascending=False).head(10)
view


# In[41]:


view.set_index('Artist',inplace=True)
view.plot(kind='bar',color='g')
plt.xlabel('Artist')
plt.ylabel('Views')
plt.title('Top 10  Artist with higher views')
plt.xticks(rotation=70)


# we can see here Bruno mars was the most viewed artist with 10.23 billion views.Macklemore & Ryan Lewis  and Macklemore & Ryan Lewis are the second and third artist with 10.12 billion views and 10 billion respectively.
# BLACKPINK and J Balvin  complete the top 5 artists with 9.4 billion and 8.4 billion views ,
# Nicki Minaj,Earth, Wind & Fire  and Post Malone occupy positions from sixth to eight  with 8 billion,6.4billion and 6.3 billion respectively
# one direction and nicky jam complete the top 10 artist with 6.3 and 6.32 billion views
# These figures highlight the popularity of these artists and their music, as well as the significant role of online video platforms in promoting and distributing music.

# ### Determining the Top 10 artist with most Likes on youtube

# In[50]:


#groupby the artist 
df.groupby('Artist')['Likes'].agg('sum').sort_values(ascending=False).head(10)


# In[52]:


#make graph of the top 10 most liked artists in Youtube,  bar chart

ax=df.groupby('Artist').agg({'Likes':'sum','Stream':'sum'}).reset_index()
bx=ax.sort_values('Likes',ascending=False).head(10)
sns.barplot(data=bx,x='Likes',y='Artist')
plt.title('Top 10 most Liked Artist ')


# as we can see here BTS is the most liked artist with 14 million likes and after this blackpink is on second place here and and in the fourth place in top views ,and in third and fourth charlie puth and ed sheeran with 10 million and 8 million likes respectively 

# ### Determine the top 10 Streamers on spotify

# In[44]:


cx=ax.sort_values('Stream',ascending=False).head(10)


# In[45]:


df.groupby('Artist')['Stream'].agg('sum').head(10)


# In[46]:


sns.barplot(data=cx,y='Stream',x='Artist')
plt.xticks(rotation=80)
plt.title('Top 10 streamers')


# as we can see post malone is one first position in streamers with 1.2 billion streams and in second position ed sheeran with 1.74 billion streams , 
# dua lipa ,the weken and xxxtentacion from third to fifth position with 1.4, 1.3 billion  and 46 million streams respectively

# ## who is the most commented artist on youtube

# In[53]:


ax=df.groupby('Artist')['Comments'].sum().reset_index().sort_values(by='Comments',ascending=False).head(10)
ax


# as we can see BTS on the top first position with 39 million comments after this blackpink 19 million ,stray kids, twice,psy from third to fifth position with 8.4 million to 7.4 million comments

# In[54]:


sns.barplot(data=ax,y='Artist',x='Comments')
plt.title('Top 10 most commented Artist')


# #### aggregate  views ,comments  and likes based on artist

# In[58]:


tc=df.groupby('Track').agg({'Views':'sum','Comments':'sum','Likes':'sum'}).reset_index()
bv=tc.sort_values('Views',ascending=False).head(10)
bv


# ### what are top 10 songs on youtube with higher views.

# In[59]:


plt.barh(bv['Track'],bv['Views'],color='g')
plt.title('Top 10 most  Viewed tracks')
plt.show()


# as we can see most viewed song on youtube is Swalla .feat. Nicki Minaj & Ty Dolla $ign with 5.1 billion views and on second Thrift shop with 4.5 billion views 
#  on third ,fourth and fifth something just like this,sin pijama and somebody that i used with 4.1 to 4.2 billion views

# ### determine most commented song on youtube

# In[60]:


av=tc.sort_values('Comments',ascending=False).head(10)
av


# In[61]:


plt.barh(av['Track'],av['Comments'])
plt.title('Top 10 most commented Tracks')
plt.show()


# Dynamite with 1.8 billion comments on first position on youtube

# ### most liked song on youtube or spotify 

# In[62]:


sn=tc.sort_values('Likes',ascending=False).head(10)
sn


# In[65]:



plt.barh(sn['Track'],sn['Likes'],color='r')
plt.title('Top 10 most Liked tracks')
plt.show()


# Despacito song most liked song on youtube with 10 million likes

# ### most viewed song  relatiship with stream

# In[55]:


df.groupby('Track').agg({'Views':'sum','Stream':'sum'}).reset_index().sort_values(by='Views' ,ascending=False).head(10)


# The reason why songs with the most views on YouTube are not the top songs on Spotify could be due to a variety of factors. Some songs that are popular on YouTube may not be as popular on Spotify because the audiences of these two platforms have different preferences. Additionally, the algorithms used by each platform to recommend and promote songs may also differ, leading to differences in the popularity of songs on each platform. Finally, other factors such as marketing and promotion by artists and record labels may also play a role in the popularity of songs on each platform

# ### which is the most viewed album type on youtube

# In[45]:


ac=df.groupby(['Album_type'])['Views'].sum().head()
ac


# # * which album type is getting more views

# In[58]:


gp=df.groupby('Album_type')['Views'].sum().reset_index()
sns.set(style="whitegrid")
plt.pie(data=gp,x='Views',labels='Album_type',autopct='%1.0f%%')
plt.title('Album Views by Types')


# #### From the above Pie chart we can make few conclusions like:
# 

# * album type is most popular type ,the data shows in album type has 1.148762e+12 views which is 75% of data total data, and it is higher compared to other compilation and single types

# * after the album type singles are most popular as compare to compilation, the data shows in single is 3.300549e+11 views which is 22% of total data and compilation is 3% (4.882922e+10 views)
#  

# ### Top 10 licensed album on youtube & spotify

# In[60]:


al=df[df['Licensed']==1]
la=al['Album'].value_counts()[:10]
plt.pie(la,autopct='%.2f%%',labels=la.index)
plt.show()


# here we can see heroes and willains with 12.34 records highest number of song distributor on albums

# ### make a histogram to visualize all the important factors of singers

# In[48]:


df.hist(bins=40,figsize=(20,18))


# ### Display heatmap

# In[49]:


plt.figure(figsize=(10,8))
sns.heatmap(df.corr(),linewidth=0.6,annot=True,fmt='.1f',linecolor='black',cmap="jet")
plt.axis('tight')
plt.title('Heatmap')
plt.show()


# This heatmap represents the correlation between the audio features. We can see there are some positive and negative correlation between audio features

# ### Determine Most viewed top 10  album on youtube 

# In[71]:


A=df.groupby(['Album'])['Views'].sum().reset_index().sort_values(by='Views', ascending=False).head(10)
A


# In[80]:


sns.barplot(data=A,x='Views',y='Album')


# the hiest  with 11 billion views is on the first place of highest viewed album
# after this swala with 5.1 billion views on second place

# ### which is the most Liked album on youtube and spotify

# In[81]:


b=df.groupby(['Album'])['Likes'].sum().reset_index().sort_values(by='Likes', ascending=False).head(10)
b


# In[105]:


sns.barplot(data=b, y='Album',x='Likes',color='green')
plt.xticks(rotation=90)


# album vida is most liked album with 120 million likes and see you again ,the heist on second and thrd place respectively with 80 and 74 million views 

# ### Most commented album on youtube

# In[113]:


df.groupby(['Album'])['Comments'].sum().reset_index().sort_values(by='Comments', ascending=False).head(10)


# In[101]:



ax=df.groupby('Album').agg({'Comments':'sum','Stream':'sum'}).reset_index()
bx=ax.sort_values('Comments',ascending=False).head(10)
sns.barplot(data=bx,x='Comments',y='Album')
plt.title('Top 10 most commented')


# BE is the most commented album nad on second position map of soul ,higher number of comments means least album but in fourth place the VIDA which have higher likes as well means its most like and commented song with positive response

# ### top streamed album on youtube

# In[97]:


c=df.groupby(['Album'])['Stream'].sum().reset_index().sort_values(by='Stream', ascending=False).head(10)
c


# In[120]:


sns.barplot(data=c,y='Album',x='Stream',color='yellow')


# The reason why songs with the most views on YouTube are not the top songs on Spotify could be due to a variety of factors. Some songs that are popular on YouTube may not be as popular on Spotify because the audiences of these two platforms have different preferences. Additionally, the algorithms used by each platform to recommend and promote songs may also differ, leading to differences in the popularity of songs on each platform. Finally, other factors such as marketing and promotion by artists and record labels may also play a role in the popularity of songs on each platform.
# ​

# ### Identifying the top 10 channels based on views

# In[25]:


a=df.groupby(['Channel'])['Views'].sum().reset_index().head(10)
b=a.sort_values(by='Views',ascending=False)
b


# In[26]:


plt.barh(b['Channel'],b['Views'])


# G is the most viewed channel on yotube after this ucideboy ,sourapple and 070 shake are on top 5 positions

# ### what are the top liked channel on youtube

# In[27]:


a=df.groupby(['Channel'])['Likes'].sum().reset_index().head(10)
b=a.sort_values(by='Likes',ascending=False)
b


# In[28]:


sns.barplot(data=b,x='Likes' ,y='Channel')


# as we can see G Dle with 13 million likes and after this uicideby with 3.3 million likes in second place

# ### determining the relationship between energy and loudness

# In[68]:


sns.lmplot(data=df,x='Energy',y='Loudness',line_kws={'color':'red'})


# as we can see the loudness increases with energy and viceversa

# ### The Relationship between Views and Streams

# In[37]:


sns.lmplot(data=df,x='Views',y='Stream',line_kws={'color':'red'})


# ### The Relationship between like and comments

# In[39]:


sns.lmplot(data=df,x='Likes',y='Comments',line_kws={'color':'red'})
plt.show()


# ### Relationship between like and views

# In[40]:


sns.lmplot(data=df,x='Likes', y='Views',line_kws={'color':'black'})
plt.grid(True)
plt.axis('tight')


# ### Determine the Relation between Acoustiness and energy

# In[69]:


df.columns


# In[71]:


fig = plt.figure(figsize=(10,5))
sns.jointplot(data=df,x='Acousticness',y='Energy',kind='hist')
plt.ylabel("Energy", labelpad=20)
plt.xlabel("Acoustiness", labelpad=20)


# A track with high acousticness is likely to be composed of mostly acoustic instruments, such as guitar, piano, or strings, whereas a track with low acousticness is likely to be composed of mostly electronic instruments. A negative correlation between energy (left side) and acousticness indicates that as the energy of a track increases, the amount of acoustic instruments decreases, and vice versa. We can see the similar pattern for loudness (right side) also. Where acousticnes tend to decreases as loudness increase.

# ### Determine  the Relationship between tempo and speechiness

# In[64]:


fig = plt.figure(figsize=(10,5))
sns.jointplot(data=df,x='Tempo',y='Speechiness',kind='scatter')
plt.ylabel("Speechiness", labelpad=20)
plt.xlabel("Tempo", labelpad=20)
plt.axis('tight')


# we can see there is a correlation between speechiness and tempo ,as the songs with faster tempo have higher level of speechiness have higher level of speechiness . 

# ### Relatonship between tempo and key

# In[72]:


fig = plt.figure(figsize=(10,5))
sns.jointplot(data=df,x='Tempo',y='Key',kind='hist')

plt.ylabel("Speechiness", labelpad=20)
plt.xlabel("Tempo", labelpad=20)


# The key of a song can influence its emotional tone and can also affect its perceived tempo. For example, a song in a minor key might have a slower perceived tempo than a song in a major key, even if the actual tempo is the same

# ### Relationship bw Instrumentalness and speechiness

# In[71]:


sns.jointplot(data=df,x = 'Instrumentalness', y = 'Speechiness', kind = 'scatter')


# These two columns are often inversely related, as songs with a higher level of speechiness often have a lower level of instrumentalnessThis is because spoken word or rap tends to be more focused on the lyrics and vocal delivery, while instrumental music tends to be more focused on the music itself.

# ### Relation between Instrumentalness and Acousticness

# In[77]:


sns.jointplot(data=df,x='Instrumentalness',y='Acousticness',kind='resid')


# These two columns are often positively correlated, meaning that songs with high levels of acousticness also tend to have high levels of instrumentalness. This is because acoustic instruments are often used to create instrumental music, and instrumental music often features acoustic instruments.

# ### Relationship between Danceability and Energy

# In[80]:


sns.jointplot(data=df, x ='Danceability', y = 'Energy', kind = 'hex')


# These two columns can be closely related, as songs with high danceability often have a high energy level as well. This is because danceable songs typically have a strong and consistent beat that encourages movement, which often correlates with a high-energy sound.

# ### Relationship bw Loudness and Energy

# In[84]:


sns.jointplot(data = df, x = 'Loudness', y = 'Energy', kind = 'scatter')


# Loudness and Energy are two audio features that are commonly used to describe music. Loudness refers to the perceived volume of a song, while Energy refers to the intensity or activity level of a song. In general, songs with high loudness tend to have high energy as well, as they are often more intense and dynamic. However, we can see there are some songs that have high energy without being particularly loud, or vice versa.
# 

# ### Relationship bw valence and Energy 

# In[85]:


sns.jointplot(data =df, x = 'Valence', y = 'Energy', kind = 'resid')


# There is often a positive correlation between energy and valence, meaning that songs with high energy levels tend to have a more positive emotional tone. This may be because high-energy songs often have a more upbeat and lively sound that is associated with positive emotions like happiness and excitement

# # Conclusion

# Music is not just a medium of timepass or entertainment its  a universal language that connects people across world with different cultures . But how do people choose what music to listen to and where to listen to it? we found that there is a clear difference between the most popular songs on Spotify and YouTube, with the top songs on YouTube having more views but not necessarily the most streams on Spotify. Why is that? Is it because YouTube offers more variety, more visuals, or more interaction? Or is it because Spotify users have different tastes, different moods, or different habits? We also found a strong positive correlation between the loudness and energy of a track, indicating that more energetic tracks tend to be more loud. This makes sense, as people often listen to music to boost their mood, express their emotions, or have fun. There was also a negative correlation between energy and acousticness, indicating that as the energy of a track increases, the amount of acoustic instruments decreases. This suggests that electronic music is more popular than acoustic music when it comes to high-energy tracks. Finally, we found that albums are the most popular type of release, with singles and compilations making up a smaller proportion of the releases. This implies that music listeners still value the concept of an album as a coherent artistic expression, rather than just a collection of songs. What do you think? Do you agree with these insights? Do they reflect your own musical preferences and habits? Or do you have a different perspective on music and how to enjoy it? Feel free to share your thoughts and opinions in the comments below.
