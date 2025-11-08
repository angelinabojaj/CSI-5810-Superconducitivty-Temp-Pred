# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def atomicmass_page():
    # Streamlit
    st.subheader("Atomic Mass Graphs")

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