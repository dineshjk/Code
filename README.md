# DJKMath Library

A Python library implementing high-precision trigonometric functions using power series expansions.

## Features
- Power series implementations of trigonometric functions:
  - Sine, Cosine, Tangent
  - Secant, Cosecant, Cotangent
- Arbitrary precision using mpmath library
- Support for both degree and radian inputs
- Degree-Minute-Second (DMS) angle input
- Built-in comparison with mpmath functions

## Project Structure
```
Code/
├── DJKMath/
│   ├── Series/
│   │   ├── trigo_sin_cos_tan.py
│   │   └── test_inout.py
│   └── Arithmetic/
│       └── number_theory.py
├── Utils/
│   ├── inout.py
│   ├── keyboard_utils.py
│   └── menu_utils.py
```

## Dependencies
- Python 3.x
- mpmath library
- Windows OS (for keyboard utilities)

## Usage
```python
python DJKMath/Series/trigo_sin_cos_tan.py
```

## Author
Dinesh Karia
16 April 2025