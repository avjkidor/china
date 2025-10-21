import streamlit as st
import pandas as pd
import plotly.express as px

trade = pd.read_csv('trade_merged.csv')
export = trade[trade['flow_code'] == 'X']
sector_sum = export.groupby("sector")["primary_value"].sum().reset_index()

st.header('Распределение экспорта Китая по секторам экономики')

trade_pie = px.pie(
    sector_sum,
    names='sector',
    values='primary_value',
    hover_data={'primary_value':True},
)

trade_pie.update_traces(textinfo='none', hovertemplate='%{label}: %{percent:.1%}')

st.plotly_chart(trade_pie, use_container_width=True)
