import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("""
# Tips study      
This app is a depiction on various charts derived from tips dataset.
Different statistics are provided below. 
""")

tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
tips.head()

fig = plt.figure(figsize=(8, 4))
axes = fig.add_axes([0, 0, 1, 1])
axes.hist(
    tips['total_bill'],
    bins=12
)
axes.set_title('Total bill histogram')
with st.expander("Total bill histogram"):
    st.pyplot(fig)

fig = plt.figure(figsize=(8, 4))
axes = fig.add_axes([0, 0, 1, 1])
axes.scatter(
    x=tips['total_bill'], 
    y=tips['tip'],
    marker='o',
)
axes.set_title('Tips and total bills')
axes.set_xlabel('Total bill $')
axes.set_ylabel('Tip amount $')
with st.expander("Total bill and tip scatterplot"):
    st.pyplot(fig)

fig = plt.figure(figsize=(8, 4))
axes = fig.add_axes([0, 0, 1, 1])
axes.scatter(
    x=tips['total_bill'], 
    y=tips['tip'],
    marker='o',
    s = (tips['size']**3)*2
)
axes.set_title('Tips and total bills')
axes.set_xlabel('Total bill $')
axes.set_ylabel('Tip amount $')
with st.expander("Total bill and tip size scatterplot"):
    st.pyplot(fig)

avg_day_bills = tips.groupby(by='day')['total_bill'].mean()
fig = plt.figure(figsize=(8,4))
axes = fig.add_axes([0,0,1,1])
axes.bar(avg_day_bills.index,avg_day_bills)
axes.set_title('Average bill by day of week')
axes.set_ylabel('Average bill $')
with st.expander("Avg bill for each day"):
    st.pyplot(fig)

fig = plt.figure(figsize=(8, 4))
axes = fig.add_axes([0, 0, 1, 1])
colormap = ['pink' if x=='Female' else 'lightblue' for x in tips['sex']]
axes.scatter(
    x=tips['tip'], 
    y=tips['day'],
    c = colormap
)
axes.set_title('Tips for different gender and days of the week')
axes.set_xlabel('Tip amount')
with st.expander("Day of week, tip and gender scatterplot"):
    st.pyplot(fig)

total_day_bills = tips.groupby(['day','time'])['total_bill'].sum()
total_day_bills = total_day_bills.unstack().fillna(0)
fig, axes = plt.subplots()
axes.bar(total_day_bills.index,total_day_bills['Dinner']+total_day_bills['Lunch'],width=0.8,label='Dinner')
axes.bar(total_day_bills.index,total_day_bills['Lunch'],width=0.8,label='Lunch')
axes.set_title('Total bills for lunch and dinner')
axes.set_ylabel('Total bill $')
axes.legend()
with st.expander("Total bill (dinner and lunch)"):
    st.pyplot(fig)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 4))
axes[0].hist(tips[tips['time']=='Lunch']['tip'])
axes[1].hist(tips[tips['time']=='Dinner']['tip'])
axes[0].set_title('Lunch tips')
axes[1].set_title('Dinner tips')
axes[0].set_xlabel('$')
axes[1].set_xlabel('$')
with st.expander("Tips from lunch and dinner histograms"):
    st.pyplot(fig)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 4)) 
axes[0].scatter(
    x=tips[(tips['smoker'] == 'Yes') & (tips['sex'] == 'Male')]['total_bill'], 
    y=tips[(tips['smoker'] == 'Yes') & (tips['sex'] == 'Male')]['tip'],
    label = 'Smoking'
)
axes[0].scatter(
    x=tips[(tips['smoker'] == 'No') & (tips['sex'] == 'Male')]['total_bill'], 
    y=tips[(tips['smoker'] == 'No') & (tips['sex'] == 'Male')]['tip'],
    label = 'Non-smoking'
)
axes[1].scatter(
    x=tips[(tips['smoker'] == 'Yes') & (tips['sex'] == 'Female')]['total_bill'], 
    y=tips[(tips['smoker'] == 'Yes') & (tips['sex'] == 'Female')]['tip'],
    label = 'Smoking'
)
axes[1].scatter(
    x=tips[(tips['smoker'] == 'No') & (tips['sex'] == 'Female')]['total_bill'], 
    y=tips[(tips['smoker'] == 'No') & (tips['sex'] == 'Female')]['tip'],
    label = 'Non-smoking'
)
axes[0].set_title('Men')
axes[1].set_title('Women')
axes[0].set_xlabel('Total bill')
axes[0].set_ylabel('Tip')
axes[1].set_xlabel('total bill')
axes[1].set_ylabel('Tip')
axes[0].legend()
with st.expander("Total bill and tip for male/female and smoking/non-smoking guests"):
    st.pyplot(fig)