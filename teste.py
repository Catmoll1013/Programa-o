import streamlit as st
import pandas as pd
import numpy as np

st.title('Teste cat - datas')

st.write("Tabela")

lista_data = [13, 1, 30, 20] 
lista_nomes = ['niver cat', 'ano novo', 'corpus cristi', 'dia da amizade']

texto = st.text_input("Digite o nome do feriadob/evento")
data = float(st.text_input("Digite a data (apenas o dia)", "0"))
if texto:
    lista_nomes.append(texto)
    lista_data.append(data)

    dataframe = pd.DataFrame({
        'Nome': lista_nomes,
        'Data': lista_data
    })

    dataframe.style.highlight_max(axis=0)

    st.write(dataframe)

    chart_data = pd.DataFrame(
         np.random.randn(20, 3),
         columns=['a', 'b', 'c'])

    st.bar_chart(chart_data)
