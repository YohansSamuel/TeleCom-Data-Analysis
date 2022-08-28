from tkinter import PAGES
import numpy as np
import pandas as pd
import streamlit as st

# 
import sys
sys.path.insert(0,'./scripts/')
from user_overview import UserOverview
import user_engagement_dashboard

#
import seaborn as sns
import matplotlib.pyplot as plt


# displays user overview analysis
def user_overview_analysis():
    st.title("User Overview Analysis")
    
    # original dataset
    st.header('Sample Data from the original dataset')
    df = pd.read_csv("./data/telecom_data_source.csv",index_col=0)
    st.write(df.head(10))

    # cleaned dataset
    st.header('Sample Data from the cleaned dataset')
    df = pd.read_csv("./data/cleaned_telecom_data_source.csv",index_col=0)
    st.write(df.head(10))
    
    # display top 10 handsets used by users
    st.header('Display top 10 handsets used by customers')
    user_ov = UserOverview(df)
    top_10_handsets = user_ov.get_top_handsets(10)
    st.write(top_10_handsets)

    # display top 3 manufacturers
    st.header('Display top 3 handset manufacturers')
    top_3_manufacturers = user_ov.get_top_manufacturers(3)
    st.write(top_3_manufacturers)

    
    # display the top_handsets result in bar graph
    
# 
def user_engagement_analysis():
    st.title("User Engagement Analysis")

# 
def user_experience_analysis():
    st.title("User Experience Analysis")

# 
def user_satisfaction_analysis():
    st.title("User Satisfaction Analysis")


pages = {
    "User Overview Analysis": user_overview_analysis,
    "User Engagement Analysis": user_engagement_analysis,
    "User Experience Analysis": user_experience_analysis,
    "User Satisfaction Analysis": user_satisfaction_analysis
}


options = st.sidebar.selectbox("TelCo Data Analysis",list(pages.keys()))
pages[options]()

