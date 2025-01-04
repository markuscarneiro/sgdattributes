import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="SDG Attributes",
    page_icon="🌱",
    layout="centered"
)

# Título da página
st.title("🌱 SDG Attributes")

# Corpo do texto
st.markdown("""
### About the Project
This model is part of the project **"Green Port Complex: Proposed Indicators Linked to the SDGs"**, led by **Darliane Cunha** and **Clóvis Oliveira**, with financial support from the **Foundation for Research and Scientific and Technological Development of Maranhão (FAPEMA)** and the **Maranhão Port Administration Company (EMAP)**.

The model was conceived by:
- **Darliane Cunha**
- **Clóvis Oliveira**
- **Markus Carneiro Costa**

The data visualization tool was developed by:
- **Markus Carneiro Costa**
""")

# Footer
st.markdown("---")
