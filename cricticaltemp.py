# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def ct_page():
    # Data Imported
    train_Data = pd.read_csv("train.csv")
    unique_m_Data = pd.read_csv("unique_m.csv")

    # Graph of Critical Temperatures
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
        
    histogram("critical_temp", "Critical Temperatures (Celcisus)")
    
    # Calculate Mean
    mean_critical_temp = train_Data["critical_temp"].mean()
    print(f"Critical Temperature Mean {mean_critical_temp}")
    
    # Calculate Standard Devition
    std_critical_temp = train_Data["critical_temp"].std()
    print(f"Critical Temperature Standard Devivation {std_critical_temp}")
    
    # Display
    st.text(f"Critical Temperature Mean: {mean_critical_temp} \nCritical Temperature Standard Deviation: {std_critical_temp}")