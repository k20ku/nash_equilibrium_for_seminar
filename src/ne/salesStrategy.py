from typing import Callable
from enum import Enum
import dataclasses

class SalesStrategy(Enum):
    OFF = lambda p,q,c: (p-2*c)*q
    HY  = lambda p,q,c: (p-c)*q
    ON  = lambda p,q,c: p*q
