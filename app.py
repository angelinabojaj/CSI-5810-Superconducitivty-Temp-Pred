# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit implemenation
def home():
    st.title("CSI 5810: Superconductivity Temperature Prediction App")
    st.subheader("Introduction")
    st.set_page_config(initial_sidebar_state="expanded")

def go_mass(): 
    plt.close("all")
    st.session_state.page = "atomicmass"

def go_fie(): 
    plt.close("all")
    st.session_state.page = "fie"

def go_radius(): 
    plt.close("all")
    st.session_state.page = "atomicradius"

def go_density(): 
    plt.close("all")
    st.session_state.page = "density"
    
def go_electron(): 
    plt.close("all")
    st.session_state.page = "electronaffinity"

def go_fusion(): 
    plt.close("all")
    st.session_state.page = "fusionheat"

def go_thermal(): 
    plt.close("all")
    st.session_state.page = "thermalconduc"

def go_valence(): 
    plt.close("all")
    st.session_state.page = "valence"

def go_ct():
    plt.close("all")
    st.session_state.page = "ct"

def go_lg():
    plt.close("all")
    st.session_state.page = "lg"

# Side Bar Navigation
st.sidebar.title("Graphs Broken Down")
st.sidebar.button("Home Page", key = "home", on_click=home)
st.sidebar.button("Atomic Mass", key = "mass", on_click=go_mass)
st.sidebar.button("FIE", key = "fie", on_click=go_fie)
st.sidebar.button("Atomic Radius", key = "radius", on_click=go_radius)
st.sidebar.button("Density", key = "den", on_click=go_density)
st.sidebar.button("Electron Affinity", key = "ea", on_click= go_electron)
st.sidebar.button("Fusion Heat", key = "fus", on_click=go_fusion)
st.sidebar.button("Thermal Conductvitiy", key = "thermal",on_click=go_thermal)
st.sidebar.button("Valence", key = "val", on_click=go_valence)
st.sidebar.button("Critical Temperature", key = "ct", on_click=go_ct)
st.sidebar.button("Logic Regression Graphs", key = "lg", on_click=go_lg)

# Loading Pages
if "page" not in st.session_state:
    home()

elif st.session_state.page == "atomicmass":
    from atomicmass import atomicmass_page
    atomicmass_page()
    
elif st.session_state.page == "fie":
    from fie import fie_page
    fie_page()

elif st.session_state.page == "atomicradius":
    from atomicradius import rad_page
    rad_page()

elif st.session_state.page == "density":
    from density import density_page
    density_page()
    
elif st.session_state.page == "electronaffinity":
    from electronaffinity import electron_page
    electron_page()

elif st.session_state.page == "fusionheat":
    from fusionheat import fusion_page
    fusion_page()
    
elif st.session_state.page == "thermalconduc":
    from thermalconduc import thermal_page
    thermal_page()
    
elif st.session_state.page == "valence":
    from valence import valence_page
    valence_page()

elif st.session_state.page == "ct":
    from cricticaltemp import ct_page
    ct_page()

elif st.session_state.page == "lg":
    from logicregression import lt_page
    lt_page()