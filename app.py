
import streamlit as st
import pandas as pd
from PIL import Image 
  
st.set_page_config(page_title = 'Money Fighter', page_icon = ':large_yellow_square:') 


st.title('Money Fighter')
menu = ['Home', 'Stats', 'About']

choice = st.sidebar.selectbox('Menu', menu)
df = pd.read_csv('df_del_nan_v3.csv')

image = Image.open('./pak.jpg') 

if choice == 'Home':
    st.subheader('Home')
    st.table(df.head())
elif choice == 'Stats':
    st.subheader('Stats')
else:
    st.subheader('About')
    descripcion = ('Money Fighter  is a website that predicts the result of the upcoming MMA fights.\
         We take into account thousands of past bouts  and use a complex model to predict the \
         outcome of each fight.\
         Our predictions give you an edge over the bookmakers and other gamblers, \
         as well as insightful data about fighters’ tendencies in different situations. \
         Our predictions are 100% free and we do not accept any payments from the fighters, \
         their managers or promoters. Our goal is to help MMA fans understand the sport better\
         by providing them with valuable information about the upcoming fights.')
   
    st.image(image = image, width=200)
    st.markdown(f'<div style="text-align: justify;">{descripcion}</div>', unsafe_allow_html=True)                          
