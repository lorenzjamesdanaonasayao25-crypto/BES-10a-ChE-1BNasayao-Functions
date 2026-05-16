#This project is a calculator that is based on the amount of moles needed from the user with the usual reagents used in laboratory experiments.
#The reagents that were commonly used in our laboratory experiments as a first year ChE Student are:
#NaOH, NH4OH, KOH, HCl, H2SO4, H3PO4, KHP

inyou = input('Hello! Please state your name: ')
inREAG = input('Enter Name of Reagent Needed: ')
inMOL = input('Enter Amount of Moles Needed: ')
    #input variables
    #inyou is a variable that defines the user's name
    #inREAG is a variable that states what reagent is needed by the user
    #inMOL is the amount of moles needed from the said reagent

molNaOH = 39.997
molNH4OH = 35.046
molKOH = 56.110
molHCl = 36.458
molH2SO4 = 98.073
molH3PO4 = 97.994
molKHP = 204.22
    #The list above shows the molar mass of the usual reagents used in laboratories, especially in titrations.


def calc_and_print(reagent, moles, molar_mass):
    grams = float(moles) * float(molar_mass)
    print("The amount of grams needed for", moles, "M", reagent, "is", grams)
    #custom function defined using Chapter 4 concepts
    #This function takes the three inputs, calculates the grams, and prints the final sentence all at once.


#conditional functions and calculations
if inREAG == "NaOH":
    calc_and_print(inREAG, inMOL, molNaOH)

elif inREAG == "NH4OH":
    calc_and_print(inREAG, inMOL, molNH4OH)

elif inREAG == "KOH":
    calc_and_print(inREAG, inMOL, molKOH)

elif inREAG == "HCl":
    calc_and_print(inREAG, inMOL, molHCl)

elif inREAG == "H2SO4":
    calc_and_print(inREAG, inMOL, molH2SO4)

elif inREAG == "H3PO4":
    calc_and_print(inREAG, inMOL, molH3PO4)

elif inREAG == "KHP":
    calc_and_print(inREAG, inMOL, molKHP)

else:
    print("Invalid Reagent Name. Name does not correlate to Inventory")

#The output will show the amount of grams needed to achieve the amount of moles asked by the user for the reagent they needed.