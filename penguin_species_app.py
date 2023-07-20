# Create a function that accepts 'model', island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g' and 'sex' as inputs and returns the species name.
import streamlit as st
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