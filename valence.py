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
        
    histogram("mean_Valence", "Mean - Valence")
    histogram("wtd_mean_Valence", "Weighted Mean - Valence")
    histogram("gmean_Valence", "Geometric Mean - Valence")
    histogram("wtd_gmean_Valence", "Weighted Geometric Mean - Valence")
    histogram("entropy_Valence", "Entropy - Valence")
    histogram("wtd_entropy_Valence", "Weighted Entropy - Valence")
    histogram("range_Valence", "Range - Valence")
    histogram("wtd_range_Valence", " Weighted Range - Valence")
    histogram("std_Valence", "Standard Deviation - Valence")
    histogram("wtd_std_Valence", "Weighted Standard Deviation - Valence")