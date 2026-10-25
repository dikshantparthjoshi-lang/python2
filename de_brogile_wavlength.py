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
    element = input("Do you want to calculate velocity and wavelength for which element: ").strip().lower()
    x= api.get_element_data(element)
    if x is None:# ye error ko dekhna ek bar kyuki chatgpt ka tareka ka architecture sahi hai hum while ki jagaha if use kar rahe hai idhar par
        print("Provide a valid element symbol.")
        element= input("Do you want to calculate velocity and wavelength for which element:  ")
    
    option = input(f"Enter what to calculate for '{api.get_element_data(element)["name"]}' wavelength or velocity: ").strip().lower()
    while option not in ["wavelength", "velocity"]:
        print("Invalid choice. Please choose 'wavelength' or 'velocity'.")
        option = input(f"Enter what to calculate for '{element}' (wavelength / velocity ): ").strip().lower()

    if option == "wavelength":# update needed here check the code precisily
        element_info = api.get_element_data(element)
        atomic_mass = element_info["atomic_mass"]
        mass_kg = atom_mass_to_kg(atomic_mass)
        symbol_fmt = element_info["symbol"]
        print(f"Loaded Element: {element_info['name']} ({symbol_fmt}) | Mass: {atomic_mass} u ({mass_kg:.5e} kg)")

        
        v = get_float_input("Enter velocity of particle in m/s: ")
        wavelength = wavelength_calc(mass_kg, v)
        print(f"-> De Broglie wavelength of {symbol_fmt}: {wavelength:.5e} meters")
    elif option=="velocity":
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
        wl1 = get_float_input("Enter wavelength 1 (metre): ")
        vel1 = velocity_calc(m1, wl1)

        print("\nEntry 2:")
        m2 = get_float_input("Enter mass 2 (kg): ")
        wl2 = get_float_input("Enter wavelength 2 (m): ")
        vel2 = velocity_calc(m2, wl2)

        # Plot comparison
        plt.figure(figsize=(7, 5))
        plt.bar(["Particle 1", "Particle 2"], [vel1, vel2], color=["#1469C5", "#C10F0F"])
        plt.ylabel("Velocity (m/s)")
        plt.title("Velocity Comparison")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
        

def main():
    print("Initializing De Broglie Wavelength Calculator...")
    print("if you want to insert value in y\u02e3 whether value x value is positive or negative and y is can be any positive value.")
    print("Please insert in the form of 'yex', for example 5.13e-13 represents 5.13*10⁻¹³")
    elements_db = api.fetch_all_elements()
    while True:
        if not elements_db:
            print("Warning: Could not connect to element API database. Element features will be limited.")
            print("Please check your internet connection or try again later.")
            print("You can still perform standard calculations without element data.")
            l=input(f"Do you want to just calculate a single value or compare two values \"with graph\"(single/double): ").strip().lower()
            if l== "single":
                api_limit_check()
            if l== "double":
                k = input("What do you want to cṇalculate? (wavelength / velocity): ").strip().lower()
                while k not in ["wavelength", "velocity"]:
                    print("Invalid choice. Please choose 'wavelength' or 'velocity'.")
                    k = input("What do you want to calculate? (wavelength / velocity): ").strip().lower()
                if k=="wavlength":
                    m1 = get_float_input("Enter mass of particle in kg: ")
                    v1 = get_float_input("Enter velocity of particle in m/s: ")
                    wavelength1 = wavelength_calc(m1, v1)
                    print(f"-> De Broglie wavelength: {wavelength1:.5e} meters")
                    m2 = get_float_input("Enter mass of particle in kg: ")
                    v2 = get_float_input("Enter velocity of particle in m/s: ")
                    wavelength2 = wavelength_calc(m2, v2)
                    print(f"-> De Broglie wavelength: {wavelength2:.5e} meters")
                    plt.figure(figsize=(7, 5))
                    plt.bar(["Particle1","Particle2"],[wavelength1,wavelength2],color=["#1469C5", "#C10F0F"])
                    plt.title("Wavelength Comparison")
                    plt.ylabel("Wavelength (metre)")
                    plt.grid(axis='y', linestyle='--', alpha=0.7)
                    plt.show()
                if k=="velocity":
                    m1 = get_float_input("Enter mass of particle in kg: ")
                    wavelength1 = get_float_input("Enter De Broglie wavelength in meters: ")
                    velocity1 = velocity_calc(m1, wavelength1)
                    print(f"-> Velocity of particle: {velocity1:.5e} m/s")
                    m2 = get_float_input("Enter mass of particle in kg: ")
                    wavelength2 = get_float_input("Enter De Broglie wavelength in meters: ")
                    velocity2 = velocity_calc(m2, wavelength2)
                    print(f"-> Velocity of particle: {velocity2:.5e} m/s")
                    plt.figure(figsize=(7, 5))
                    plt.bar(["Particle 1", "Particle 2"], [velocity1, velocity2], color=["#1469C5", "#C10F0F"])
                    plt.ylabel("Velocity (m/s)")
                    plt.title("Velocity Comparison")
                    plt.grid(axis='y', linestyle='--', alpha=0.7)
                    plt.show()
                    
        elif elements_db:
                l= input("Do you want to just calculate a single value or compare two values \"with graph\"(single/double):")
                while l not in ["single","double"]:
                    l= input("Invalid Input. Please enter either single or double:")
                k= input(f"Do you want to create {l} value calculation element or standard (element/standard): ")
                while k not in ["element","standard"]:
                    k= input("Invalid Input. Please either element or standard:")
                if k=="element":
                    if l=="single":
                        calculate_single_option()
                    elif l=="double":
                        x= input("Do you want to do calculation for same element or different element(same/different):")
                        while x not in ["same","different"]:
                            x= input("Invalid Input. Either input same or different:")
                        if x=="same":
                            compare_values_same_element()
                        if x=="different":
                            compare_values_element()
                if k=="standard":
                    if l=="single":
                        api_limit_check()
                    if l=="double":
                        k = input("What do you want to calculate? (wavelength / velocity): ").strip().lower()
                        while k not in ["wavelength", "velocity"]:
                            print("Invalid choice. Please choose 'wavelength' or 'velocity'.")
                            k = input("What do you want to calculate? (wavelength / velocity): ").strip().lower()
                        if k=="wavlength":
                            m1 = get_float_input("Enter mass of particle in kg: ")
                            v1 = get_float_input("Enter velocity of particle in m/s: ")
                            wavelength1 = wavelength_calc(m1, v1)
                            print(f"-> De Broglie wavelength: {wavelength1:.5e} meters")
                            m2 = get_float_input("Enter mass of particle in kg: ")
                            v2 = get_float_input("Enter velocity of particle in m/s: ")
                            wavelength2 = wavelength_calc(m2, v2)
                            print(f"-> De Broglie wavelength: {wavelength2:.5e} meters")
                            plt.figure(figsize=(7, 5))
                            plt.bar(["Particle1","Particle2"],[wavelength1,wavelength2],color=["#1469C5", "#C10F0F"])
                            plt.title("Wavelength Comparison")
                            plt.ylabel("Wavelength (metre)")
                            plt.grid(axis='y', linestyle='--', alpha=0.7)
                            plt.show()
                        if k=="velocity":
                            m1 = get_float_input("Enter mass of particle in kg: ")
                            wavelength1 = get_float_input("Enter De Broglie wavelength in meters: ")
                            velocity1 = velocity_calc(m1, wavelength1)
                            print(f"-> Velocity of particle: {velocity1:.5e} m/s")
                            m2 = get_float_input("Enter mass of particle in kg: ")
                            wavelength2 = get_float_input("Enter De Broglie wavelength in meters: ")
                            velocity2 = velocity_calc(m2, wavelength2)
                            print(f"-> Velocity of particle: {velocity2:.5e} m/s")
                            plt.figure(figsize=(7, 5))
                            plt.bar(["Particle 1", "Particle 2"], [velocity1, velocity2], color=["#1469C5", "#C10F0F"])
                            plt.ylabel("Velocity (m/s)")
                            plt.title("Velocity Comparison")
                            plt.grid(axis='y', linestyle='--', alpha=0.7)
                            plt.show()
                    
                
               
    
        again = input("\nRun another calculation? (yes/no): ").strip().lower()
        while again not in ["yes","no"]:
            again= input("Invalid Input. Either input yes or no:")
        if again != "yes":
            print("Exiting calculator. Goodbye!")
            break
        
def api_limit_check():
       
    x = input("What do you want to calculate? (wavelength / velocity): ").strip().lower()
    while x not in ["wavelength", "velocity"]:
        print("Invalid choice. Please choose 'wavelength' or 'velocity'.")
        x = input("What do you want to calculate? (wavelength / velocity): ").strip().lower()
    if x == "wavelength":
        m = get_float_input("Enter mass of particle in kg: ")
        v = get_float_input("Enter velocity of particle in m/s: ")
        wavelength = wavelength_calc(m, v)
        print(f"-> De Broglie wavelength: {wavelength:.5e} meters")# '.5e' converts to scientific notation with 5 decimal places
    if x == "velocity":
        m = get_float_input("Enter mass of particle in kg: ")
        wavelength = get_float_input("Enter De Broglie wavelength in meters")
        velocity = velocity_calc(m, wavelength)
        print(f"-> Velocity of particle: {velocity:.5e} m/s")
        
        
def compare_values_element():
    '''Handles optional side-by-side comparison for elements with bar plots (different elements).'''
    l= input("element 1 symbol: ").strip()
    element_info1 = api.get_element_data(l)
    if element_info1 is None:
        print(f"Element symbol '{l}' not found in database.")
        l = input("Please enter a valid element Symbol: ").strip()
        element_info1 = api.get_element_data(l)
    k= input("element 2 symbol: ").strip()
    element_info2 = api.get_element_data(k)
    if element_info2 is None:
        print(f"Element symbol '{k}' not found in database.")
        k = input("Please enter a valid element Symbol: ").strip()
        element_info2 = api.get_element_data(k)
    atomic_mass1 = element_info1["atomic_mass"]
    atomic_mass2 = element_info2["atomic_mass"]
    mass_kg1 = atom_mass_to_kg(atomic_mass1)
    mass_kg2 = atom_mass_to_kg(atomic_mass2)
    t= input("Do you want to compare wavelength or velocity? (wavelength/velocity): ").strip().lower()
    while t not in ["wavelength", "velocity"]:
        print("Invalid choice. Please choose 'wavelength' or 'velocity'.")
        t = input("Please enter 'wavelength' or 'velocity': ").strip().lower()
    if t=='wavelength':
        v1 = get_float_input(f"Enter velocity for {element_info1['name']} in m/s: ")
        v2 = get_float_input(f"Enter velocity for {element_info2['name']} in m/s: ")
        wl1 = wavelength_calc(mass_kg1, v1)
        wl2 = wavelength_calc(mass_kg2, v2)
        plt.figure(figsize=(7, 5))
        plt.bar([element_info1['name'], element_info2['name']], [wl1, wl2], color=['#2b5c8f', '#d95f02'])
        plt.ylabel("Wavelength (metre)")
        plt.title("De Broglie Wavelength Comparison")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
    elif t=='velocity':
        wl1 = get_float_input(f"Enter wavelength for {element_info1['name']} in m: ")
        wl2 = get_float_input(f"Enter wavelength for {element_info2['name']} in m: ")
        vel1 = velocity_calc(mass_kg1, wl1)
        vel2 = velocity_calc(mass_kg2, wl2)
        plt.figure(figsize=(7, 5))
        plt.bar([element_info1['name'], element_info2['name']], [vel1, vel2], color=["#1469C5", "#C10F0F"])
        plt.ylabel("Velocity (m/s)")
        plt.title("Velocity Comparison")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
        
        
def compare_values_same_element():
    '''Handles optional side-by-side comparison for the same element with bar plots.'''
    symbol = input("Enter element Symbol (e.g., H, He, Fe): ").strip()
    element_info = api.get_element_data(symbol)
    if element_info is None:
        print(f"Element symbol '{symbol}' not found in database.")
        symbol = input("Please enter a valid element Symbol: ").strip()
        element_info = api.get_element_data(symbol)
    atomic_mass = element_info["atomic_mass"]
    mass_kg = atom_mass_to_kg(atomic_mass)
    t= input("Do you want to compare wavelength or velocity? (wavelength/velocity): ").strip().lower()
    while t not in ["wavelength", "velocity"]:
        print("Invalid choice. Please choose 'wavelength' or 'velocity'.")
        t = input("Please enter 'wavelength' or 'velocity': ").strip().lower()
        
    if t=='wavelength':
        v1 = get_float_input(f"Enter velocity 1 for {element_info['name']} in m/s: ")
        v2 = get_float_input(f"Enter velocity 2 for {element_info['name']} in m/s: ")
        wl1 = wavelength_calc(mass_kg, v1)
        wl2 = wavelength_calc(mass_kg, v2)
        plt.figure(figsize=(7, 5))
        plt.bar([f"{element_info['name']} (v1)", f"{element_info['name']} (v2)"], [wl1, wl2], color=['#2b5c8f', '#d95f02'])
        plt.ylabel("Wavelength (metre)")
        plt.title(f"De Broglie Wavelength Comparison for {element_info['name']}")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()
        
    elif t=='velocity':
        wl1 = get_float_input(f"Enter wavelength 1 for {element_info['name']} in m: ")
        wl2 = get_float_input(f"Enter wavelength 2 for {element_info['name']} in m: ")
        vel1 = velocity_calc(mass_kg, wl1)
        vel2 = velocity_calc(mass_kg, wl2)
        plt.figure(figsize=(7, 5))
        plt.bar([f"{element_info['name']} (λ1)", f"{element_info['name']} (λ2)"], [vel1, vel2], color=["#1469C5", "#C10F0F"])
        plt.ylabel("Velocity (m/s)")
        plt.title(f"Velocity Comparison for {element_info['name']}")
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.show()


main()