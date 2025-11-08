# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def valence_page():
    # Streamlit implemenation
    st.subheader("Atomic Radius Graphs")

    # Data Imported
    train_Data = pd.read_csv("train.csv")
    unique_m_Data = pd.read_csv("unique_m.csv")
     
    def histogram(column, feature):
            if column in train_Data.columns:
                st.subheader(f"{feature}")
                fig, ax = plt.subplots()
                ax.hist(train_Data[column], bins = 40, color="brown")
                ax.set_xlabel(feature)
                ax.set_ylabel("Number of Occurences")
                ax.set_title(f"Frequency of {feature}")
                st.pyplot(fig)
            else:
                st.error("WRONG")
        
    histogram("mean_fie", "Mean - FIE")
    histogram("wtd_mean_atomic_mass", "Weighted Mean - FIE")
    histogram("gmean_fie", "Geometric Mean - FIE")
    histogram("wtd_gmean_fie", "Weighted Geometric Mean - FIE")
    histogram("entropy_fie", "Entropy - FIE")
    histogram("wtd_entropy_fie", "Weighted Entropy - FIE")
    histogram("range_fie", "Range - FIE")
    histogram("wtd_range_fie", " Weighted Range - FIE")
    histogram("std_fie", "Standard Deviation - FIE")
    histogram("wtd_std_fie", "Weighted Standard Deviation - FIE")