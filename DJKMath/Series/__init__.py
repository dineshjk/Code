"""
Series/__init__.py
Expose commonly used utilities by default when importing from Utils.
"""
from .trigo_sin_cos_tan import (
    sine_power_series,
    cosine_power_series,
    tangent_power_series
)

__all__ = [
    'sine_power_series',
    'cosine_power_series',
    'tangent_power_series'
]