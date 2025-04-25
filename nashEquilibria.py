from __future__ import annotations
import sympy as sp
"""
主に使用するライブラリです（もう先輩は卒業してしまって開発する意味はないのですが．．．）
Pythonに慣れるためであったり，便利だけど割とレガシーなSympyライブラリの便利な一部分を切り取って，モダンなPythonで仕上げていくことが目的です．
"""

# 利潤の計算式を保持するクラス
# 順次salesStrategyに置き換えていく予定
class Profit:
    profit = {'off':lambda P,Q,c: Q*(P-2*c),
                'hy':lambda P,Q,c: Q*(P-c),
                'on':lambda P,Q,c: Q*(P)}
    """
    Javaのstaticコンストラクタを模したものだったが，pythonはインスタンス化が容易であるためいらない．
    削除予定
    """
    @staticmethod
    def of(strategyName :str):
        return Profit.profit[strategyName]
    def of(strategyName :str):
        return lambda cost :lambda price, quantity:Profit.profit[strategyName](price,quantity,cost)
    
def oneminus(x):
    1-x
"""
実際に利用してもらうクラス．
`game.py` を直接利用しないで，卒論の主な検証作業はこれでできるようにする．
newConditionsが卒論の章番号に対応しているので，そこから，簡単にこのクラスを利用できる関数も追加したい．
"""
class MarketData:
    
    # 価格
    Pa,Pb = sp.symbols('Pa,Pb' ,positive=True)

    # コスト
    c = sp.Symbol('c' ,positive=True)

    firms :dict[str,int]={'a':0,'b':1}

    """
    使うときに必要最低限の引数だけでインスタンス化ができるように当時作ったが，改修していくにつれて場当たり的な感じが否めない．
    データコンテナ化して，もっと均衡計算ロジックとデータ格納を分離していきたい．だいたい，メソッドにすればいいところが
    フィールドになっていてダサい．
    """
    def __init__(self,
                 quantity_a,
                 strategyName_a: str,
                 strategyName_b: str
                ):
        self.Qa = quantity_a
        self.Qb = lambda pa,pb: oneminus(self.Qa(pa,pb)) # 実行時に
        self.Strgy_a, self.Strgy_b= strategyName_a, strategyName_b
        self.pi_a, self.pi_b = Profit.of(self.Strgy_a), Profit.of(self.Strgy_b)

    def solveEq(self):
        pa, pb = self.Pa, self.Pb
        c = self.c

        qa, qb = self.Qa(pa,pb), self.Qb(pa,pb)
        pi_a, pi_b = self.pi_a(pa,qa,c), self.pi_b(pb,qb,c)
        eq_1, eq_2 = sp.Eq(sp.diff(pi_a, pa), 0), sp.Eq(sp.diff(pi_b, pb), 0)
        eqPrices = sp.solve([eq_1,eq_2],[pa,pb])
        return eqPrices

def geqZero(expression:sp.Expr):
    return sp.solve(sp.GreaterThan(expression,0))

def optimalEquation(utilityFunc : sp.Expr, strategy: sp.Symbol)->sp.Eq:
    marginalUtility=sp.diff(utilityFunc, strategy)
    return sp.Eq(marginalUtility,0)

if __name__ == "__main__":
    st=sp.Symbol('st')
    c=sp.Symbol('c')
    utilityFunc=(st-c)**2
    optSt=optimalEquation(utilityFunc, st)
    print(optSt)
