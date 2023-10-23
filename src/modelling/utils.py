# Use this module to code a `pickle_object` function.
# This will be useful to pickle the model
# (and encoder if need be).
import pickle
from typing import Any

from prefect import task


@task(name="Load pickle")
def load_pickle(path: str) -> Any:
    with open(path, "rb") as f:
        loaded_obj = pickle.load(f)
    return loaded_obj


@task(name="Save pickle")
def save_pickle(path: str, obj: Any) -> None:
    with open(path, "wb") as f:
        pickle.dump(obj, f)