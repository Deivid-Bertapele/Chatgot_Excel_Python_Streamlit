import streamlit as st
from dotenv import load_dotenv
import pandas as pd
import openai
import os

# Carrega as variáveis de ambiente
load_dotenv()


def carregar_dados(arquivo):
    try:
        if arquivo.name.endswith('.csv'):
            df = pd.read_csv(arquivo)
        elif arquivo.name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(arquivo)
        else:
            return None
        return df
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo: {str(e)}")
        return None


def perguntar_ao_chatgpt(pergunta, contexto):
    api_key = os.environ.get("KEY_OPEN_AI")
    if not api_key:
        return "Erro: Chave da API OpenAI não encontrada nas variáveis de ambiente"

    client = openai.OpenAI(api_key=api_key)
    try:
        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": contexto},
                {"role": "user", "content": pergunta}
            ],
            temperature=0.7
        )
        return resposta.choices[0].message.content
    except openai.RateLimitError:
        return "Erro: Limite de uso da API atingido. Por favor, verifique sua conta OpenAI e os limites de uso."
    except openai.AuthenticationError:
        return "Erro: Problema com a autenticação. Verifique sua chave API."
    except Exception as e:
        return f"Erro ao processar a pergunta: {str(e)}"


# Interface do Streamlit
st.title("Análise de Dados com ChatGPT")

# Upload do arquivo
arquivo = st.file_uploader("Carregue seu arquivo CSV ou Excel", type=[
                           'csv', 'xlsx', 'xls'])

if arquivo is not None:
    df = carregar_dados(arquivo)

    if df is not None:
        # Mostrar os primeiros registros
        st.write("Primeiros registros do arquivo:")
        st.write(df.head())

        # Área para a pergunta
        pergunta = st.text_input("Faça uma pergunta sobre seus dados:")

        if pergunta:
            # Criar contexto com informações sobre os dados
            contexto = f"""
            Você é um analista de dados especializado. Analise os dados fornecidos.
            As colunas disponíveis são: {', '.join(df.columns.tolist())}
            Os primeiros registros são: {df.head().to_string()}
            """

            # Obter resposta do ChatGPT
            resposta = perguntar_ao_chatgpt(pergunta, contexto)

            # Mostrar resposta
            st.write("Resposta:")
            st.write(resposta)
