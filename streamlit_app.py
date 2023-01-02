import streamlit as st
import pandas as pd

st.title(' My parents New Healthy Diner')

#streamlit.add('Menu Content')
#st.write('Menu Content')
st.header('Breakfast Menu')
st.header(':mango:')
st.header(':kiwi_fruit:')
st.text('🥣 omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')
st.header(':banana::mango: Build Your Own Fruit Smoothie :kiwi_fruit::grapes:')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
    
