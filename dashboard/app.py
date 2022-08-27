from tkinter import PAGES
import numpy as np
import pandas as pd
import streamlit as st

def EDA():
    st.title("Exploratory Data Analysis")

def user_overview_analysis():
    st.title("User Overview Analysis")

def user_engagement_analysis():
    st.title("User Engagement Analysis")

def user_experience_analysis():
    st.title("User Experience Analysis")

def user_satisfaction_analysis():
    st.title("User Satisfaction Analysis")
pages = {
    "Exploratory Data Analysis": EDA,
    "User Overview Analysis": user_overview_analysis,
    "User Engagement Analysis": user_engagement_analysis,
    "User Experience Analysis": user_experience_analysis,
    "User Satisfaction Analysis": user_satisfaction_analysis
}

options = st.sidebar.selectbox("TelCo Data Analysis",list(pages.keys()))
pages[options]()