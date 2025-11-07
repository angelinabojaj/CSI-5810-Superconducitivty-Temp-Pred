# Libraries
from ucimlrepo import fetch_ucirepo 

# Predict Temperature Project
# By Angelina Bojaj

# Platform Used: Streamlit (pip install streamlit, #streamlit hello)
    # Reference: https://streamlit.io/#install

# Data Imported
# pip install ucimlrepo
superconductivty_data = fetch_ucirepo(id=464) 
  
# data (as pandas dataframes) 
X = superconductivty_data.data.features 
y = superconductivty_data.data.targets 
  
# metadata 
# print(superconductivty_data.metadata) 
# variable information 
# print(superconductivty_data.variables) 

# Features & Target
data_Copy = X.copy
data_Copy['target'] = y

# Graph 1: Features vs Nonfeatures

# Graph 2: Integers vs Other Variables

