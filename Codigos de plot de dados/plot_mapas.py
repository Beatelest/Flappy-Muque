import pyqtgraph as pg
import serial
import time
import numpy as np
import imageio.v3 as iio  # imageio v3 é moderno
from pyqtgraph.Qt import QtCore
from PyQt6.QtWidgets import QApplication

# ser = serial.Serial('COM7', 115200)  # Ajuste a porta se necessário


tempo_inicial = time.perf_counter()
amplitude = []
tempo = []
limiar = []
t_simu = 30

app = QApplication([])
win = pg.GraphicsLayoutWidget(show=True)
plot = win.addPlot()
plot.setXRange(0, t_simu)  # Em segundos
plot.setYRange(0, 3.3)

bola = pg.ScatterPlotItem(size=15, brush='g') 
plot.addItem(bola)


# Carrega imagem uma vez só
# imagem_path = r"C:\Users\teles\Documents\UFS - GRADUACAO\graduacao\Estagio\codigos\Conversao_ad\trapezio.jpg"
# imagem = iio.imread(imagem_path)
# img_item = pg.ImageItem(np.rot90(imagem, k=-1))  # Corrige rotação
# img_item.setZValue(0)
# img_item.setRect(0, 0, 20, 3.5)
# plot.addItem(img_item)
# plot.setXRange(0, 20)
# plot.setYRange(0, 3.3)
# # plot.invertX(True)

# Fabricando imagem 
# Pontos (x, y) do trajeto central — escalado para 0 a 20 em X e 0 a 3.3 em Y
caminho_x = np.arange(1, t_simu+1)  # Supondo t_simu = 40

# TRAPÉZIO
caminho_y = np.concatenate([
    0.5 * np.ones(5),
    [0.5, 0.5, 1, 1.5, 2],
    2 * np.ones(10),
    [2, 1.5, 1, 0.5, 0.5],
    0.5 * np.ones(5),
])
# RETA
# caminho_y = 1.5 * np.ones(t_simu)

# # TRIÃNGULO
# caminho_y = np.concatenate([
#     0.5 * np.ones(10),
#     [0.5, 1, 1.5, 2, 2.5],
#     [2.5, 2, 1.5, 1, 0.5],
#     0.5 * np.ones(10),
# ])


trajeto = pg.PlotDataItem(
    caminho_x,
    caminho_y,
    pen=pg.mkPen('b', width=80)
)
plot.addItem(trajeto)


bola = pg.ScatterPlotItem(size=15, brush='g')
bola.setZValue(1)
plot.addItem(bola)

# Loop principal
while True:
    try :
      app.processEvents()
    # try:
    #     ybola = float(ser.readline().decode().strip())
    #     ybola = round(ybola, 3)
    #     t = round(time.perf_counter() - tempo_inicial, 3)

    #     bola.setData([t], [ybola])
    #     time.sleep(0.001)

    #     amplitude.append(ybola)
    #     tempo.append(t)
        
    #     if t >= t_simu:
    #         print("Tempo atingido, encerrando e salvando dados...")
    #         dados_combinados = np.column_stack((tempo, amplitude))
    #         np.savetxt('dados_triangulo.txt', dados_combinados, header="Tempo, Amplitude", fmt='%.3f')
    #         break

    except KeyboardInterrupt:
        print("Encerrando e salvando dados...")
        # dados_combinados = np.column_stack((tempo, amplitude))
        # np.savetxt('dados_trapezio.txt', dados_combinados, header="Tempo, Amplitude", fmt='%.3f')
        break
    # except:
    #     pass

