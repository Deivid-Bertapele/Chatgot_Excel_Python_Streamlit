# Análise de Dados com ChatGPT

Este projeto utiliza **Streamlit** para criar uma interface interativa que permite carregar arquivos de dados (CSV ou Excel) e fazer perguntas sobre os dados utilizando a API da OpenAI (ChatGPT).

## Funcionalidades
- Upload de arquivos CSV ou Excel.
- Exibição das primeiras linhas dos dados carregados.
- Interação com o ChatGPT para gerar análises baseadas nos dados fornecidos.

## Tecnologias Utilizadas
- Python
- Streamlit
- Pandas
- OpenAI API
- dotenv (para gerenciar variáveis de ambiente)

## Como Executar
1. Colcar o repositório:
    ```bash
    git clone https://github.com/Deivid-Bertapele/Chatgt_Excel_Python_Streamlit.git
    ```
2. Instale as dependências necessárias:
    ```bash
    pip install streamlit pandas openai python-dotenv
    ```
3. Crie um arquivo `.env` e defina a sua chave de API da OpenAI:
    ```
    KEY_OPEN_AI=your_openai_api_key
    ```
4. Execute o aplicativo Streamlit:
    ```bash
    streamlit run app.py
    ```

## Como Usar
1. Faça o upload de um arquivo CSV ou Excel.
2. Visualize as primeiras linhas do conjunto de dados.
3. Digite uma pergunta sobre os dados no campo de texto.
4. Receba uma resposta gerada pelo ChatGPT com base nos dados fornecidos.

## Observação
- Certifique-se de que sua chave de API OpenAI é válida e possui créditos suficientes.
- O modelo utilizado é o **GPT-4o-mini**, podendo ser alterado conforme necessidade.

![image](https://github.com/user-attachments/assets/0414e25e-efb0-41d8-a5b3-e1ee33dc29cc)



