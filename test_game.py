import pytest
import sympy as sp
from game import optimalEquation, equilibriate, safeSolve, dictToTuple
"""
以下をテストしたい
if __name__ == "__main__":
    x,y,c = sp.symbols('x y c')
    # Example usage of optimalEquation function
    e0=safeSolve([sp.Eq(x**2,2)],[x])
    print(e0)  # Output: [(-sqrt(2),),(-sqrt(2),)]
    e1=safeSolve([sp.Eq(x-1, 0), sp.Eq(y-3, 0)], [x, y])
    print(e1)  # Output: [(1,3)]
    e2=safeSolve([sp.Eq(1+1, 3)], [x])
    print(e2)  # Output: []
    e3=safeSolve([sp.Eq(x-1-y, 0), sp.Eq(y-3, 0)], [x])
    print(e3)  # ValueError: Number of equations must match number of strategies 
    e4=safeSolve([sp.Eq(x-1-y, 0)], [x,y])
    print(e4)  # ValueError: Number of equations must match number of strategies 
    ne0=equilibriate((sp.Eq(x**2-2, 0),x), (sp.Eq(y-3, 0),y))
    print(ne0) # Output: [(-sqrt(2),3),(-sqrt(2),3)]

"""

x, y, c = sp.symbols("x y c")

def test_dict_to_tuple_empty():
    assert dictToTuple({}) == ()

def test_dict_to_tuple_single():
    assert dictToTuple({x: -1}) == (-1,)

def test_dict_to_tuple_multiple():
    assert dictToTuple({x: c - 1, y: c - 2}) == (c - 1, c - 2)

def test_safe_solve_linear():
    assert safeSolve([sp.Eq(x - 1, 0), sp.Eq(y - 3, 0)], [x, y]) == [(1, 3)]

def test_safe_solve_quadratic():
    assert safeSolve([sp.Eq(x**2, 2)], [x]) == [(-sp.sqrt(2),), (sp.sqrt(2),)]

def test_safe_solve_invalid_equation():
    assert safeSolve([sp.Eq(1 + 1, 3)], [x]) == []

def test_safe_solve_no_equations():
    with pytest.raises(ValueError, match="Equations and strategies must not be empty"):
        safeSolve([], [])
    with pytest.raises(ValueError, match="Equations and strategies must not be empty"):
        safeSolve([], [x,y])
    with pytest.raises(ValueError, match="Equations and strategies must not be empty"):
        safeSolve([sp.Eq(x - 1, 0)], [])

def test_safe_solve_mismatched_variables():
    with pytest.raises(ValueError, match="Number of equations must match number of strategies"):
        safeSolve([sp.Eq(x - 1 - y, 0), sp.Eq(y - 3, 0)], [x])
    
    with pytest.raises(ValueError, match="Number of equations must match number of strategies"):
        safeSolve([sp.Eq(x - 1 - y, 0)], [x, y])

def test_equilibriate():
    expected = [(-sp.sqrt(2), 3), (sp.sqrt(2), 3)]
    assert equilibriate((sp.Eq(x**2 - 2, 0), x), (sp.Eq(y - 3, 0), y)) == expected

def test_equlibriate_with_symbols():
    expected = [(-sp.sqrt(c), c),(sp.sqrt(c), c)]
    assert equilibriate((sp.Eq(x**2 - y, 0), x), (sp.Eq(y - c, 0), y)) == expected

def test_equilibriate_empty():
    assert equilibriate() == []

def test_equilibriate_originallyDict():
    # Original implementation returns dict like `{x: c, y: c}`
    # when there exists single equilibrium.
    # However, it returns a list of tuple like `[(-sp.sqrt(c), c),(sp.sqrt(c), c)]`
    # when there exist more than two equilibria.
    # This test checks if the output is a list of tuples.
    # 
    expected = [(c,c)]
    assert equilibriate((x-y,x),(y-c,y)) == expected

ignore = sp.symbols('ignore')
def test_optimal_equation():
    assert optimalEquation(c, x) == sp.Eq(0, 0)
    # This equation is not valid, but it is a test case 
    # because this is not `optimalEquation` 's bussiness.
    assert optimalEquation(x, x) == sp.Eq(1, 0)
    assert optimalEquation(x**2 + y**2-c, x) == sp.Eq(2*x, 0)
    assert optimalEquation(x**2 + y**2, y) == sp.Eq(2*y, 0)
    assert optimalEquation(x**2 + y**2, ignore) == sp.Eq(0, 0)
    assert optimalEquation(x**2 + c*x*y, x) == sp.Eq(2*x+c*y, 0)