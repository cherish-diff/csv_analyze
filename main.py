import streamlit as st
import pandas as pd
import numpy as np
from collections import defaultdict

# state init
st.session_state.df = pd.DataFrame()
st.session_state.header_list = []
st.session_state.line_chart_data = defaultdict(list)


st.write("Data visualization | Upload CSV and Visualize | Simple")
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

    if 'df' in st.session_state:
        load_df()
    

with col2:
    with st.container(border=True):
       st.session_state.line_chart_data['x_selected_col'] = st.selectbox("Select Base Column", st.session_state.df.columns)
       st.session_state.line_chart_data['y_selected_cols'] = st.multiselect("Columns For Line Chart", st.session_state.header_list, default=[])
    
       
    if st.session_state.line_chart_data['y_selected_cols'] and st.session_state.line_chart_data['x_selected_col']:
        # x wise y avrage
        chart_data = st.session_state.df.groupby(st.session_state.line_chart_data['x_selected_col'])[st.session_state.line_chart_data['y_selected_cols']].mean().reset_index()
        st.line_chart(
            chart_data,
            x=st.session_state.line_chart_data['x_selected_col'],
            y=st.session_state.line_chart_data['y_selected_cols'], height=250)