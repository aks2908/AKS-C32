import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
st.title('A Sample Dashboard')
uploaded_file = st.file_uploader("Choose a file ",type='csv')
if uploaded_file is not None:
    st.write('File uploaded successfully')
    df = pd.read_csv(uploaded_file)
    st.subheader('Data Preview')
    st.write(df.head())
    st.subheader('Data Statistics')
    st.write(df.describe())
    st.subheader('Filter Data')
    columns = df.columns.to_list()
    selected_column = st.selectbox('Select columns to filter by ',columns)
    unique_values = df[selected_column].unique()
    selected_values = st.selectbox('Select Value',unique_values)
    filtered_df = df[df[selected_column] == selected_values]
    st.write(filtered_df)
    st.subheader('Plot filtered Data')
    x_column = st.selectbox('Select x-axis column',columns)
    y_column = st.selectbox('Select y-axis column', columns)
    if st.button('Generate Plot'):
        st.title("House hold income ~ Exp plot")
        fig = px.line(filtered_df, x=x_column, y=y_column, title="HH Inc ~ Exp plot")
        st.plotly_chart(fig)

else:
    st.write('Waiting for file upload')
    plt.show()