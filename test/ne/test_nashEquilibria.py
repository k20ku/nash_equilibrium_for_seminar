import pytest
import sympy as sp
from src.ne.nashEquilibria import optimalEquation, MarketData, oneminus, equilibriate, safeSolve, dictToTuple

def test_ne():
    x, y, c = sp.symbols("x y c")
    assert x**2 == x*x 
