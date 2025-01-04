import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="SDG Attributes Table",
    page_icon="🌱",
    layout="wide"
)

# Carregando o arquivo Excel
file_path = "SDG_attributes_ANEXO.xlsx"  # Ajuste o caminho conforme necessário
try:
    data = pd.read_excel(file_path)
    
    # Validar se as colunas necessárias estão presentes
    required_columns = ["CATEGORY", "ATTRIBUTE", "AREA", "METRIC"]
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        st.error(f"Erro: As seguintes colunas estão faltando no arquivo: {', '.join(missing_columns)}")
        st.stop()

    # Tratamento da coluna CATEGORY para preencher valores NaN
    data["CATEGORY"] = data["CATEGORY"].fillna(method="ffill")

    # Tratamento da coluna ATTRIBUTE para preencher valores NaN
    data["ATTRIBUTE"] = data["ATTRIBUTE"].fillna(method="ffill")

except FileNotFoundError as e:
    st.error(f"Erro: O arquivo '{file_path}' não foi encontrado. {e}")
    st.stop()
except Exception as e:
    st.error(f"Ocorreu um erro ao carregar o arquivo: {e}")
    st.stop()

# Título e introdução
st.title("SDG Attributes for Sector Ports")
st.write("This model presents the sustainability indicators associated with the Sustainable Development Goals (SDGs) for the port sector.")

# Dividindo a área de filtros em colunas
col1, col2 = st.columns([2, 2])  # Ajusta as larguras das colunas
with col1:
    # SelectBox para CATEGORY
    categories = data["CATEGORY"].unique()
    selected_category = st.selectbox("Select an SDG", options=categories)

with col2:
    # SelectBox para AREA
    areas = data[data["CATEGORY"] == selected_category]["AREA"].unique()
    selected_area = st.selectbox("Filter by AREA", options=["ALL"] + list(areas))

# Filtrando o DataFrame com base nas seleções
filtered_data = data[data["CATEGORY"] == selected_category]
if selected_area != "ALL":
    filtered_data = filtered_data[filtered_data["AREA"] == selected_area]

# Função para criar HTML com células mescladas na coluna ATTRIBUTE e linhas alternadas
def create_html_table(df):
    html = """
    <table style='width:100%; border-collapse: collapse;'>
        <thead>
            <tr style='background-color: #333333; color: white; font-weight: bold; border: 1px solid black;'>
                <th style='text-align: center; padding: 8px; border: 1px solid black;'>ATTRIBUTE</th>
                <th style='text-align: center; padding: 8px; border: 1px solid black;'>METRIC</th>
            </tr>
        </thead>
        <tbody>
    """
    
    previous_attribute = None
    row_color = "#FFFFFF"  # Branco
    alternate_color = "#F2F2F2"  # Cinza claro

    for _, row in df.iterrows():
        attribute = row["ATTRIBUTE"]
        metric = row["METRIC"]

        # Alterna a cor de fundo quando o valor do atributo muda
        if attribute != previous_attribute:
            row_color = alternate_color if row_color == "#FFFFFF" else "#FFFFFF"
            rowspan_count = (df["ATTRIBUTE"] == attribute).sum()
            html += f"<tr style='background-color: {row_color};'><td rowspan='{rowspan_count}' style='border: 1px solid black; padding: 8px; text-align: left;'>{attribute}</td>"
            previous_attribute = attribute
        else:
            html += f"<tr style='background-color: {row_color};'>"

        # Adiciona a célula METRIC
        html += f"<td style='border: 1px solid black; padding: 8px; text-align: left;'>{metric}</td></tr>"

    html += "</tbody></table>"
    return html

# Exibindo o DataFrame filtrado no Streamlit com HTML customizado
if not filtered_data.empty:
    st.subheader(f"Filtered Results for {selected_category}")
    html_table = create_html_table(filtered_data[["ATTRIBUTE", "METRIC"]])
    st.markdown(html_table, unsafe_allow_html=True)
else:
    st.write("No data available for display.")
