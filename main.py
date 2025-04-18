import streamlit as st
import pandas as pd
import numpy as np
from collections import defaultdict

# state init
st.session_state.df = pd.DataFrame()
st.session_state.header_list = []
st.session_state.line_chart_data = defaultdict(list)


st.subheader("Upload CSV | Visualize | Analyze")
def load_df():
    if not st.session_state.df.empty:
        st.dataframe(st.session_state.df, height=250, use_container_width=True)
        st.session_state.header_list = [key for key, val in st.session_state.df.dtypes.to_dict().items() if val in ['int64', 'float64']]

col1, col2 = st.columns(2)
with col1:
    uploaded_file = st.file_uploader("Upload a Data File.", type=["csv",])
    if uploaded_file:
        df = pd.read_csv(uploaded_file, index_col=False)
        st.session_state.df = df

with col2:
    if 'df' in st.session_state:
        load_df()
        
# ================= edit section =====================

edit_section = st.expander("Edit Section", expanded=False)
with edit_section:
    st.subheader("Edit Data")
    st.session_state.df = st.data_editor(
        st.session_state.df,
        num_rows="dynamic",
        use_container_width=True,
        key="edit_data",
    )


def create_bar():
    selected_x = st.selectbox("Select Base Column", st.session_state.df.columns, key="bar_x")
    selected_y = st.multiselect("Columns For Bar Chart", st.session_state.header_list, default=[], key="bar_y")
    if selected_x and selected_y:
        chart_data = st.session_state.df.groupby(selected_x)[selected_y].mean().reset_index()
        st.bar_chart(
            chart_data,
            x=selected_x,
            y=selected_y, height=250)
        
def create_line():
    selected_x = st.selectbox("Select Base Column", st.session_state.df.columns, key="line_x")
    selected_y = st.multiselect("Columns For Bar Chart", st.session_state.header_list, default=[], key="line_y")
    if selected_x and selected_y:
        chart_data = st.session_state.df.groupby(selected_x)[selected_y].mean().reset_index()
        st.line_chart(
            chart_data,
            x=selected_x,
            y=selected_y, height=250)
        

with st.container(border=True):
    st.subheader("Analyze | Visualize | Predict")

    tab_bar, tab_line = st.tabs(["Bar Chart", "Line Chart"])

    with tab_bar:
        create_bar()

    with tab_line:
        create_line()


with st.sidebar:
    st.subheader("Data Analysis")
    st.write("This is a simple data visualization app that allows you to upload a CSV file and visualize the data using bar and line charts.")
    st.write("You can select the columns you want to visualize and the app will generate the charts for you.")
    st.write("This app is built using Streamlit, a Python library for building web apps.")
    st.write("You can use this app to quickly visualize your data and gain insights from it.")
    st.write(" Relex We are not storing any data.")




