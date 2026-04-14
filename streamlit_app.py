import streamlit as st

st.title("🏋️ App Gym Caya")

st.write("Bienvenido a tu app de entrenamiento")

peso = st.number_input("Ingresa tu peso (kg):", min_value=0.0)

if peso > 0:
    st.write(f"Tu peso es: {peso} kg")
