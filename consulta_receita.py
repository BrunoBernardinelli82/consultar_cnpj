import requests
import streamlit as st


def consultar_cnpj_api(cnpj):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    headers = {"key": "chave-api-dados",
               "value": "colocar a chave da api"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
st.set_page_config(page_title="Consulta de CNPJ", page_icon="🔍")
st.title("Consulta de CNPJ")



cnpj_consulta = st.text_input("Digite o CNPJ para consulta")
cnpj_consulta = cnpj_consulta.replace(".", "").replace("/", "").replace("-", "")
print(cnpj_consulta)


if st.button("Consultar"):
    resultado = consultar_cnpj_api(cnpj_consulta)

    if resultado:
        #st.dataframe(pd.DataFrame(resultado))
        
        nome_empresa = resultado.get('nome', 'N/A')
        if "RECUPERACAO JUDICIAL" in nome_empresa:
            nome_empresa = f"<span style='color:red;'>{nome_empresa}</span>"

        st.markdown(f"""
        ## Informações da Empresa
        **Nome:** {nome_empresa}
        **Nome Fantasia:** {resultado.get('fantasia', 'N/A')}
        **CNPJ:** {resultado.get('cnpj', 'N/A')}
        **Abertura:** {resultado.get('abertura', 'N/A')}
        **Situação:** {resultado.get('situacao', 'N/A')}
        **Tipo:** {resultado.get('tipo', 'N/A')}
        **Porte:** {resultado.get('porte', 'N/A')}
        **Natureza Jurídica:** {resultado.get('natureza_juridica', 'N/A')}
        
        ## Atividade Principal
        **Código:** {resultado.get('atividade_principal', [{}])[0].get('code', 'N/A')}
        **Descrição:** {resultado.get('atividade_principal', [{}])[0].get('text', 'N/A')}
        
        ## Atividades Secundárias
        """, unsafe_allow_html=True)

        for atividade in resultado.get('atividades_secundarias', []):
            st.markdown(f"""
            **Código:** {atividade.get('code', 'N/A')}
            **Descrição:** {atividade.get('text', 'N/A')}
            """)

        st.markdown(f"""
        ## Quadro de Sócios e Administradores
        **Nome:** {resultado.get('qsa', [{}])[0].get('nome', 'N/A')}
        **Qualificação:** {resultado.get('qsa', [{}])[0].get('qual', 'N/A')}
        
        ## Endereço
        **Logradouro:** {resultado.get('logradouro', 'N/A')}
        **Número:** {resultado.get('numero', 'N/A')}
        **Bairro:** {resultado.get('bairro', 'N/A')}
        **Município:** {resultado.get('municipio', 'N/A')}
        **UF:** {resultado.get('uf', 'N/A')}
        **CEP:** {resultado.get('cep', 'N/A')}
        
        ## Contato
        **Email:** {resultado.get('email', 'N/A')}
        **Telefone:** {resultado.get('telefone', 'N/A')}
        
        ## Capital Social
        **Capital Social:** R$ {resultado.get('capital_social', 'N/A')}
        
        ## Simples Nacional
        **Optante:** {'Sim' if resultado.get('simples', {}).get('optante', False) else 'Não'}
        **Data de Opção:** {resultado.get('simples', {}).get('data_opcao', 'N/A')}
        **Data de Exclusão:** {resultado.get('simples', {}).get('data_exclusao', 'N/A')}
        
        ## Atualizações
        **Última Atualização:** {resultado.get('ultima_atualizacao', 'N/A')}
        """)

    
    
    