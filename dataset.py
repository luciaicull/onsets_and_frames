import os
from abc import abstractmethod

import numpy as np
from torch.utils.data import Dataset

from .constants import *

class PianoRollAudioDataset(Dataset):
    def __init__(self, path, groups=None, sequence_length=None, seed=42, device=DEFAULT_DEVICE):
        self.path = path
        self.groups = groups if groups is not None else self.available_groups()

        self.data = []

    def __getitem__(self, index):
        data = self.data[index]
        result = dict(path=data['path'])

    def __len__(self):
        return len(self.data)

    @classmethod
    @abstractmethod
    def available_groups(cls):
        """return the names of all available groups"""
        raise NotImplementedError

    @abstractmethod
    def files(self, group):
        """return the list of input files (audio_filename, tsv_filename) for this groups"""
        raise NotImplementedError

    def load(self, audio_path, tsv_path):
        """
        load an audio track and the corresponding labels
        Returns
        -------
            A dictionary containing the following data:
            audio: torch.ShortTensor, shape = [num_samples]
                the raw waveform
            ramp: torch.ByteTensor, shape = [num_steps, midi_bins]
                a matrix that contains the number of frames after the corresponding onset
            velocity: torch.ByteTensor, shape = [num_steps, midi_bins]
                a matrix that contains MIDI velocity values at the frame locations
        """
        saved_data_path = audio_path.replace('.flac', '.pt').replace('.wav', '.pt')
        if os.path.exists(saved_data_path):
            return torch.load(saved_data_path)

        


class MAESTRO(PianoRollAudioDataset):
    def __init__(self, path='/ssd2/maestro/maestro-v1.0.0'):
        super().__init__(path)


class MAPS(PianoRollAudioDataset):
    def __init__(self, path='/ssd2/MAPS_MUS'):
        super().__init__(path)




