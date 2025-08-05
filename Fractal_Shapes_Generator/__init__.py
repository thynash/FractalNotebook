"""Fractal Shapes Generator package."""

from .Mandelbrot import generate_mandelbrot_set, mandelbrot_description
from .Julia import generate_julia_set, julia_description

__all__ = [
    "generate_mandelbrot_set", "mandelbrot_description",
    "generate_julia_set", "julia_description"
]

