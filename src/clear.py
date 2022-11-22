import gc

gc.collect()

import torch
torch.cuda.empty_cache()

torch.cuda.memory_summary(device=None, abbreviated=False)