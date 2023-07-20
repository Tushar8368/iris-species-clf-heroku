# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'penguin_app.py'.

# Importing the necessary libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Load the DataFrame
csv_file = "https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/penguin.csv"
df = pd.read_csv(csv_file)

# Display the first five rows of the DataFrame
df.head()

# Drop the NAN values
df = df.dropna()

# Add numeric column 'label' to resemble non numeric column 'species'
df['label'] = df['species'].map({'Adelie': 0, 'Chinstrap': 1, 'Gentoo':2})


# Convert the non-numeric column 'sex' to numeric in the DataFrame
df['sex'] = df['sex'].map({'Male':0,'Female':1})

# Convert the non-numeric column 'island' to numeric in the DataFrame
df['island'] = df['island'].map({'Biscoe': 0, 'Dream': 1, 'Torgersen':2})


# Create X and y variables
X = df[['island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex']]
y = df['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 42)


# Build a SVC model using the 'sklearn' module.
svc_model = SVC(kernel = 'linear')
svc_model.fit(X_train, y_train)
svc_score = svc_model.score(X_train, y_train)

# Build a LogisticRegression model using the 'sklearn' module.
log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)
log_reg_score = log_reg.score(X_train, y_train)

# Build a RandomForestClassifier model using the 'sklearn' module.
rf_clf = RandomForestClassifier(n_jobs = -1)
rf_clf.fit(X_train, y_train)
rf_clf_score = rf_clf.score(X_train, y_train)



def prediction(model, island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex):
    
    island_mapping = {'Biscoe': 0, 'Dream': 1, 'Torgersen': 2}

  
    sex_mapping = {'Female': 0, 'Male': 1}

  
    island = island_mapping[island]
    sex = sex_mapping[sex]

   
    features = [[island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex]]

   
    predicted_species = model.predict(features)

    predicted_species = predicted_species[0]

    
    species = ''
    if predicted_species == 0:
        species = 'Adelie'
    elif predicted_species == 1:
        species = 'Chinstrap'
    elif predicted_species == 2:
        species = 'Gentoo'

    return species


st.title("Penguin Species Prediction App")

b_len = st.sidebar.slider("Bill Length", float(df['bill_length_mm'].min()), float(df['bill_length_mm'].max()))
b_dep = st.sidebar.slider("Bill Depth", float(df['bill_depth_mm'].min()), float(df['bill_depth_mm'].max()))
f_len = st.sidebar.slider("Flipper Length", float(df['flipper_length_mm'].min()), float(df['flipper_length_mm'].max()))
b_mass = st.sidebar.slider("Body Mass", float(df['body_mass_g'].min()), float(df['body_mass_g'].max()))

sex = st.sidebar.slider("Sex", float(df['sex'].min()), float(df['sex'].max()))
island = st.sidebar.slider("Island", float(df['island'].min()), float(df['island'].max()))

classifier = st.sidebar.selectbox('Classifier', ('Support Vector Machine', 'Logistic Regression', 'Random Forest Classifier'))

if st.sidebar.button("Predict"):
  if classifier == 'Support Vector Machine':
    species_type = prediction(svc_model, b_len, b_dep, f_len, b_mass, sex, island)
    score = svc_model.score(X_train, y_train)

  elif classifier =='Logistic Regression':
    species_type = prediction(log_reg,  b_len, b_dep, f_len, b_mass, sex, island)
    score = log_reg.score(X_train, y_train)

  else:
    species_type = prediction(rf_clf,  b_len, b_dep, f_len, b_mass, sex, island)
    score = rf_clf.score(X_train, y_train)

    st.write("Species predicted:", species_type)
    st.write("Accuracy score of this model is:", score)    