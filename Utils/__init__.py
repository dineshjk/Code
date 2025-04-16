"""
Utils package initialization.
Contains utility functions for menu operations and input handling.
"""

from .keyboard_utils import (
    clear_screen,
    get_single_key,
    wait_for_key
)

from .inout import (
    get_integer,
    get_float,
    get_complex,  # Add the new function
    get_bunch_integers,
    get_bunch_floats,
    get_bunch_complex  # Add the new function
)

from .menu_utils import (
    operate_menu,
    show_menu
)

__all__ = [
    'clear_screen',
    'get_single_key',
    'wait_for_key',
    'get_integer',
    'get_float',
    'get_complex',  # Add to __all__
    'operate_menu',
    'show_menu',
    'get_bunch_integers',
    'get_bunch_floats',
]
