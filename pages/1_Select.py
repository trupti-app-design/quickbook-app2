# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import streamlit as st
import datetime


st.title ("Profit & Loss Report")
st.header("Quickbooks Profit & Loss")

if "report_result" not in st.session_state:
    st.session_state["report_result"] = ""
if "value_result" not in st.session_state:
    st.session_state["value_result"] = ""
if "min_selection" not in st.session_state:
    st.session_state["min_selection"] = ""
if "max_selection" not in st.session_state:
    st.session_state["max_selection"] = ""



Report_list=["Custom","Today","This Fiscal Year"]
Value_list=["All","Active","Non-Zero"]


report_result=st.selectbox("Select Report Period",Report_list)
value_result=st.selectbox("Select Values",Value_list)


min_date = datetime.datetime(2020,1,1)
max_date = datetime.date(2022,1,1)
min_selection=st.date_input("Select a date",(min_date))
max_selection=st.date_input("Select a date",(max_date))

submit=st.button("Submit")

if submit:
    st.session_state["report_result"] = report_result
    st.session_state["value_result"] = value_result
    st.session_state["min_selection"] = min_selection
    st.session_state["max_selection"] = max_selection

