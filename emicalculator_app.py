import streamlit as st

def calculate_emi(p, n, r):
    r = r / 100  
    emi = (p * r * (1 + r)**n) / (((1 + r)**n) - 1)
    return round(emi, 3)

st.title("EMI Calculator")

principal = st.slider("Principal Loan Amount", 1000, 1000000)
tenure = st.slider("Loan period (in years)", 1, 30)
roi = st.slider("Rate of Interest (in % per annum)", 1, 15)


n = tenure * 12
r = roi / 12

if st.button("Calculate EMI"):
    emi = calculate_emi(principal, n, r)
    st.write("EMI:", emi)