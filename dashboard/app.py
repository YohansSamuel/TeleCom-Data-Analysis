from cProfile import label
from tkinter import PAGES
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
# 
import sys
sys.path.insert(0,'./scripts/')
from user_overview import UserOverview
import user_engagement_dashboard
from data_plots import plot_hist,plot_mult_hist

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
    # plt.figure(figsize=(10,5))
    # sns.barplot(x=top_3_manufacturers.index, y=top_3_manufacturers.values)
    # plt.title('Top 3 Handset Manufacturers', size=14, fontweight="bold")
    # plt.xlabel('Handset Manufacturers', size=13, fontweight="bold") 
    # plt.ylabel('Number of Users', size=13, fontweight="bold")
    # plt.show()

    fig = go.Figure(go.Pie(labels = top_3_manufacturers.index,
    values = top_3_manufacturers.values
    ))
    st.header("Top 3 Handset Manufacturers")
    st.plotly_chart(fig)
# 
def user_engagement_analysis():
    st.title("User Engagement Analysis")
    df = pd.read_csv('./data/user_engagement.csv',index_col=0)
    user_engagement_df = df[['Cluster','Session Frequency','Duration','Total Data Usage']]
    user_engagement_df = user_engagement_df.groupby('Cluster').agg({'Session Frequency':'count',
    'Duration':'sum','Total Data Usage':'sum'})

    col = st.sidebar.selectbox(
        "Select top 10 from", (["Session Frequency", "Duration", "Total Data Usage"]))
    if col == "Sessions_Frequency":
        sessions = df.nlargest(10, "Session Frequency")['Session Frequency']
        return plot_hist(sessions)
    elif col == "Duration":
        duration = df.nlargest(10, "Duration")['Duration']

        return plot_mult_hist([duration], 1, 1, "User Engagement Duration", ['Duration (sec)'])

    else:
        total_data_volume = df.nlargest(
            10, "Total Data Usage")['Total Data Usage']
        
        return plot_mult_hist([total_data_volume], 1, 1, "User Engagement Total Data Usage", ['Total Data Usage (kbps)'])

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

