import streamlit as st
import pandas as pd
import requests as r
import snowflake.connector as sc
from urllib.error import URLError

st.title(' My Mom`s New Healthy Diner')

#streamlit.add('Menu Content')
#st.write('Menu Content')
st.header('Breakfast Favourites')
st.text('🥣 omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)
    
# Create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = r.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
    
# New Section to display fruitvice api response
st.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = st.text_input('What fruit would you like information about?')
    if not fruit_choice:
        st.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        st.dataframe(back_from_function)

except URLError as e:
    st.error()
#don't run anything past here while we troubleshoot
#st.stop()
st.header("The Fruit Load list Contains:")
#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * FROM FRUIT_LOAD_LIST")
        return my_cur.fetchall()
        
# Add a button to load the fruit
if st.button('Get Fruit Load List'):
    my_cnx = sc.connect(**st.secrets["snowflake"])
    my_cur = my_cnx.cursor()
    my_data_row = get_fruit_load_list()
    st.dataframe(my_data_rows)
st.stop()
add_my_fruit = st.text_input('What fruit would you like to add?','Kiwi')
st.write('Thanks for adding ', add_my_fruit)

#This will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values ('from Streamlit')")
