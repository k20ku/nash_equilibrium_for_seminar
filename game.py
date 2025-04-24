import sympy as sp
from typing import List, Tuple, Union


def optimalEquation(utilityFunc : sp.Expr, strategy: sp.Symbol)->sp.Eq:
    marginalUtility=sp.diff(utilityFunc, strategy)
    return sp.Eq(marginalUtility,0)

def equilibriate(*eqationStrategyPairs :Tuple[sp.Eq, sp.Symbol])->List[Tuple[sp.Expr, ...]]:
    """
    :param conditionStrategyPairs: [(eq1, strategy1), (eq2, strategy2), ...]
    :return: [(strategy1, value1), (strategy2, value2), ...]
    """
    if len(eqationStrategyPairs) == 0:
        return []
    eqs, strategies = map(list,zip(*eqationStrategyPairs))
    # `preresults`は`List[dict[]]`の時も`dict[Tuple]`の時もある
    return safeSolve(eqs, strategies)


def dictToTuple(d:dict)->Tuple:
    """
    >>> from sympy import symbols
    >>> x, y, c = symbols('x y c')
    >>> dictToTuple({x: -1})
    (-1,)
    >>> dictToTuple({x: c-1, y: c-2})
    (c-1, c-2)
    """
    return tuple(d.values())

def safeSolve(eqs :List[sp.Eq],
              strategies: List[sp.Symbol]
              )->List[Tuple[sp.Expr, ...]]:
    """
    :param eqs: List of equations
    :param strategies: List of variables to solve for
    :return: List of solutions as tuples
    """
    # やっぱり引数がからだったら事前条件満たしてない判定したほうがいい
    if len(eqs) == 0 or len(strategies) == 0:
        raise ValueError("Equations and strategies must not be empty")
    # 戦略に対して最適等式が
    if len(eqs) != len(strategies):
        raise ValueError("Number of equations must match number of strategies")
    preresults = sp.solve(eqs, strategies)
    return preresults if not isinstance(preresults, dict) else [dictToTuple(preresults)]

if __name__ == "__main__":
    x, y, c = sp.symbols('x y c')
    print(dictToTuple({})) # Output: ()
    print(dictToTuple({x: -1})) # Output: (-1,)
    print(dictToTuple({x: c-1, y: c-2})) # Output: (c-1, c-2)