# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def fusion_page():
    # Streamlit implemenation
    st.subheader("Atomic Radius Graphs")

    # Data Imported
    train_Data = pd.read_csv("train.csv")
    unique_m_Data = pd.read_csv("unique_m.csv")
     
    def histogram(column, feature):
            if column in train_Data.columns:
                st.subheader(f"{feature}")
                fig, ax = plt.subplots()
                ax.hist(train_Data[column], bins = 40, color="purple")
                ax.set_xlabel(feature)
                ax.set_ylabel("Number of Occurences")
                ax.set_title(f"Frequency of {feature}")
                st.pyplot(fig)
            else:
                st.error("WRONG")
        
    histogram("mean_FusionHeat", "Mean - Fusion Heat")
    histogram("wtd_mean_FusionHeat", "Weighted Mean - Fusion Heat")
    histogram("gmean_FusionHeat", "Geometric Mean - Fusion Heat")
    histogram("wtd_gmean_FusionHeat", "Weighted Geometric Mean - Fusion Heat")
    histogram("entropy_FusionHeat", "Entropy - Fusion Heat")
    histogram("wtd_entropy_FusionHeat", "Weighted Entropy - Fusion Heat")
    histogram("range_FusionHeat", "Range - Fusion Heat")
    histogram("wtd_range_FusionHeat", " Weighted Range - Fusion Heat")
    histogram("std_FusionHeat", "Standard Deviation - Fusion Heat")
    histogram("wtd_std_FusionHeat", "Weighted Standard Deviation - Fusion Heat")