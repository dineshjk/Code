"""
test_utils.py
This is test files that will go on changing.
Currently testing Menu and Keyboard input.
"""
# test_utils.py

# This is test files that will go on changing.

import sys
import os

# Add parent directory to Python path to find Utils package
#sys.path.append(".")
#sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# According to many help files the least preferred and volatile is first one.
# The second is robust
# The third is the most robust and preferred.


from Utils import get_integer, operate_menu, clear_screen, get_single_key,get_bunch_integers
from number_theory import all_divisors, is_prime, gcd_numbers, lcm_numbers



def main():

    menu_items = [
        ("[G] Greatest Common Divisor", "G", "gcd_numbers"),
        ("[L] Least Common Multiple", "L", "lcm_numbers"),
        ("[Q] Quit", "Q", "QUIT")
    ]
    clear_screen()
    # print("Welcome to the GCD Calculator!")
    while True:
        # Step 1 Decide function.
        selected_func = operate_menu(menu_items, begin_message="Welcome to the Arithmetic Utility!", end_message="Select Option")
        if selected_func is None:
            print("\nExiting...")
            break
        elif selected_func == "QUIT":
            print("\nExiting...")
            break
        elif selected_func == "gcd_numbers":
            clear_screen()
            begin_message = "GCD Sub Menu"
            end_message = "Select Option"
            # Step 2 Decide sub function.
            sub_menu_items = [
                ("[Y] How many numbers is known to me", "Y", "get_integer"),
                ("[N] How many numbers is not known to me", "N", "get_bunch_integers"),
                ("[R] Return to Main Menu", "R", "RETURN")

            ]
            while True:
                selected_func = operate_menu(sub_menu_items, begin_message, end_message)
                if selected_func is None:
                    print("\nExiting to previous menu...")
                    get_single_key("Press any key to continue...")
                    clear_screen()
                    break
                elif selected_func == "RETURN":
                    print("\nExiting to previous menu...")
                    get_single_key("Press any key to continue...")
                    clear_screen()
                    break
                elif selected_func == "get_integer":
                    clear_screen()
                    num_count = get_integer("How many numbers do you want to find the GCD for? ")
                    numbers = []
                    get_bunch_integers(numbers, num_count)
                    print(f"You entered: {numbers}")
                    gcd_result = gcd_numbers(numbers)
                    print(f"The GCD of {numbers} is: {gcd_result}")
                    get_single_key("Press any key to continue...")
                elif selected_func == "get_bunch_integers":
                    clear_screen()
                    numbers = []
                    get_bunch_integers(numbers)
                    print(f"You entered: {numbers}")
                    gcd_result = gcd_numbers(numbers)
                    print(f"The GCD of {numbers} is: {gcd_result}")
                    get_single_key("Press any key to continue...")
                else:
                    print("Invalid selection. Please try again.")
                    get_single_key("Press any key to continue...")
        elif selected_func == "lcm_numbers":
            clear_screen()
            begin_message = "LCM Sub Menu"
            end_message = "Select Option"
            # Step 2 Decide sub function.
            sub_menu_items = [
                ("[Y] How many numbers is known to me", "Y", "get_integer"),
                ("[N] How many numbers is not known to me", "N", "get_bunch_integers"),
                ("[R] Return to Main Menu", "R", "RETURN")

            ]
            while True:
                selected_func = operate_menu(sub_menu_items, begin_message, end_message)
                if selected_func is None:
                    print("\nExiting to previous menu...")
                    get_single_key("Press any key to continue...")
                    clear_screen()
                    break
                elif selected_func == "RETURN":
                    print("\nExiting to previous menu...")
                    get_single_key("Press any key to continue...")
                    clear_screen()
                    break
                elif selected_func == "get_integer":
                    clear_screen()
                    num_count = get_integer("How many numbers do you want to find the GCD for? ")
                    numbers = []
                    get_bunch_integers(numbers, num_count)
                    print(f"You entered: {numbers}")
                    lcm_result = lcm_numbers(numbers)
                    print(f"The LCM of {numbers} is: {lcm_result}")
                    get_single_key("Press any key to continue...")
                elif selected_func == "get_bunch_integers":
                    clear_screen()
                    numbers = []
                    get_bunch_integers(numbers)
                    print(f"You entered: {numbers}")
                    lcm_result = lcm_numbers(numbers)
                    print(f"The LCM of {numbers} is: {lcm_result}")
                    get_single_key("Press any key to continue...")
                else:
                    print("Invalid selection. Please try again.")
                    get_single_key("Press any key to continue...")








if __name__ == "__main__":
    main()
