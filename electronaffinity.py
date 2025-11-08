# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def electron_page():
    # Streamlit implemenation
    st.subheader("Electron Affinity Graphs")

    # Data Imported
    train_Data = pd.read_csv("train.csv")
    unique_m_Data = pd.read_csv("unique_m.csv")
     
    def histogram(column, feature):
            if column in train_Data.columns:
                st.subheader(f"{feature}")
                fig, ax = plt.subplots()
                ax.hist(train_Data[column], bins = 40, color="blue")
                ax.set_xlabel(feature)
                ax.set_ylabel("Number of Occurences")
                ax.set_title(f"Frequency of {feature}")
                st.pyplot(fig)
            else:
                st.error("WRONG")
        
    histogram("mean_ElectronAffinity", "Mean - Electron Affinity")
    histogram("wtd_mean_ElectronAffinity", "Weighted Mean - Electron Affinity")
    histogram("gmean_ElectronAffinity", "Geometric Mean - Electron Affinity")
    histogram("wtd_gmean_ElectronAffinity", "Weighted Geometric Mean - Electron Affinity")
    histogram("entropy_ElectronAffinity", "Entropy - Electron Affinity")
    histogram("wtd_entropy_ElectronAffinity", "Weighted Entropy - Electron Affinity")
    histogram("range_ElectronAffinity", "Range - Electron Affinity")
    histogram("wtd_range_ElectronAffinity", " Weighted Range - Electron Affinity")
    histogram("std_ElectronAffinity", "Standard Deviation - Electron Affinity")
    histogram("wtd_std_ElectronAffinity", "Weighted Standard Deviation - Electron Affinity")