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
    page_title="SDG per Port",
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

# Carregar o arquivo diretamente
@st.cache_data
def load_data(file_path):
    try:
        df = pd.read_csv(file_path, delimiter=';')
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
    # Lista de portos
    portos = ['Port A', 'Port B', 'Port C', 'Port D', 'Port E', 'Port F']

    # Configuração do layout do Streamlit
    st.markdown("<h1 style='text-align: center;'>SDG per Port</h1>", unsafe_allow_html=True)

    # Agrupar por TEMA para obter os valores para cada porto
    df_filtrado = df.groupby('TEMA')[['Port A', 'Port B', 'Port C', 'Port D', 'Port E', 'Port F']].mean().reset_index()
    N = len(df_filtrado['TEMA'])

    # Criar o gráfico de radar com TEMA como rótulo
    theta = radar_factory(N, frame='polygon')

    # Gerar um gráfico individual para cada porto
    fig, axs = plt.subplots(figsize=(18, 12), nrows=2, ncols=3, subplot_kw=dict(projection='radar'))
    fig.subplots_adjust(wspace=0.25, hspace=0.35, top=0.85, bottom=0.1)

    # Cor verde personalizada
    verde_custom = '#00A36C'

    for ax, porto in zip(axs.flat, portos):
        valores = df_filtrado[porto].values
        labels = df_filtrado['TEMA'].values  # Usar TEMA como rótulos

        ax.plot(theta, valores, color=verde_custom, linewidth=2)
        ax.fill(theta, valores, color=verde_custom, alpha=0.5)
        ax.set_varlabels(labels, fontsize=10)  # Tamanho original da fonte dos rótulos
        ax.set_title(porto, weight='bold', size='medium', position=(0.5, 1.1), horizontalalignment='center')  # Tamanho original do título
        ax.grid(True, which='major', axis='x', color='gray', linestyle='-', linewidth=0.5)
        ax.set_rgrids(range(0, 4), labels=["0", "1", "2", "3"], angle=0, fontsize=8)

    # Exibir o gráfico no Streamlit
    st.pyplot(fig)
