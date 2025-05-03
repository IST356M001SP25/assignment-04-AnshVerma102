'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

st.title("UniBrow")
st.caption("The Universal data browser")


st.write("This is a simple data browser that allows you to load and view data files.")
st.write("You can load CSV, Excel, and JSON files.")


file = st.file_uploader("Upload a file", type=["csv", "xlsx", "json"])
output = st.empty()
if file is not None:
   ext = pl.get_file_extension(file.name)
   df = pl.load_file(file, ext)
   if df is not None:
       st.write("Data loaded successfully!")
       st.dataframe(df)
       cols = pl.get_column_names(df)
       st.write(f"Columns: {cols}")
       cols = pl.get_columns_of_type(df, 'object')
       st.write(f"Object Columns: {cols}")
       cols = pl.get_columns_of_type(df, 'int64')
       st.write(f"Int64 Columns: {cols}")
       cols = pl.get_columns_of_type(df, 'float64')
       st.write(f"Float64 Columns: {cols}")
       unique = pl.get_unique_values(df, 'state')
       st.write(f"Unique States: {unique}")
   else:
       st.write("Failed to load data.")

