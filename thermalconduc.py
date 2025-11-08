# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def thermal_page():
    # Streamlit implemenation
    st.subheader("Atomic Radius Graphs")

    # Data Imported
    train_Data = pd.read_csv("train.csv")
    unique_m_Data = pd.read_csv("unique_m.csv")
     
    def histogram(column, feature):
            if column in train_Data.columns:
                st.subheader(f"{feature}")
                fig, ax = plt.subplots()
                ax.hist(train_Data[column], bins = 40, color="pink")
                ax.set_xlabel(feature)
                ax.set_ylabel("Number of Occurences")
                ax.set_title(f"Frequency of {feature}")
                st.pyplot(fig)
            else:
                st.error("WRONG")
        
    histogram("mean_ThermalConductivity", "Mean - Thermal Conductivity")
    histogram("wtd_mean_ThermalConductivity", "Weighted Mean - Thermal Conductivity")
    histogram("gmean_ThermalConductivity", "Geometric Mean - Thermal Conductivity")
    histogram("wtd_gmean_ThermalConductivity", "Weighted Geometric Mean - Thermal Conductivity")
    histogram("entropy_ThermalConductivity", "Entropy - Thermal Conductivity")
    histogram("wtd_entropy_ThermalConductivity", "Weighted Entropy - Thermal Conductivity")
    histogram("range_ThermalConductivity", "Range - Thermal Conductivity")
    histogram("wtd_range_ThermalConductivity", " Weighted Range - Thermal Conductivity")
    histogram("std_ThermalConductivity", "Standard Deviation - Thermal Conductivity")
    histogram("wtd_std_ThermalConductivity", "Weighted Standard Deviation - Thermal Conductivity")