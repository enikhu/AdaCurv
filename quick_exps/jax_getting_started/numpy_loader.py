import numpy as onp
from torch.utils import data

def numpy_collate(batch):
  if isinstance(batch[0], onp.ndarray):
    return onp.stack(batch)
  elif isinstance(batch[0], (tuple,list)):
    transposed = zip(*batch)
    return [numpy_collate(samples) for samples in transposed]
  else:
    return onp.array(batch)

class NumpyLoader(data.DataLoader):
  def __init__(self, dataset, batch_size=1,
                shuffle=False, sampler=None,
                batch_sampler=None, num_workers=0,
                pin_memory=False, drop_last=False,
                timeout=0, worker_init_fn=None):
    super(self.__class__, self).__init__(dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        sampler=sampler,
        batch_sampler=batch_sampler,
        num_workers=num_workers,
        collate_fn=numpy_collate,
        pin_memory=pin_memory,
        drop_last=drop_last,
        timeout=timeout,
        worker_init_fn=worker_init_fn)

class CastToNumpy(object):
  def __call__(self, arr):
      return onp.array(arr, dtype=onp.float32)
    # return onp.ravel(onp.array(pic, dtype=onp.float32)) / 255.0

class FlattenAndCast(object):
  def __call__(self, pic):
      # return onp.array(pic, dtype=onp.float32)
    return onp.ravel(onp.array(pic, dtype=onp.float32)) / 255.0
