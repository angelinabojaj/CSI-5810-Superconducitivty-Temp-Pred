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
# ------------------------------------------------------------------------------------------------ #
# FIE (Orange)
    # Description
    
# Graph 1 Feature: Mean Atomic Mass
if "mean_fie" in train_Data.columns:
    st.subheader("Mean - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["mean_fie"], bins = 40, color="orange")
    ax.set_xlabel("Mean - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Mean Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 2 Feature: Weighted Mean
if "wtd_mean_fie" in train_Data.columns:
    st.subheader("Weighted Mean - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_mean_fie"], bins = 40, color="orange")
    ax.set_xlabel("Weighted Mean - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Mean Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 3 Feature: Geometric Mean
if "gmean_fie" in train_Data.columns:
    st.subheader("Geometric Mean - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["gmean_fie"], bins = 40, color="orange")
    ax.set_xlabel("Geometric Mean - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Geometric Mean Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")
    
# Graph 4 Feature: Weighted Geometric Mean
if "wtd_gmean_fie" in train_Data.columns:
    st.subheader("Weighted Geometric Mean - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_gmean_fie"], bins = 40, color="orange")
    ax.set_xlabel("Weighted Geomtric Mean - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Geometric Mean Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 5 Feature: Entropy
if "entropy_fie" in train_Data.columns:
    st.subheader("Entropy - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["entropy_fie"], bins = 40, color="orange")
    ax.set_xlabel("Entropy - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Entropy - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 6 Feature:Weighted Entropy
if "wtd_entropy_fie" in train_Data.columns:
    st.subheader("Weighted Entropy - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_entropy_fie"], bins = 40, color="orange")
    ax.set_xlabel("Weighted Entropy - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Entropy - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 7 Feature:Range
if "range_fie" in train_Data.columns:
    st.subheader("Range - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["range_fie"], bins = 40, color="orange")
    ax.set_xlabel("Range - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Range - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 8 Feature:Weighted Range
if "wtd_range_fie" in train_Data.columns:
    st.subheader("Weighted Range - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_range_fie"], bins = 40, color="orange")
    ax.set_xlabel("Weighted Range - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Range - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 9 Feature:Standard Deviation
if "std_fie" in train_Data.columns:
    st.subheader("Standard Deviation - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_mean_fie"], bins = 40, color="orange")
    ax.set_xlabel("Weighted Mean Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Standard Deviation - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 10 Feature: Weighted Standard Deviation
if "wtd_std_fie" in train_Data.columns:
    st.subheader("Weighted Standard Deviation - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_std_fie"], bins = 40, color="orange")
    ax.set_xlabel("Weighted Standard Deviation - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Standard Deviation - Atomic Mass")
    
    st.pyplot(fig)
