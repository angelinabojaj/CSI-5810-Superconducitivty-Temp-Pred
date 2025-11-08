# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit implemenation
st.title("CSI 5810: Superconductivity Temperature Prediction App")
st.subheader("Atomic Mass Graphs")

def go_mass(): 
    st.session_state.page = "app.py"

def go_fie(): 
    st.session_state.page = "fie.py"

def go_radius(): 
    st.session_state.page = "atomicradius.py"

def go_density(): 
    st.session_state.page = "density.py"

def go_electron(): 
    st.session_state.page = "electronaffinity.py"

def go_fusion(): 
    st.session_state.page = "fusionheat.py"

def go_thermal(): 
    st.session_state.page = "thermalconduc.py"

def go_valence(): 
    st.session_state.page = "valence.py"

# Side Bar Navigation
st.sidebar.title("Graphs Broken Down")
st.sidebar.button("Atomic Mass", key = "mass", on_click="app")
st.sidebar.button("FIE", key = "fie", on_click="fie")
st.sidebar.button("Atomic Radius", key = "radius", on_click= "atomicradius")
st.sidebar.button("Density", key = "den")
st.sidebar.button("Electron Affinity", key = "ea")
st.sidebar.button("Fusion Heat", key = "fus")
st.sidebar.button("Thermal Conductvitiy", key = "thermal")
st.sidebar.button("Valence", key = "val")
st.sidebar.button("Logic Regression Graphs")

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

# ------------------------------------------------------------------------------------------------ #
# Atomic Radius (Yellow)
    # Description
    
# Graph 1 Feature: Mean Atomic Mass

# Graph 2 Feature: Weighted Mean

# Graph 3 Feature: Geometric Mean

# Graph 4 Feature: Weighted Geometric Mean

# Graph 5 Feature: Entropy

# Graph 6 Feature:Weighted Entropy

# Graph 7 Feature:Range

# Graph 8 Feature:Weighted Range

# Graph 9 Feature:Standard Deviation

# Graph 10 Feature: Weighted Standard Deviation


# ------------------------------------------------------------------------------------------------ #