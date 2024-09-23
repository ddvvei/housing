import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


st.title('California Housing Data(1990) by Danying Wei')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
price_filter = st.slider('Minimal Median House Price', 0, 500001, 200000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults


income_level = st.sidebar.radio(
    "Select income level:"
    ('Low','Medium','High')
)


if income_level == 'Low':
    filter_df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium':
    filter_df = df[(df['median_income'] > 2.5) &(df['median_income'] < 4.5)]
else:
    filter_df = df[df['median_income'] > 4.5]


df = df[df.median_house_value >= price_filter]
df = df[df.ocean_proximity.isin(location_filter)]

# show on map
st.subheader('See more filters in the sidebar:')
st.map(df)

# show the plot
# show the plot
st.subheader('Median house value')
fig, ax = plt.subplots(figsize=(10, 5))
plt.style.use("seaborn-v0_8")

# Filter the dataframe for the histogram based on the slider value
filtered_df = df[df.median_house_value >= price_filter]
filtered_df.median_house_value.hist(bins=30, ax=ax)
st.pyplot(fig)