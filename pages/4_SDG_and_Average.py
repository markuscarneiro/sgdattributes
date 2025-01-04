import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

st.set_page_config(
    page_title="SDG and Average",
    page_icon="🌱",
    layout="wide"
)

# Função para criar o gráfico de radar
def radar_factory(num_vars, frame='circle'):
    theta = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)

    class RadarTransform(PolarAxes.PolarTransform):
        def transform_path_non_affine(self, path):
            if path._interpolation_steps > 1:
                path = path.interpolated(num_vars)
            return Path(self.transform(path.vertices), path.codes)

    class RadarAxes(PolarAxes):
        name = 'radar'
        PolarTransform = RadarTransform

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.set_theta_zero_location('N')

        def fill(self, *args, closed=True, **kwargs):
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            if x[0] != x[-1]:
                x = np.append(x, x[0])
                y = np.append(y, y[0])
                line.set_data(x, y)

        def set_varlabels(self, labels, fontsize=10):
            self.set_thetagrids(np.degrees(theta), labels, fontsize=fontsize)

        def _gen_axes_patch(self):
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars, radius=.5, edgecolor="k")
            else:
                raise ValueError("Unknown value for 'frame': %s" % frame)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                spine = Spine(axes=self, spine_type='circle', path=Path.unit_regular_polygon(num_vars))
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5) + self.transAxes)
                return {'polar': spine}

    register_projection(RadarAxes)
    return theta

# Função para carregar os dados do arquivo
@st.cache_data
def load_data(file_path):
    try:
        df = pd.read_csv(file_path, delimiter=';')
        # Criar a coluna MEDIA (média dos valores para os portos)
        df['MEDIA'] = df[['Port A', 'Port B', 'Port C', 'Port D', 'Port E', 'Port F']].mean(axis=1)
        return df
    except FileNotFoundError:
        st.error("O arquivo não foi encontrado.")
        return pd.DataFrame()

# Especificar o caminho do arquivo
file_path = "BASE.csv"
df = load_data(file_path)

# Verificar se o DataFrame foi carregado corretamente
if df.empty:
    st.error("Não foi possível carregar os dados. Verifique o arquivo fornecido.")
else:
    # Configuração do layout do Streamlit
    st.markdown("<h1 style='text-align: center;'>SDG per Port vs. Average per SDG</h1>", unsafe_allow_html=True)

    # Adicionar a select box para selecionar o porto em uma estrutura de três colunas
    col1, col2, col3 = st.columns([1, 2, 1])  # Colunas para centralizar a select box

    with col2:  # Coluna do meio
        portos = ['Port A', 'Port B', 'Port C', 'Port D', 'Port E', 'Port F']
        porto_selecionado = st.selectbox("Select Port", portos)

    st.markdown(f"<h3 style='text-align: center;'>{porto_selecionado}</h3>", unsafe_allow_html=True)

    # Obter todos os temas únicos (ODS)
    temas = df['TEMA'].unique()

    # Gerar um par de gráficos (porto e média) para cada tema
    for tema in temas:
        df_filtrado = df[df['TEMA'] == tema]

        # Verificar se há dados para o tema selecionado
        if df_filtrado.empty:
            st.warning(f"Não há dados disponíveis para o tema '{tema}'.")
            continue

        # Definir número de variáveis para o gráfico de radar
        N = len(df_filtrado['ITEM_AJUST'].unique())
        
        # Verificar se N é maior que zero para evitar divisão por zero
        if N == 0:
            st.warning(f"Não há itens disponíveis para gerar o gráfico de radar para o tema '{tema}'.")
            continue

        # Criar o gráfico de radar
        theta = radar_factory(N, frame='polygon')

        # Gráfico comparativo do porto selecionado com a média para o tema atual
        fig, (ax1, ax2) = plt.subplots(figsize=(12, 6), nrows=1, ncols=2, subplot_kw=dict(projection='radar'))
        fig.subplots_adjust(wspace=0.5, top=0.85, bottom=0.15)

        valores_porto = df_filtrado[porto_selecionado].values[:N]
        valores_media = df_filtrado['MEDIA'].values[:N]
        labels = df_filtrado['ITEM_AJUST'].values[:N]

        # Gráfico do porto específico
        ax1.plot(theta, valores_porto, color='#00A36C', linewidth=2, label=porto_selecionado)
        ax1.fill(theta, valores_porto, color='#00A36C', alpha=0.5)
        ax1.set_varlabels(labels, fontsize=10)
        ax1.set_title(f"{porto_selecionado} - {tema}", weight='bold', size='medium', position=(0.5, 1.1), horizontalalignment='center')
        ax1.set_rgrids(range(0, 4), labels=["0", "1", "2", "3"], angle=0, fontsize=8)

        # Gráfico da média
        ax2.plot(theta, valores_media, color='gray', linewidth=2, linestyle='--', label='Average')
        ax2.fill(theta, valores_media, color='gray', alpha=0.2)
        ax2.set_varlabels(labels, fontsize=10)
        ax2.set_title(f"Average - {tema}", weight='bold', size='medium', position=(0.5, 1.1), horizontalalignment='center')
        ax2.set_rgrids(range(0, 4), labels=["0", "1", "2", "3"], angle=0, fontsize=8)

        # Configurações de grade e legendas
        for ax in (ax1, ax2):
            ax.grid(True, which='major', axis='x', color='gray', linestyle='-', linewidth=0.5)

        st.pyplot(fig)
