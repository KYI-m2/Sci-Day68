import streamlit as st
import streamlit_option_menu
import pandas as pd
with st.sidebar :
  tab = option_menu (
    "Sci-Day",
    ['Home','About Sci-Day','Activities'],
    icon = ['home','book','game']
  )
if tab == 'Home' :
  st.header('Welcome to Sci-Day")
  st.text('ง๗ง')
  st.image("sci.jpg")
if tab == 'About Sci-Day' :
  st.text('deee')
if tab == 'Activities':
