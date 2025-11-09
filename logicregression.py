# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def lg_page():
    st.title("Classifer Models")
    
    # Data Imported
    train_Data = pd.read_csv("train.csv")
    unique_m_Data = pd.read_csv("unique_m.csv")

    target = st.selectbox("Selected Target", train_Data.columns)
    feature = st.multiselect("Selected Feature", [col for col in train_Data.columns if col != target])
    
    # KNN Classifer
    
    # Linear Logic Regression Models / Classifer
    
    