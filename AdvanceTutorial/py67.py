# Useful python decorator


import time
from functools import wraps
from typing import Callable, Any
from time import sleep

def retry(retries: int = 3, delay: float = 1) -> Callable:
    if retries < 1 or delay <= 0:
        raise ValueError('Are You High, Mate?')
    
    def decorator(func: Callable) -> Any:
        for i in range(1, retries + 1):
            ...

def connect() -> None:
    ...