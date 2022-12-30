#---------------------------------
# Author: OG
# Description: Python script related to the hands on snowflake series workshop
#---------------

import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My new healthy diner spot')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast with blue cheese')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

straeamlit.dataframe(my_fruit_list)
