import streamlit as st
import numpy as np
import pandas as pd
import pickle
import json



# Load Model

with open('num_cols.txt', 'r') as file_1:
  num_cols = json.load(file_1)

with open('cat_cols.txt', 'r') as file_2:
  cat_cols = json.load(file_2)

with open('best_rf_model.pkl', 'rb') as file_3:
  best_rf_model = pickle.load(file_3)

  def run():
    #Membuat Title
        st.title("Prediksi Nasabah")
    # Membuat form
        with st.form(key='form parameter'):
          age = st.number_input("Age", min_value=18, max_value=92, value=20, step=1, help="Usia Nasabah")
          tenor = st.slider("Tenure", 0, 10, 6)
          balance = st.number_input("Balance", 0, 250000, 100000)
          salary = st.number_input("EstimatedSalary", 12, 200000, 100000)
          cscore = st.number_input("CreditScore", 350, 850, 400)
          st.markdown("====")

          geo = st.selectbox("Geography", ("Spain", "France", "Germany"), index=1)
          gen = st.selectbox("Gender", ("Male", "Female"), index=1)
          st.markdown("====")

          nop = st.number_input("NumOfProducts", 0, 4, 0)
          hcc = st.number_input("HasCrCard", 0, 1, 0)
          iam = st.number_input("IsActiveMember", 0, 1, 0)

          submitted = st.form_submit_button("Predict")
    
        data_inf = {
        'CreditScore': cscore,
        'Geography': geo,
        'Gender': gen,
        'Age': age,
        'Tenure': tenor,
        'Balance': balance,
        'NumOfProducts': nop,
        'HasCrCard': hcc,
        'IsActiveMember': iam,
        'EstimatedSalary': salary}

        data_inf = pd.DataFrame([data_inf])
        st.dataframe(data_inf)

        if submitted:
           #Split columns
           data_inf_num = data_inf[num_cols]
           data_inf_cat = data_inf[cat_cols]

           # Concat
           data_final = np.concatenate([data_inf_num, data_inf_cat], axis = 1)

          # Mengonversi hasil concatenate menjadi DataFrame dengan nama kolom
           data_final = pd.DataFrame(data_final, columns=num_cols + cat_cols)

           # Predict
           y_pred = best_rf_model.predict(data_final)
           churn_labels = []
           for pred in y_pred:
              if pred == 1:
                churn_labels.append('Churn')
              else:
                churn_labels.append('Tidak Churn')

              st.write("# Prediksi : ", str(churn_labels))

if __name__=="__main__":
    run()