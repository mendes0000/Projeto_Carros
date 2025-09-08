import streamlit as st

# python -m streamlit run app.py

# ------------------------------------------------- Sidebar

st.sidebar.image("logo.png")
st.sidebar.title('Motorshop')


carros = ['supra','ferrari','nissan', 'Porsche', 'maquina de misterio', 'ix35']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)



# ----------------------------------------------- Principal 
st.title('nickolas - Aluguel de Carros')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

if opcao == 'supra':
    diaria = 950

elif opcao == 'ferrari':
    diaria = 620

elif opcao == 'maquina de misterio':
    diaria = 350

elif opcao == 'nissan':
    diaria = 1000

elif opcao == 'porsche':
    diaria = 650

elif opcao == 'ix35':
    diaria = 700





if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total:.2f}')






