import numpy as np
from torch.utils.data import Dataset

from .constants import *

class PianoRollAudioDataset(Dataset):
    def __init__(self, path):
        self.path = path

        self.data = []

    def __getitem__(self, index):
        data = self.data[index]
        result = dict(path=data['path'])

    def __len__(self):
        return len(self.data)

class MAESTRO(PianoRollAudioDataset):
    def __init__(self, path='/ssd2/maestro/maestro-v1.0.0'):
        super().__init__(path)


class MAPS(PianoRollAudioDataset):
    def __init__(self, path='/ssd2/MAPS_MUS'):
        super().__init__(path)




