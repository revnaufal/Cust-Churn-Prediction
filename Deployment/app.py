import streamlit as st
import eda as eda
import prediction as prediction

navigation = st.sidebar.selectbox("Pilih Halaman : ", ("EDA", "Predict Nasabah"))
if navigation == "EDA":
    eda.run()
else:
    prediction.run()