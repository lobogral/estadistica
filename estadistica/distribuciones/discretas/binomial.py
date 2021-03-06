"""Ofrece una clase para manejo de la distribución binomial."""
from sympy import Piecewise
from sympy import Expr
from sympy import binomial as nC
from estadistica.distribuciones.dist_disc import DistDisc
from estadistica.distribuciones.dist_conc import DistConc


class Binomial(DistConc):
    """Ofrece funcionalidades para distribución binomial."""

    def __init__(self,
                 var: Expr,
                 prob_exito: float,
                 num_ensa: int) -> None:
        """Inicializa la clase.

        Establece valores concretos para que se pueda
        crear la distribución.

        Parameters
        ----------
        var
            Variable
        num_ensa
            Número de ensayos independientes
        prob_exito
            Probabilidad de éxito
        """
        prob_fracaso = 1 - prob_exito
        func_dist = Piecewise((
            nC(num_ensa, var)*(prob_exito**var)*(prob_fracaso**(num_ensa-var)),
            (var >= 0) & (var <= num_ensa)))
        self.dist = DistDisc()
        self.dist.est_func_dist(func_dist)
