# (c) 2024 Kamil Stachurski
# kamil.stachurski@ifj.edu.pl

from pathlib import Path
from brukerapi.dataset import Dataset

data_path = '/Users/kamil/MCAO-Model/data/20240305_113058_GR24_CeO2_Gd_PAA_filtracja_i_sonifikacja_1_1'

dataset = Dataset(data_path / Path('9/fid'))

data = dataset.data

print(data.shape)
print(dataset.TE)
print(dataset.TR)
# print(dataset.flip_angle)
# print(dataset.sw)
# print(dataset.transmitter_freq)