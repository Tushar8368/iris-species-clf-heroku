# Write the code for creating the Improvised EMI calculator app
import streamlit as st
def calculate_emi(p, n, r):
    r = r / 100 
    emi = (p * r * (1 + r)**n) / (((1 + r)**n) - 1)
    return round(emi, 3)

def calculate_outstanding_balance(p, n, r, m):
    r = r / 100  
    balance = (p * ((1 + r)**n) - ((1 + r)**m)) / (((1 + r)**n) - 1)
    return round(balance, 3)

st.title("Improved EMI Calculator")

principal = st.slider("Principal Loan Amount", 1000, 1000000)
tenure = st.slider("Loan period (in years)", 1, 30)
roi = st.slider("Rate of Interest (in % per annum)", 1, 15)
period = st.slider("Period after which Outstanding Loan Balance is calculated (in months)", 1, tenure * 12)

n = tenure * 12
r = roi / 12

if st.button("Calculate EMI"):
    emi = calculate_emi(principal, n, r)
    st.write("Monthly EMI:", emi)

if st.button("Calculate Outstanding Loan Balance"):
    balance = calculate_outstanding_balance(principal, n, r, period)
    st.write("Outstanding Loan Balance:", balance)