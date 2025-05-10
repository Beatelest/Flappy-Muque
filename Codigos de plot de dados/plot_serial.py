import pyqtgraph as pg
import serial
import time
import numpy as np
from pyqtgraph.Qt import QtCore
from PyQt6.QtWidgets import QApplication

ser = serial.Serial('COM7', 115200)  # Ajuste a porta se necessário

app = QApplication([])
win = pg.GraphicsLayoutWidget(show=True)
plot = win.addPlot()
plot.setXRange(-1, 1)
plot.setYRange(0, 3.3)

bola = pg.ScatterPlotItem(size=15, brush='g') 
plot.addItem(bola)

barra1 = pg.BarGraphItem(x=[0], height=[0], width=2, brush='r')
barra2 = pg.BarGraphItem(x=[0], height=[0], width=2, brush='r')
plot.addItem(barra1)
plot.addItem(barra2)

tempo_inicial = time.perf_counter()
amplitude = []
tempo = []
limiar = []
# Loop principal no lugar de QTimer
while True:
    app.processEvents()  # Atualiza a interface gráfica

    try:
        ybola = float(ser.readline().decode().strip())
        ybola = round(ybola, 1)
        bola.setData([0], [ybola])
        print(ybola)
        tempo_atual = time.perf_counter()
        t = tempo_atual - tempo_inicial
        # print(f"Tempo decorrido: {t:.4f} segundos")
        if t <= 5 :
            limiar.append = 0
        elif 5 < t < 10:
            barra1.setOpts(y=[0], height=[0.05])
            barra2.setOpts(y=[0.5], height=[0.05])
            limiar.append = 1
        elif 10 <= t < 15:
            barra1.setOpts(y=[0.5], height=[0.05])
            barra2.setOpts(y=[1], height=[0.05])
            limiar.append = 2
        elif 15 <= t < 20:
            barra1.setOpts(y=[1], height=[0.05])
            barra2.setOpts(y=[1.5], height=[0.05])
            limiar.append = 3
        elif 20 <= t < 25:
            barra1.setOpts(y=[1.5], height=[0.05])
            barra2.setOpts(y=[2], height=[0.05])
            limiar.append = 4
        elif 25 <= t < 30:
            barra1.setOpts(y=[2], height=[0.05])
            barra2.setOpts(y=[2.5], height=[0.05])
            limiar.append = 5
        elif 30 <= t < 35:
            barra1.setOpts(y=[2.5], height=[0.05])
            barra2.setOpts(y=[3], height=[0.05])
            limiar.append = 6

        time.sleep(0.0001)  # Pequena pausa para evitar travar o sistema
        amplitude.append(ybola)
        t = round(t,3)
        tempo.append(t)
    except KeyboardInterrupt:
        print("Encerrando e salvando dados...")
        # Combine os dois vetores em uma matriz 2D
        dados_combinados = np.column_stack((tempo, amplitude, limiar))
        # Salve a matriz combinada no arquivo
        np.savetxt('dados.txt', dados_combinados, header="Tempo, Amplitude, limiar", fmt='%f')
        break
    except:
        pass
