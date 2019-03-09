import numpy as np
from torch.utils.data import Dataset

from .constants import *

class AudioToPianoRollDataset(Dataset):
    def __init__(self, path, device=DEFAULT_DEVICE):
        self.path = path
        self.device = device

        self.data = []
        # print('Loading %d group%s of %s at %s' % (len(groups), 's'[:len(groups) - 1], self.__class__.__name__, path))



#    def __getitem__(self, index):

