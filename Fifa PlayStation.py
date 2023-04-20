import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[3]:


fifa = pd.read_csv("fifa_data.csv")
fifa


# In[25]:


plt.hist(fifa.Overall)

plt.show()


# In[26]:


bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(fifa.Overall, bins=bins)

plt.show()


# In[27]:


bins = [0,10,20,30,40,50,60,70,80,90,100]
plt.hist(fifa.Overall, bins=bins)
plt.xticks(bins)
plt.show()


# In[29]:


bins = [40,50,60,70,80,90,100]
plt.hist(fifa.Overall, bins=bins)
plt.xticks(bins)
plt.show()


# In[162]:


bins = [40,50,60,70,80,90,100,110]
plt.hist(fifa.Overall, bins=bins, color="#fc03a5")
plt.xticks(bins)

plt.ylabel("Number of Players")
plt.xlabel("Skill Level")
plt.title("Distribution of Players in FIFA 2018")
plt.show()


# In[161]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fifa = pd.read_csv("fifa_data.csv")

bins = [40,50,60,70,80,90,100,110]
plt.hist(fifa.Overall, bins=bins, color="#fc8c03")
plt.xticks(bins)

plt.ylabel("Number of Players")
plt.xlabel("Skill Level")
plt.title("Distribution of Players in FIFA 2018")
plt.show()


# In[43]:


fifa.head(5)


# In[44]:


fifa["Preferred Foot"]


# PieCharts

# In[60]:


left = fifa.loc[fifa["Preferred Foot"]== "Left"].count()[0]
right = fifa.loc[fifa["Preferred Foot"]== "Right"].count()[0]
labels = ["Left Foot", "Right Foot"]
colors=["#eb5e34", "#0dd690"]
plt.pie([left, right], labels=labels, colors=colors, autopct=""%.2f")


plt.show()


# In[63]:


left = fifa.loc[fifa["Preferred Foot"]== "Left"].count()[0]
right = fifa.loc[fifa["Preferred Foot"]== "Right"].count()[0]
labels = ["Left Foot", "Right Foot"]
colors=["#eb5e34", "#0dd690"]
plt.pie([left, right], labels=labels, colors=colors, autopct="%.2f")


plt.show()


# In[4]:


left = fifa.loc[fifa["Preferred Foot"]== "Left"].count()[0]
right = fifa.loc[fifa["Preferred Foot"]== "Right"].count()[0]
labels = ["Left Foot", "Right Foot"]
colors=["#eb5e34", "#0dd690"]
plt.pie([left, right], labels=labels, colors=colors, autopct="%.f %%")

plt.title("Foot Preference of FIFA Players")
plt.show()


# In[38]:


age_30_above = fifa.loc[fifa["Age"]>= 30].count()[0]
age_30_below = fifa.loc[fifa["Age"]<= 30].count()[0]
labels = ["age_30_above", "age_30_below"]
colors=["#eb5e34", "#0dd690"]
plt.pie([age_30_above, age_30_below], labels=labels, colors=colors, autopct="%.f %%")
plt.title("Age Difference of FIFA Players")
plt.show()


# In[33]:


fifa.Weight


# In[36]:


fifa.Weight=[x.strip("lbs") if type(x) == str else x for x in fifa.Weight]
fifa.Weight


# In[59]:


fifa.Weight=[x.strip("lbs") if type(x) == str else x for x in fifa.Weight]
fifa.Weight[0]


# In[60]:


fifa.Weight=[int(x.strip("lbs")) if type(x) == str else x for x in fifa.Weight]
fifa.Weight[0]


# In[70]:


plt.figure(figsize=(8,5), dpi=100)

plt.style.use('ggplot')

fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]

light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
medium = fifa[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
heavy = fifa[fifa.Weight >= 200].count()[0]

weights = [light,light_medium, medium, medium_heavy, heavy]
label = ['under 125', '125-150', '150-175', '175-200', 'over 200']
explode = (.4,.2,0,0,.4)

plt.title('Weight of Professional Soccer Players (lbs)')

plt.pie(weights, labels=label, explode=explode, pctdistance=0.8,autopct='%.2f %%')
plt.show()


# In[4]:


fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]

light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
medium = fifa[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
heavy = fifa[fifa.Weight >= 200].count()[0]

plt.show()


# In[158]:


fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]

light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
medium = fifa[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
heavy = fifa[fifa.Weight >= 200].count()[0]

weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ["Under 125", "125-150", "150-170", "175-200", "Over 200"]
plt.pie(weights, labels=labels)
plt.show()


# In[94]:


fifa.Weight = [int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]

plt.style.use("ggplot")

light = fifa.loc[fifa.Weight < 125].count()[0]
light_medium = fifa[(fifa.Weight >= 125) & (fifa.Weight < 150)].count()[0]
medium = fifa[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa[(fifa.Weight >= 175) & (fifa.Weight < 200)].count()[0]
heavy = fifa[fifa.Weight >= 200].count()[0]

weights = [light, light_medium, medium, medium_heavy, heavy]
labels = ["Under 125", "125-150", "150-170", "175-200", "Over 200"]
plt.title("Weight Distribution of FIFA Players (in lbs)")
plt.pie(weights, labels=labels, autopct="%.2f%%", pctdistance=0.8, explode=explode)
plt.show()


# In[157]:


age_30_above = fifa.loc[fifa["Age"]>= 30].count()[0]
age_30_below = fifa.loc[fifa["Age"]<= 30].count()[0]
labels = ["age_30_above", "age_30_below"]
colors=["#eb5e34", "#0dd690"]
plt.pie([age_30_above, age_30_below], labels=labels, colors=colors, autopct="%.f %%")
plt.title("Age Difference of FIFA Players")
plt.show()


# In[5]:


fc_barcelona = fifa.loc[fifa.Club == "Barcelona"].count()[0]
fc_barcelona


# In[120]:


fifa


# In[6]:


plt.style.use("default")


barcelona = fifa.loc[fifa.Club == "FC Barcelona"]['Overall']
real_madrid = fifa.loc[fifa.Club == "Real Madrid"]['Overall']
man_city = fifa.loc[fifa.Club == "Manchester City"]['Overall']
trelleborgs_ff = fifa.loc[fifa.Club == "Trelleborgs FF"]['Overall']


labels = "FC Barcelona", "Real Madrid", "Manchester City", "Trelleborgs FF"


boxes = plt.boxplot ([barcelona, real_madrid, man_city, trelleborgs_ff], labels=labels, patch_artist=True, medianprops={'linewidth': 2})

for box in boxes['boxes']:
    box.set(color="#4286f4", linewidth=2)
    
    
plt.title("Professional Football Team Comparison")
plt.ylabel("FIFA Overall Rating")
plt.xlabel("Clubs")
plt.show()


# In[ ]:




