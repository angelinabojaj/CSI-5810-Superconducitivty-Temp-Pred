# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit implemenation
st.title("CSI 5810: Superconductivity Temperature Prediction App")
st.subheader("Atomic Radius Graphs")


def rad_page():
   # Streamlit implemenation
    st.subheader("Atomic Radius Graphs")

    # Data Imported
    train_Data = pd.read_csv("train.csv")
    unique_m_Data = pd.read_csv("unique_m.csv")
     
    def histogram(column, feature):
            if column in train_Data.columns:
                st.subheader(f"{feature}")
                fig, ax = plt.subplots()
                ax.hist(train_Data[column], bins = 40, color="yellow")
                ax.set_xlabel(feature)
                ax.set_ylabel("Number of Occurences")
                ax.set_title(f"Frequency of {feature}")
                st.pyplot(fig)
            else:
                st.error("WRONG")
        
    histogram("mean_atomic_radius", "Mean - Atomic Radius")
    histogram("wtd_mean_atomic_radius", "Weighted Mean - Atomic Radius")
    histogram("gmean_atomic_radius", "Geometric Mean - Atomic Radius")
    histogram("wtd_gmean_atomic_radius", "Weighted Geometric Mean - Atomic Radius")
    histogram("entropy_atomic_radius", "Entropy - Atomic Radius")
    histogram("wtd_entropy_atomic_radius", "Weighted Entropy - Atomic Radius")
    histogram("range_atomic_radius", "Range - Atomic Radius")
    histogram("wtd_range_atomic_radius", " Weighted Range - Atomic Radius")
    histogram("std_atomic_radius", "Standard Deviation - Atomic Radius")
    histogram("wtd_std_atomic_radius", "Weighted Standard Deviation - Atomic Radius")