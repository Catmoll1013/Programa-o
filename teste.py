import streamlit as st
import pandas as pd
import numpy as np

st.title('Teste cat')

st.write("Tabela")

lista_variavel = [10, 20, 30, 40] 
lista_nomes = ['cat', 'moll', '19', '13/10']

texto = st.text_input("Digite um nome")
variavel = float(st.text_input("Digite a variavel", "0"))
if texto:
    lista_nomes.append(texto)
    lista_variavel.append(variavel)

    dataframe = pd.DataFrame({
        'Nome': lista_nomes,
        'Salário': lista_variavel
    })

    dataframe.style.highlight_max(axis=0)

    st.write(dataframe)

    chart_data = pd.DataFrame(
         np.random.randn(20, 3),
         columns=['a', 'b', 'c'])

    st.bar_chart(chart_data)
