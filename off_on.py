import sympy as sp
x,y = sp.symbols('x,y')
Pa,Pb,c = sp.symbols('Pa,Pb,c')
Qb=(Pa-Pb+2)**2/8
Qa=1-Qb
pi_a=Qa*(Pa-2*c)
pi_b=Qb*Pb
eq_1 = sp.Eq(sp.diff(pi_a, Pa), 0)
eq_2 = sp.Eq(sp.diff(pi_b, Pb), 0)
Pfn = sp.solve([eq_1,eq_2],[Pa,Pb])
# a=[(x1,y1),(x2,y2)] []:List, ():Tuple
# a[0] = (x1,y1), a[0][0] = (x1,y1)[0] = x1
# Pfn >>> [(3*c/4 - 3*sqrt(c**2 + 2*c + 9)/4 - 5/4, c/4 - sqrt(c**2 + 2*c + 9)/4 + 1/4), (3*c/4 + 3*sqrt(c**2 + 2*c + 9)/4 - 5/4, c/4 + sqrt(c**2 + 2*c + 9)/4 + 1/4)]
Pfn_nash = Pfn[1]
pi_a_nash = sp.simplify(pi_a.subs([(Pa,Pfn_nash[0]),(Pb,Pfn_nash[1])]))
pi_b_nash = sp.simplify(pi_b.subs([(Pa,Pfn_nash[0]),(Pb,Pfn_nash[1])]))
