from typing import Union

from datasets import Dataset, DatasetDict, IterableDataset, IterableDatasetDict, Split
from datasets import load_dataset as hf_load_dataset
from datasets import load_from_disk


def load_dataset(
    path, use_load_from_disk=False, streaming=True, split=Split.TRAIN, **kwargs
) -> Union[DatasetDict, Dataset, IterableDatasetDict, IterableDataset]:
    if use_load_from_disk:
        ds = load_from_disk(path, **kwargs)
    else:
        ds = hf_load_dataset(path, streaming=streaming, split=split, **kwargs)
    return ds


def get_headers(ds):
    return ds.column_names


def get_features(ds):
    return ds.features


def get_row_count(ds):
    return ds.num_rows
