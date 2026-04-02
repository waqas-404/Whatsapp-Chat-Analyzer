import streamlit as st
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import preprocessor
import helper

st.sidebar.title("WhatsApp Chat Analyzer")

st.set_page_config(layout="wide")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    data = preprocessor.preprocess(data)
    
    
    st.title("Top Statistics")

    user_list = data['users'].unique().tolist()
    user_list.remove('Group Notification')
    user_list.sort()
    user_list.insert(0,"Overall")
    
    selected_user = st.sidebar.selectbox("Show analysis wrt: ",user_list)  
    
    if st.sidebar.button("Show Analysis"):
        
        num_messages, num_words, num_media , num_links = helper.fetch_sats(selected_user, data)
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.header('Total Messages')       
            st.header(num_messages)

        with col2:
            st.header('Number of Words')
            st.header(num_words)

        with col3:
            st.header('Media shared')
        
            st.header(num_media)
            
        with col4:
            st.header('Links shared')
            st.header(num_links)
            
            
# Monthly timeline

        timeline = helper.monthly_timeline(selected_user, data)
        
        fig, ax = plt.subplots()
        ax.plot(timeline['time'],timeline['messages'], color='green')
        plt.xticks(rotation='vertical')
        st.title('Monthly timeline')
        st.pyplot(fig)

# daily timeline

        st.title('Daily Timeline')
        
        daily_timeline = helper.daily_timeline(selected_user, data)
        fig, ax = plt.subplots()
        
        ax.plot(daily_timeline['only_date'],daily_timeline['messages'], color='green')
        plt.xticks(rotation='vertical')
        plt.figure(figsize=(23,10))
        st.pyplot(fig)
        
        
# daily activity map
        col1, col2 = st.columns(2)
        with col1:
            daily_activity_map = helper.daily_activity_map(selected_user, data)
            fig, ax = plt.subplots()
            ax.bar(daily_activity_map.index, daily_activity_map.values)
            plt.xticks(rotation='vertical')
            st.title("Daily Activity Map")
            st.pyplot(fig)
 
# Monthly Activity Map       
        with col2:
            monthly_activity_map = helper.monthly_activity_map(selected_user, data)
            fig, ax = plt.subplots()
            ax.bar(monthly_activity_map.index, monthly_activity_map.values, color='orange')
            plt.xticks(rotation='vertical')
            st.title("Monthly Activity Map")
            st.pyplot(fig)
            
        st.title("Weekly Activity Map")
        user_heatmap = helper.activity_heatmap(selected_user, data)

        if user_heatmap.empty:
            st.warning("No activity heatmap data available for this selection.")
        else:
            fig, ax = plt.subplots()
            sns.heatmap(user_heatmap, ax=ax)
            st.pyplot(fig)
        

# most busy users
        if selected_user == 'Overall':
            st.header("Most busy users:")
            name, count, new_df = helper.most_busy_users(data)
            col3, col2 = st.columns(2)
            with col3:
                
                fig, ax = plt.subplots()
                ax.bar(name, count)
                
                plt.xticks(rotation = 'vertical')
                st.pyplot(fig)
            
            with col2:
                st.dataframe(new_df)
                
                
# Create WordCloud
        st.title("WordCloud")
        df_wc = helper.create_worldcloud(selected_user, data)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        
# Most common words
        new_df = helper.most_common_words(selected_user, data)
        fig, ax = plt.subplots()
        ax.barh(new_df[0],new_df[1])
        plt.xticks(rotation='vertical')
        
        st.title("Most common words")
        st.pyplot(fig)
        
#Emoji Analysis

        emoji_df = helper.emoji_helper(selected_user, data)
        st.title("Emoji Analysis")
        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(emoji_df)
            
        with col2:
            fig, ax = plt.subplots()
            ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(), autopct='%0.2f')   
            st.pyplot(fig)
        
            

        
        