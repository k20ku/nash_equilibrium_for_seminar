from typing import Callable
import sympy as sp
from salesStrategy import SalesStrategy
import dataclasses
# python -m src.ne.nerefined

@dataclasses.dataclass
class Quantity:
    qunatity_lambda: Callable[[sp.Expr, sp.Expr], sp.Expr]

    def toExpr(self, price0: sp.Expr, price1: sp.Expr) -> sp.Expr:
        return self.Qa(price0, price1)

if __name__ == "__main__":
    P1, P2, cost = sp.symbols('P1 P2 c')
    qunatity_lambda0 = lambda p1, p2: 1 - p1 - p2
    Q = Quantity(qunatity_lambda0)
    print(Q.toExpr(P1, P2))  # Output: 1 - P1 - P2
    print(1-Q.toExpr(P1, P2))  # Output: P1 + P2 - 1
    print(SalesStrategy.OFF(P1,1-Q.toExpr(P1, P2),cost))
    utilityFunc1 = SalesStrategy.OFF(P1,1-Q.toExpr(P1, P2),cost)
    # print(optimalEquation(utilityFunc1, P1)) # optimalEquationが見つからないと言われる