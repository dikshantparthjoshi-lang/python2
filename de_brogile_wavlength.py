import scipy.constants as const
import matplotlib.pyplot as plt
import calc
import api

# Planck's constant (J·s)
h = const.h

def wavelength_calc(m, v):
    """Calculates De Broglie Wavelength: λ = h / (m * v)"""
    p = calc.multiply(m, v)
    return calc.divide(h, p)

def velocity_calc(m, wavelength):
    """Calculates Particle Velocity: v = h / (m * λ)"""
    p = calc.divide(h, wavelength)
    return calc.divide(p, m)

def atom_mass_to_kg(atomic_mass):
    """Converts atomic mass units (u) to kilograms (kg)"""
    return atomic_mass * 1.66053906660e-27

def get_float_input(prompt):
    """Helper function to safely get positive floating-point input from user."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Input must be a positive number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_single_option():
    """Handles standard single-value calculations."""
    option = input("Enter what to calculate (wavelength / velocity / element): ").strip().lower()
    while option not in ["wavelength", "velocity", "element"]:
        print("Invalid choice. Please choose 'wavelength', 'velocity', or 'element'.")
        option = input("Enter what to calculate (wavelength / velocity / element): ").strip().lower()

    if option == "wavelength":
        m = get_float_input("Enter mass of particle in kg: ")
        v = get_float_input("Enter velocity of particle in m/s: ")
        wavelength = wavelength_calc(m, v)
        print(f"-> De Broglie wavelength: {wavelength:.5e} meters")# '.5e' converts to scientific notation with 5 decimal places

    elif option == "velocity":
        m = get_float_input("Enter mass of particle in kg: ")
        wavelength = get_float_input("Enter De Broglie wavelength in meters: ")
        velocity = velocity_calc(m, wavelength)
        print(f"-> Velocity of particle: {velocity:.5e} m/s")

    elif option == "element":
        symbol = input("Enter element Symbol (e.g., H, He, Fe): ").strip()
        element_info = api.get_element_data(symbol)
        while not element_info:
            print(f"Element symbol '{symbol}' not found in database.")
            symbol = input("Please enter a valid element Symbol: ").strip()
            element_info = api.get_element_data(symbol)

        atomic_mass = element_info["atomic_mass"]
        mass_kg = atom_mass_to_kg(atomic_mass)
        symbol_fmt = element_info["symbol"]
        print(f"Loaded Element: {element_info['name']} ({symbol_fmt}) | Mass: {atomic_mass} u ({mass_kg:.5e} kg)")

        choice = input(f"Calculate wavelength or velocity for {symbol_fmt}? (wavelength/velocity): ").strip().lower()
        while choice not in ["wavelength", "velocity"]:
            choice = input("Invalid option. Enter 'wavelength' or 'velocity': ").strip().lower()
 
        if choice == "wavelength":
            v = get_float_input("Enter velocity of particle in m/s: ")
            wavelength = wavelength_calc(mass_kg, v)
            print(f"-> De Broglie wavelength of {symbol_fmt}: {wavelength:.5e} meters")
        else:
            wavelength = get_float_input("Enter De Broglie wavelength in meters: ")
            velocity = velocity_calc(mass_kg, wavelength)
            print(f"-> Velocity of {symbol_fmt}: {velocity:.5e} m/s")

def compare_values():
    """Handles optional side-by-side comparison with bar plots."""
    print("\n--- Comparison Tool ---")
    comp = input("What do you want to compare? (wavelength / velocity): ").strip().lower()
    while comp not in ["wavelength", "velocity"]:
        comp = input("Please select either 'wavelength' or 'velocity': ").strip().lower()

    if comp == "wavelength":
        print("\nEntry 1:")
        m1 = get_float_input("Enter mass 1 (kg): ")
        v1 = get_float_input("Enter velocity 1 (m/s): ")
        wl1 = wavelength_calc(m1, v1)

        print("\nEntry 2:")
        m2 = get_float_input("Enter mass 2 (kg): ")
        v2 = get_float_input("Enter velocity 2 (m/s): ")
        wl2 = wavelength_calc(m2, v2)

        # Plot comparison
        plt.figure(figsize=(7, 5))
        plt.bar(["Particle 1", "Particle 2"], [wl1, wl2], color=['#2b5c8f', '#d95f02'])
        plt.ylabel("Wavelength (m)")
        plt.title("De Broglie Wavelength Comparison")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

    elif comp == "velocity":
        print("\nEntry 1:")
        m1 = get_float_input("Enter mass 1 (kg): ")
        wl1 = get_float_input("Enter wavelength 1 (m): ")
        vel1 = velocity_calc(m1, wl1)

        print("\nEntry 2:")
        m2 = get_float_input("Enter mass 2 (kg): ")
        wl2 = get_float_input("Enter wavelength 2 (m): ")
        vel2 = velocity_calc(m2, wl2)

        # Plot comparison
        plt.figure(figsize=(7, 5))
        plt.bar(["Particle 1", "Particle 2"], [vel1, vel2], color=["#1469C5", '#d95f02'])
        plt.ylabel("Velocity (m/s)")
        plt.title("Velocity Comparison")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()

def main():
    print("Initializing De Broglie Wavelength Calculator...")
    elements_db = api.fetch_all_elements()
    
    if not elements_db:
        print("Warning: Could not connect to element API database. Element features will be limited.")

    while True:
        calculate_single_option()
        
        want_compare = input("\nDo you want to compare two values on a chart? (yes/no): ").strip().lower()
        while want_compare not in ["yes", "no"]:
            want_compare = input("Please enter 'yes' or 'no': ").strip().lower()

        if want_compare == "yes":
            compare_values()

        again = input("\nRun another calculation? (yes/no): ").strip().lower()
        if again != "yes":
            print("Exiting calculator. Goodbye!")
            break

main()