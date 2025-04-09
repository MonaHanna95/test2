import streamlit as st
import pandas as pd
import io
import csv

# Set page configuration
st.set_page_config(page_title="MyPowerDash ⚡", layout="wide")
st.title("⚡ MyPowerDash – Electricity Consumption Insights")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your electricity usage CSV file", type=["csv"])