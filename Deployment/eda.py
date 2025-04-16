import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Prediksi Nasabah Bank",
    layout="wide",
    initial_sidebar_state="expanded"
)

def run():
    #Membuat Title
    st.title("Nasabah Chrun Prediction")

    # Membuat Sub Header
    st.subheader("Memprediksi apakah seorang nasabah akan keluar")

    #Menambah Gambar
    st.image("https://miro.medium.com/v2/resize:fit:1400/1*47xx1oXuebvYwZeB0OutuA.png")

    # menambah deskrisi
    st.write("Page ini dibuat oleh Naufal")
    st.write("# Header")
    st.write("## Subheader")

    # Menambah garis
    st.markdown("====")

    # Magic Syntax
    """
    Pada page ini penulis akan melakukan explorasi sederhana,
    Dataset yang digunakan adalah Churn Modelling.
    Dataset ini berasal dari web kaggle.com
    """

    # Show Data Frame
    df = pd.read_csv("Churn_Modelling.csv")
    st.dataframe(df)

    # Membuat barplot
    st.write("### Plot NumOfProducts")
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x="NumOfProducts", data=df)
    st.pyplot(fig)

    # Membuat Histogram bedarsarkan input user
    st.write("### Histogram bedasarkan input user")
    pilihan = st.selectbox("Pilih kolom :", ("Age","Gender","Geography"))
    fig = plt.figure(figsize=(15,5))
    sns.histplot(df[pilihan],bins=30,kde=True)
    st.pyplot(fig)

    # Membuat plotly plot
    st.write("Plotly Plot - Gender dan Balance")
    fig = px.scatter(df, x="Gender", y="Balance", hover_data=["Gender","Age"])
    st.plotly_chart(fig)

if __name__=="__main__":
    run()