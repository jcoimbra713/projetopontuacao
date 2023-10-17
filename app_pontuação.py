import pickle
import streamlit as st
import numpy as np

# Carregando a Máquina Preditiva
pickle_in = open('maquina_preditiva_pontuação_cliente.pkl', 'rb') 
maquina_preditiva_pontuação_cliente = pickle.load(pickle_in)

# Essa função é para criação da página web
def main():  
    # Elementos da página web
    # Nesse ponto, você deve personalizar o sistema com sua marca
    html_temp = """ 
    <div style ="background-color:blue;padding:13px"> 
    <h1 style ="color:white;text-align:center;">PROJETO PARA PREVER PONTUAÇÃO DE CRÉDITO</h1> 
    <h2 style ="color:white;text-align:center;">SISTEMA PARA PONTUAÇÃO DE CRÉDITO< - by João Coimbra </h2> 
    </div> 
    """
      
    # Função do Streamlit que faz o display da página web
    st.markdown(html_temp, unsafe_allow_html=True) 
      
    # As linhas abaixo criam as caixas nas quais o usuário vai inserir os dados da pessoa que deseja prever o diabetes
    idade = st.number_input("Valor Do Empréstimo")
    profissao = st.selectbox('Profissão', 
    ("advogado","arquiteto","cientista","contador","desenvolvedor","empresario","engenheiro","escritor",
     "gerente","gerente_midia","jornalista","mecanico","medico","musico","professor"))
    salario_anual = st.number_input("Salario Anual") 
    num_contas = st.number_input("Númnero de Contas") 
    num_cartoes = st.number_input("Númnero de Cartões") 
    juros_emprestimo = st.number_input("Valor do Juros")
    num_emprestimos = st.number_input("Quantidade de Empréstimos")
    dias_atraso = st.number_input("Quantidade de Dias Que Atrasou O Pagamento")
    num_pagamentos_atrasado = st.number_input("Quantas Vezes Atrasou O Pagamento")
    mix_credito  = st.selectbox('Mix Credito', ("Bom", "Normal","Ruim"))
    divida_total = st.number_input("Total Da Divida")
    taxa_uso_credito = st.number_input("Valor da Taxa de uso")
    investimento_mensal = st.number_input("Valor Do Investimento Mensal")  
    comportamento_pagamento = st.selectbox('Comportamento do Pagamento', ("Alto Gasto Com Pagamento Alto", "Alto Gasto Com Pagamento Baixo","Alto Gasto Com Pagamento Médio","Baixo Gasto Com Pagamento Alto","Baixo Gasto Com Pagamento Baixo","Baixo Gasto Com Pagamento Médio"))
    saldo_final_mes = st.number_input("Saldo Final Do Mês") 
    emprestimo_carro = st.selectbox('Fez Empréstimo de Carro', ("Não", "Sim"))
    emprestimo_casa = st.selectbox('Fez Empréstimo de Casa', ("Não", "Sim"))
    emprestimo_pessoal = st.selectbox('Fez Empréstimo Pessoal', ("Não", "Sim"))
    emprestimo_credito  = st.selectbox('Fez Empréstimo de Crédito', ("Não", "Sim"))
    emprestimo_estudantil  = st.selectbox('Fez Empréstimo de Estudantil', ("Não", "Sim"))
  

    # Quando o usuário clicar no botão "Verificar", a Máquina Preditiva fará seu trabalho
    if st.button("Verificar"): 
        result, probabilidade = prediction(idade, profissao, salario_anual, num_contas, num_cartoes, juros_emprestimo,
              num_emprestimos, dias_atraso, num_pagamentos_atrasado, mix_credito,
              divida_total, taxa_uso_credito, investimento_mensal, comportamento_pagamento,
              saldo_final_mes, emprestimo_carro, emprestimo_casa, emprestimo_pessoal,
              emprestimo_credito, emprestimo_estudantil) 
        st.success(f'Resultado: {result}')
        st.write(f'Probabilidade: {probabilidade}')

# Essa função faz a predição usando os dados inseridos pelo usuário
def prediction(idade, profissao, salario_anual, num_contas, num_cartoes, juros_emprestimo,
              num_emprestimos, dias_atraso, num_pagamentos_atrasados, mix_credito,
              divida_total, taxa_uso_credito, investimento_mensal, comportamento_pagamento,
              saldo_final_mes, emprestimo_carro, emprestimo_casa, emprestimo_pessoal,
              emprestimo_credito, emprestimo_estudantil):   
    # Pre-processando a entrada do Usuário    
    profissao_dict = {
        "advogado": 0,
        "arquiteto": 1,
        "cientista": 2,
        "contador": 3,
        "desenvolvedor": 4,
        "empresario": 5,
        "engenheiro": 6,
        "escritor": 7,
        "gerente": 8,
        "gerente midia": 9,
        "jornalista": 10,
        "mecanico": 11,
        "medico": 12,
        "musico": 13,
        "professor": 14,
        
    }
    profissao = profissao_dict[profissao]

    mix_credito_dict = {
        "Bom": 0,
        "Normal": 1,
        "Ruim": 2,
    }
    mix_credito = mix_credito_dict[mix_credito]


   
    comportamento_pagamento_dict = {
        "Alto Gasto Com Pagamento Alto": 0,
        "Alto Gasto Com Pagamento Baixo": 1,
        "Alto Gasto Com Pagamento Médio": 2,
        "Baixo Gasto Com Pagamento Alto": 3,
        "Baixo Gasto Com Pagamento Baixo": 4,
        "Baixo Gasto Com Pagamento Médio": 5,
    }
    comportamento_pagamento = comportamento_pagamento_dict[comportamento_pagamento]



    emprestimo_carro_dict = {
        "Não": 0,
        "Sim": 1,
    }
    emprestimo_carro = emprestimo_carro_dict[emprestimo_carro]


    emprestimo_casa_dict = {
        "Não": 0,
        "Sim": 1,
    }
    emprestimo_casa = emprestimo_casa_dict[emprestimo_casa]


    emprestimo_pessoal_dict = {
        "Não": 0,
        "Sim": 1,
    }
    emprestimo_pessoal = emprestimo_pessoal_dict[emprestimo_pessoal]


    emprestimo_credito_dict = {
        "Não": 0,
        "Sim": 1,
    }
    emprestimo_credito = emprestimo_credito_dict[emprestimo_credito]

    emprestimo_estudantil_dict = {
        "Sim": 0,
        "Não": 1,
    }
    emprestimo_estudantil = emprestimo_estudantil_dict[emprestimo_estudantil]

    # Fazendo a Predição
    parametro = np.array([[idade, profissao, salario_anual, num_contas, num_cartoes, juros_emprestimo,
              num_emprestimos, dias_atraso, num_pagamentos_atrasados, mix_credito,
              divida_total, taxa_uso_credito, investimento_mensal, comportamento_pagamento,
              saldo_final_mes, emprestimo_carro, emprestimo_casa, emprestimo_pessoal,
              emprestimo_credito, emprestimo_estudantil]])
    fazendo_previsao = maquina_preditiva_pontuação_cliente.predict(parametro)
    probabilidade = maquina_preditiva_pontuação_cliente.predict_proba(parametro)

    if (fazendo_previsao == 0).any():
        pred = 'A POTUAÇÃO DO CLIENTE SERÁ OURO!'

    elif (fazendo_previsao == 1).any():
        pred = 'A POTUAÇÃO DO CLIENTE SERÁ POBRE!'    
    
    else:
        pred = 'A POTUAÇÃO DO CLIENTE SERÁ PADRÃO!'

   
   
    return pred, probabilidade

if __name__ == '__main__':
    main()




