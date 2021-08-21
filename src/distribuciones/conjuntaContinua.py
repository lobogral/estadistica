from sympy import integrate, Piecewise, oo
from sympy import simplify, piecewise_fold, Symbol

x = Symbol("x", real=True)
y = Symbol("y", real=True)

def __AgregarIntervalo(función, intervalo):
    funcionTrozos = Piecewise((función, intervalo),(0, True))
    return piecewise_fold(funcionTrozos)

def ProbTotal(función):
    variables = función.atoms(Symbol)
    lista = [(variable, -oo, oo) for variable in variables]
    return integrate(función, *lista)

def Prob(función, intervalo):
    nuevaFunc = __AgregarIntervalo(función, intervalo)
    return ProbTotal(nuevaFunc)

def ProbMarginal(función, variable):
    variable = y if variable == x else x
    integral = integrate(función, (variable,-oo,oo))
    return simplify(piecewise_fold(integral.rewrite(Piecewise)))

def ProbCondicional(función, intervaloDep, varIndep, valIndep):
    varDep = y if varIndep == x else x
    funcCond = función/ProbMarginal(función, varIndep)
    funcCondEval = simplify(funcCond.subs(varIndep, valIndep))
    funcCondEvalInt = __AgregarIntervalo(funcCondEval, intervaloDep)
    return integrate(funcCondEvalInt, (varDep, -oo, oo))