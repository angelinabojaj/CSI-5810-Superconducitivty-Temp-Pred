# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit implemenation
st.title("CSI 5810: Superconductivity Temperature Prediction App")
st.subheader("Atomic Mass Graphs")
st.set_page_config(initial_sidebar_state="expanded")

def default():
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
    # Atomic Mass (Red)
        # Description: 
    
    def histogram(column, feature):
        if column in train_Data.columns:
            st.subheader(f"{feature}")
            fig, ax = plt.subplots()
            ax.hist(train_Data[column], bins = 40, color="red")
            ax.set_xlabel(feature)
            ax.set_ylabel("Number of Occurences")
            ax.set_title(f"Frequency of {feature}")
            st.pyplot(fig)
        else:
            st.error("WRONG")
        
    histogram("mean_atomic_mass", "Mean - Atomic Mass")
    histogram("wtd_mean_atomic_mass", "Weighted Mean - Atomic Mass")
    histogram("gmean_atomic_mass", "Geometric Mean - Atomic Mass")
    histogram("wtd_gmean_atomic_mass", "Weighted Geometric Mean - Atomic Mass")
    histogram("entropy_atomic_mass", "Entropy - Atomic Mass")
    histogram("wtd_entropy_atomic_mass", "Weighted Entropy - Atomic Mass")
    histogram("range_atomic_mass", "Range - Atomic Mass")
    histogram("wtd_range_atomic_mass", " Weighted Range Atomic Mass")
    histogram("std_atomic_mass", "Standard Deviation - Atomic Mass")
    histogram("wtd_std_atomic_mass", "Weighted Standard Deviation - Atomic Mass")

default()

def go_mass(): 
    plt.close("all")
    st.session_state.page = "app"

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
    default()

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