#---------------------------------
# Author: OG
# Description: Python script adapted from the hands on snowflake series workshop
# URL: https://omargomez2-first-streamlit-app-streamlit-app-wexxup.streamlit.app/
#---------------------------------

import streamlit
import pandas
import requests
import snowflake.connector
import psycopg2

from urllib.error import URLError

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My new healthy diner spot')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast with blue cheese')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

streamlit.header('Fruityvice Fruit Advice!!!')
#streamlit.text(fruityvice_response.json())
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error('Please select a fruit to get information.')
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      #streamlit.write('The user entered ', fruit_choice)
      #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
      #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      # write your own comment - what does this do?
      streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()


#streamlit.stop()


#Snowflake-related functions
def get_fruit_load_list():
  with conn.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list;")
    #conn.execute("select * from fruit_load_list;")
    return my_cur.fetchall()

#@streamlit.experimental_singleton
def init_connection():
    return psycopg2.connect(**streamlit.secrets["postgres"])

  
streamlit.header("View Our Fruit List - Add Your Favorites!")
# Add a button to load the fruit
if streamlit.button('Get Fruit List'):
  conn = init_connection()
  #my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  conn.close()
  #my_cnx.close()
  streamlit.dataframe(my_data_rows)


def insert_row_snowflake(new_fruit):
  with conn.cursor() as my_cur:
    my_cur.execute("INSERT INTO postgre_capleftus.public.fruit_load_list (fruit_name) VALUES ('hola')")
    streamlit.text("INSERT INTO postgre_capleftus.public.fruit_load_list (fruit_name) VALUES ('hola');")
    #my_cur.execute("insert into postgre_capleftus.public.fruit_load_list (fruit_name) values ('" + new_fruit + "');")
    return "Thanks for adding " + new_fruit

  
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
  conn = init_connection()
  #my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  conn.close()
  streamlit.text(back_from_function)
