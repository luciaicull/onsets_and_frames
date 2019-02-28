import torch

SAMPLE_RATE = 16000
HOP_LENGTH = 512
MELS_BIN = 229
FFT_WINDOW = 2048

ONSET_FRAME_THRESHOLD = 0.5

DEFAULT_DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'