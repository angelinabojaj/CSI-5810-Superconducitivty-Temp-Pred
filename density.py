# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit implemenation
st.title("CSI 5810: Superconductivity Temperature Prediction App")
st.subheader("Atomic Mass Graphs")

def density_page():
    # Streamlit implemenation
    st.subheader("Density Graphs")

    # Data Imported
    train_Data = pd.read_csv("train.csv")
    unique_m_Data = pd.read_csv("unique_m.csv")
     
    def histogram(column, feature):
            if column in train_Data.columns:
                st.subheader(f"{feature}")
                fig, ax = plt.subplots()
                ax.hist(train_Data[column], bins = 40, color="green")
                ax.set_xlabel(feature)
                ax.set_ylabel("Number of Occurences")
                ax.set_title(f"Frequency of {feature}")
                st.pyplot(fig)
            else:
                st.error("WRONG")
        
    histogram("mean_Density", "Mean - Density")
    histogram("wtd_mean_Density", "Weighted Mean - Density")
    histogram("gmean_Density", "Geometric Mean - Density")
    histogram("wtd_gmean_Density", "Weighted Geometric Mean - Density")
    histogram("entropy_Density", "Entropy - Density")
    histogram("wtd_entropy_Density", "Weighted Entropy - Density")
    histogram("range_Density", "Range - Density")
    histogram("wtd_range_Density", " Weighted Range - Density")
    histogram("std_Density", "Standard Deviation - Density")
    histogram("wtd_std_Density", "Weighted Standard Deviation - Density")