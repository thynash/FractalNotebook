"""Fractal Shapes Generator package."""

from .Mandelbrot import generate_mandelbrot_set, mandelbrot_description
from .Julia import generate_julia_set, julia_description
from .Koch_Snowflake import generate_koch_snowflake, koch_snowflake_description
from .Lecy_O_Curve import generate_levy_curve
from .Pythagoras_Tree import generate_pythagoras_tree
from .Sierpinnski_triangle import generate_sierpinski_triangle
from .Sierpinski_Carpet import generate_sierpinski_carpet
from .Dragon_Curve import generate_dragon_curve
from .Cantour_Set import generate_cantor_set
from .Barnsley_Fern import generate_barnsley_fern
from .Hilbert_Curve import generate_hilbert_curve
from .Peano_Curve import generate_peano_curve
from .Newton_Fractal import generate_newton_fractal

__all__ = [
    "generate_mandelbrot_set", "mandelbrot_description",
    "generate_julia_set", "julia_description",
    "generate_koch_snowflake", "generate_levy_curve",
    "generate_pythagoras_tree", "generate_sierpinski_triangle",
    "generate_sierpinski_carpet", "generate_dragon_curve",
    "generate_cantor_set", "generate_barnsley_fern",
    "generate_hilbert_curve", "generate_peano_curve",
    "generate_newton_fractal","koch_snowflake_description"
]

