import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Look")
uploaded_file = st.file_uploader('Choose a CSV file', type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader('Data Preview')
    st.write(df.head())
    
    st.subheader('Data Summery') 
    st.write(df.describe())
    
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select Value", unique_values)
    
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)
    
    st.subheader("Plot Data")
    x_col = st.selectbox("Select X-axis column", columns)
    y_col = st.selectbox("Select Y-axis column", columns)
    
    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_col)[y_col])
        
else:
    st.write("Waiting for file upload...")        
    
 