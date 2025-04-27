from __future__ import annotations
from typing import Callable
from salesStrategy import SalesStrategy
from nerefined import Quantity
from dataclasses import dataclass

import sympy as sp
"""
主に使用するライブラリです（もう先輩は卒業してしまって開発する意味はないのですが．．．）
Pythonに慣れるためであったり，便利だけど割とレガシーなSympyライブラリの便利な一部分を切り取って，モダンなPythonで仕上げていくことが目的です．
"""
def oneminus(x :sp.Expr) -> sp.Expr:
    1-x
"""
実際に利用してもらうクラス．
`game.py` を直接利用しないで，卒論の主な検証作業はこれでできるようにする．
newConditionsが卒論の章番号に対応しているので，そこから，簡単にこのクラスを利用できる関数も追加したい．
"""
class MarketData:
    
    # 価格

    """
    使うときに必要最低限の引数だけでインスタンス化ができるように当時作ったが，改修していくにつれて場当たり的な感じが否めない．
    データコンテナ化して，もっと均衡計算ロジックとデータ格納を分離していきたい．だいたい，メソッドにすればいいところが
    フィールドになっていてダサい．
    """
    def __init__(self,
                 quantity_a,
                 strategy_a: SalesStrategy,
                 strategy_b: SalesStrategy
                ):
        self.Qa :Callable[[sp.Symbol, sp.Symbol], sp.Expr]= quantity_a 
        self.Qb = lambda pa,pb: oneminus(self.Qa(pa,pb)) # 実行時に計算するようにしている．
        self.pi_a = strategy_a
        self.pi_b = strategy_b

    def func(quantity_a,
             strategy_a: SalesStrategy,
             strategy: SalesStrategy) -> sp.Expr:
        return 1

def optimalEquation(utilityFunc : sp.Expr, strategy: sp.Symbol)->sp.Eq:
    marginalUtility=sp.diff(utilityFunc, strategy)
    return sp.Eq(marginalUtility,0)

if __name__ == "__main__":

    p1,p2,c=sp.symbols('p1 p2 c')
    print(isinstance(SalesStrategy.OFF(p1,p2,c), sp.Expr))
