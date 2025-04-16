# DJKMath Library

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.x-green.svg)

A Python library implementing high-precision trigonometric functions using power series expansions.

## Installation

1. Clone the repository:
```cmd
git clone https://github.com/dineshjk/Code.git
cd Code
```

2. Install required packages:
```cmd
pip install mpmath
```

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