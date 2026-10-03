import calc 
import scipy.constants as const
# h=6.62607015e-34 # Planck's constant in J*s
# lambda = h/p , p= m*v

h= const.h
m= float(input("Enter mass of particle in kg: "))
v= float(input("Enter velocity of particle in m/s: "))
p= calc.multiply(m, v)
wavelength = calc.divide(h,p)
print("De Broglie wavelength is:", wavelength)
