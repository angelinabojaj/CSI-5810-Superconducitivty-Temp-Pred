# Libraries
import streamlit as st
import pandas as pd

# Streamlit implemenation
st.title("CSI 5810: Superconductivity Temperature Prediction App")

# Data Imported
train_Data = pd.read_csv("train.csv")
unique_m_Data = pd.read_csv("unique_m.csv")

# train.csv
    # Details:
print(train_Data.head())
print("Train Header Column Names:")
print(list(train_Data.columns))

# unique_m.csv
    # Details: 
print(unique_m_Data.head())

# Atomic Mass
# Graph 1 Feature: Mean Atomic Mass


# Graph 2 Feature:

# Graph 3 Feature:

# Graph 4 Feature:

# Graph 5 Feature:

# Graph 6 Feature:

# Graph 7 Feature:

# Graph 8 Feature:

# Graph 9 Feature:

# Graph 10 Feature:

# FIE

# Atomic Radius

# 