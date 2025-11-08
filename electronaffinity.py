# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit implemenation
st.title("CSI 5810: Superconductivity Temperature Prediction App")
st.subheader("Atomic Mass Graphs")

# Side Bar Navigation
st.sidebar.title("Graphs Broken Down")
st.set_page_config(initial_sidebar_state="expanded")

# def go_mass(): st.session_state.page = "app"
st.sidebar.button("Atomic Mass", key = "mass", on_click="app")
st.session_state.page = "app"

# def go_fie(): st.session_state.page = "fie"
st.sidebar.button("FIE", key = "fie", on_click="fie")
st.session_state.page = "fie"

# def go_radius(): st.session_state.page = "atomicradius"
st.sidebar.button("Atomic Radius", key = "radius", on_click= "atomicradius")
st.session_state.page = "atomicradius"

# def go_density(): st.session_state.page = "density"
st.sidebar.button("Density", key = "den")
st.session_state.page =  "density"

# def go_electron(): st.session_state.page = "electronaffinity"
st.sidebar.button("Electron Affinity", key = "ea")
st.session_state.page = "electronaffinity"

# def go_fusion(): st.session_state.page = "fusionheat"
st.sidebar.button("Fusion Heat", key = "fus")
st.session_state. page = "fusionheat"

# def go_thermal(): st.session_state.page = "thermalconduc"
st.sidebar.button("Thermal Conductvitiy", key = "thermal")
st.session_state.page = "thermalconduc"

# def go_valence(): st.session_state.page = "valence"
st.sidebar.button("Valence", key = "val")
st.session_state.page = "valence"

st.sidebar.button("Logic Regression Graphs")

# Data Imported
train_Data = pd.read_csv("train.csv")
unique_m_Data = pd.read_csv("unique_m.csv")
# Electron Affininity (Blue)
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