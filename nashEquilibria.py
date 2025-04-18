from __future__ import annotations
import sympy as sp


# 利潤の計算式を保持するクラス
class Profit:
    profit = {'off':lambda P,Q,c: Q*(P-2*c),
                'hy':lambda P,Q,c: Q*(P-c),
                'on':lambda P,Q,c: Q*(P)}
    @staticmethod
    def of(strategyName :str):
        return Profit.profit[strategyName]
    def of(strategyName :str):
        return lambda cost :lambda price, quantity:Profit.profit[strategyName](price,quantity,cost)
    
def oneminus(x):
    1-x

class MarketData:
    
    # 価格
    Pa,Pb = sp.symbols('Pa,Pb' ,positive=True)

    # コスト
    c = sp.Symbol('c' ,positive=True)

    firms :dict[str,int]={'a':0,'b':1}


    def __init__(self,
                 quantity_a,
                 strategyName_a: str,
                 strategyName_b: str
                ):
        self.Qa = quantity_a
        self.Qb = lambda pa,pb: oneminus(self.Qa(pa,pb))
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



#    @staticmethod
#    def solveEqLogicWithStronglyConvexUtilityFunctions(cls,utilityFuncs,)


def geqZero(expression):
    return sp.solve(sp.GreaterThan(expression,0))

