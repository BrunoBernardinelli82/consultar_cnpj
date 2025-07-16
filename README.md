
# 📊 Consulta de CNPJ – Receita Federal

Este projeto é uma aplicação simples em Python com Streamlit que permite consultar informações de empresas brasileiras a partir do número do CNPJ, utilizando a API pública da ReceitaWS.

## 🚀 Funcionalidades

- Consulta de dados cadastrais de empresas pelo CNPJ
- Exibição de:
  - Nome empresarial e fantasia
  - Situação cadastral
  - Atividades principal e secundárias
  - Quadro societário
  - Endereço completo
  - Contato (telefone e e-mail)
  - Capital social
  - Informações do Simples Nacional

## 🛠️ Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Requests](https://docs.python-requests.org/)
- [API ReceitaWS](https://www.receitaws.com.br/)

## 📦 Instalação

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/consulta-cnpj.git
cd consulta-cnpj
```

2. Crie um ambiente virtual (opcional, mas recomendado):

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Instale as dependências:

```
pip install -r requirements.txt
```

4. Insira sua chave de API no script consulta_receita.py:

```

headers = {
    "key": "chave-api-dados",  # Substitua por sua chave real
    "value": "colocar a chave da api"
}
```

## ▶️ Como Usar
Execute o aplicativo com o comando no terminal dentro do seu ambiente virtual:

```
streamlit run consulta_receita.py
```

Digite o CNPJ desejado no campo de entrada e clique em Consultar para visualizar os dados da empresa.

## ⚠️ Observações

A API da ReceitaWS possui limites de uso. Consulte a documentação oficial para mais detalhes.
Certifique-se de que o CNPJ está no formato correto (somente números).

## 📄 Licença
Este projeto está licenciado sob a MIT License.


