import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

historia_temperaturas = pd.read_csv('/home/ec2-user/clubes_de_ciencia/Dia_4/historia_temperaturas.csv')
produccion_petroleo = pd.read_csv('/home/ec2-user/clubes_de_ciencia/Dia_4/produccion_petrolio.csv')
produccion_petroleo.Date = pd.to_datetime(produccion_petroleo.Date)
historia_temperaturas = pd.to_datetime(historia_temperaturas.dt)