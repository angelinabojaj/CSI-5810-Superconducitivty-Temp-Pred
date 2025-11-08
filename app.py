# Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit implemenation
st.title("CSI 5810: Superconductivity Temperature Prediction App")
st.subheader("Overview of train_data.csv")

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
    
# Graph 1 Feature: Mean Atomic Mass
if "mean_atomic_mass" in train_Data.columns:
    st.subheader("Mean - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["mean_atomic_mass"], bins = 40, color="red")
    ax.set_xlabel("Mean - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Mean Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 2 Feature: Weighted Mean
if "wtd_mean_atomic_mass" in train_Data.columns:
    st.subheader("Weighted Mean - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_mean_atomic_mass"], bins = 40, color="red")
    ax.set_xlabel("Weighted Mean - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Mean Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 3 Feature: Geometric Mean
if "gmean_atomic_mass" in train_Data.columns:
    st.subheader("Geometric Mean - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["gmean_atomic_mass"], bins = 40, color="red")
    ax.set_xlabel("Geometric Mean - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Geometric Mean Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")
    
# Graph 4 Feature: Weighted Geometric Mean
if "wtd_gmean_atomic_mass" in train_Data.columns:
    st.subheader("Weighted Geometric Mean - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_gmean_atomic_mass"], bins = 40, color="red")
    ax.set_xlabel("Weighted Geomtric Mean - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Geometric Mean Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 5 Feature: Entropy
if "entropy_atomic_mass" in train_Data.columns:
    st.subheader("Entropy - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["entropy_atomic_mass"], bins = 40, color="red")
    ax.set_xlabel("Entropy - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Entropy - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 6 Feature:Weighted Entropy
if "wtd_entropy_atomic_mass" in train_Data.columns:
    st.subheader("Weighted Entropy - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_entropy_atomic_mass"], bins = 40, color="red")
    ax.set_xlabel("Weighted Entropy - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Entropy - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 7 Feature:Range
if "range_atomic_mass" in train_Data.columns:
    st.subheader("Range - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["range_atomic_mass"], bins = 40, color="red")
    ax.set_xlabel("Range - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Range - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 8 Feature:Weighted Range
if "wtd_range_atomic_mass" in train_Data.columns:
    st.subheader("Weighted Range - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_range_atomic_mass"], bins = 40, color="red")
    ax.set_xlabel("Weighted Range - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Range - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 9 Feature:Standard Deviation
if "std_atomic_mass" in train_Data.columns:
    st.subheader("Standard Deviation - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_mean_atomic_mass"], bins = 40, color="red")
    ax.set_xlabel("Weighted Mean Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Standard Deviation - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 10 Feature: Weighted Standard Deviation
if "wtd_std_atomic_mass" in train_Data.columns:
    st.subheader("Weighted Standard Deviation - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_std_atomic_mass"], bins = 40, color="red")
    ax.set_xlabel("Weighted Standard Deviation - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Standard Deviation - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# ------------------------------------------------------------------------------------------------ #
# FIE (Orange)
    # Description
    
# Graph 1 Feature: Mean Atomic Mass
if "mean_fie" in train_Data.columns:
    st.subheader("Mean - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["mean_fie"], bins = 40, color="orange")
    ax.set_xlabel("Mean - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Mean Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 2 Feature: Weighted Mean
if "wtd_mean_fie" in train_Data.columns:
    st.subheader("Weighted Mean - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_mean_fie"], bins = 40, color="orange")
    ax.set_xlabel("Weighted Mean - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Mean Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 3 Feature: Geometric Mean
if "gmean_fie" in train_Data.columns:
    st.subheader("Geometric Mean - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["gmean_fie"], bins = 40, color="orange")
    ax.set_xlabel("Geometric Mean - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Geometric Mean Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")
    
# Graph 4 Feature: Weighted Geometric Mean
if "wtd_gmean_fie" in train_Data.columns:
    st.subheader("Weighted Geometric Mean - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_gmean_fie"], bins = 40, color="orange")
    ax.set_xlabel("Weighted Geomtric Mean - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Geometric Mean Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 5 Feature: Entropy
if "entropy_fie" in train_Data.columns:
    st.subheader("Entropy - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["entropy_fie"], bins = 40, color="orange")
    ax.set_xlabel("Entropy - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Entropy - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 6 Feature:Weighted Entropy
if "wtd_entropy_fie" in train_Data.columns:
    st.subheader("Weighted Entropy - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_entropy_fie"], bins = 40, color="orange")
    ax.set_xlabel("Weighted Entropy - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Entropy - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 7 Feature:Range
if "range_fie" in train_Data.columns:
    st.subheader("Range - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["range_fie"], bins = 40, color="orange")
    ax.set_xlabel("Range - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Range - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 8 Feature:Weighted Range
if "wtd_range_fie" in train_Data.columns:
    st.subheader("Weighted Range - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_range_fie"], bins = 40, color="orange")
    ax.set_xlabel("Weighted Range - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Range - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 9 Feature:Standard Deviation
if "std_fie" in train_Data.columns:
    st.subheader("Standard Deviation - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_mean_fie"], bins = 40, color="orange")
    ax.set_xlabel("Weighted Mean Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Standard Deviation - Atomic Mass")
    
    st.pyplot(fig)

else:
    st.error("WRONG")

# Graph 10 Feature: Weighted Standard Deviation
if "wtd_std_fie" in train_Data.columns:
    st.subheader("Weighted Standard Deviation - Atomic Mass")
    fig, ax = plt.subplots()
    ax.hist(train_Data["wtd_std_fie"], bins = 40, color="orange")
    ax.set_xlabel("Weighted Standard Deviation - Atomic Mass")
    ax.set_ylabel("Number of Occurences")
    ax.set_title("Frequency of Weighted Standard Deviation - Atomic Mass")
    
    st.pyplot(fig)


# Atomic Radius
    # Description
    
# Graph 1 Feature: Mean Atomic Mass

# Graph 2 Feature: Weighted Mean

# Graph 3 Feature: Geometric Mean

# Graph 4 Feature: Weighted Geometric Mean

# Graph 5 Feature: Entropy

# Graph 6 Feature:Weighted Entropy

# Graph 7 Feature:Range

# Graph 8 Feature:Weighted Range

# Graph 9 Feature:Standard Deviation

# Graph 10 Feature: Weighted Standard Deviation


# Density
    # Description
    
# Graph 1 Feature: Mean Atomic Mass

# Graph 2 Feature: Weighted Mean

# Graph 3 Feature: Geometric Mean

# Graph 4 Feature: Weighted Geometric Mean

# Graph 5 Feature: Entropy

# Graph 6 Feature:Weighted Entropy

# Graph 7 Feature:Range

# Graph 8 Feature:Weighted Range

# Graph 9 Feature:Standard Deviation

# Graph 10 Feature: Weighted Standard Deviation



# Electron Affininity
    # Description
    
# Graph 1 Feature: Mean Atomic Mass

# Graph 2 Feature: Weighted Mean

# Graph 3 Feature: Geometric Mean

# Graph 4 Feature: Weighted Geometric Mean

# Graph 5 Feature: Entropy

# Graph 6 Feature:Weighted Entropy

# Graph 7 Feature:Range

# Graph 8 Feature:Weighted Range

# Graph 9 Feature:Standard Deviation

# Graph 10 Feature: Weighted Standard Deviation


# Fusion Heat
    # Description
    
# Graph 1 Feature: Mean Atomic Mass

# Graph 2 Feature: Weighted Mean

# Graph 3 Feature: Geometric Mean

# Graph 4 Feature: Weighted Geometric Mean

# Graph 5 Feature: Entropy

# Graph 6 Feature:Weighted Entropy

# Graph 7 Feature:Range

# Graph 8 Feature:Weighted Range

# Graph 9 Feature:Standard Deviation

# Graph 10 Feature: Weighted Standard Deviation


# Thermal Conductivity
    # Description
    
# Graph 1 Feature: Mean Atomic Mass

# Graph 2 Feature: Weighted Mean

# Graph 3 Feature: Geometric Mean

# Graph 4 Feature: Weighted Geometric Mean

# Graph 5 Feature: Entropy

# Graph 6 Feature:Weighted Entropy

# Graph 7 Feature:Range

# Graph 8 Feature:Weighted Range

# Graph 9 Feature:Standard Deviation

# Graph 10 Feature: Weighted Standard Deviation


# Valence
    # Description
    
# Graph 1 Feature: Mean Atomic Mass

# Graph 2 Feature: Weighted Mean

# Graph 3 Feature: Geometric Mean

# Graph 4 Feature: Weighted Geometric Mean

# Graph 5 Feature: Entropy

# Graph 6 Feature:Weighted Entropy

# Graph 7 Feature:Range

# Graph 8 Feature:Weighted Range

# Graph 9 Feature:Standard Deviation

# Graph 10 Feature: Weighted Standard Deviation