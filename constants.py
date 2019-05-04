# --- CONSTANTS --- #
ONE_TON = 1e6  # grams/ton

eV = 1.60218e-19  # J
AVOGADROS_NUMBER = 6.0221409e+23  # unit-less
He3_MOLAR_MASS = 3.00  # g/mol

He3_CONCENTRATION = 15.1e-9  # g He-3/g Lunar Regolith
D_He3_eV_PER_REACTION = 18.3e6  # eV per reaction of D + He-3
# Reaction is D + He-3 -> He + p+ + 18.3 MeV

REGOLITH_CONVERSION_COEFFICIENT = 0.75
# % of He-3 from regolith that is recoverable (The value of 0.75 is at 600 degrees C
D_He3_ELECTRICAL_CONVERSION_COEFFICIENT = 0.65
# Energy retained from conversion, 0 is none, 1 is max

c_LOW_REGOLITH = .21  # J/(gK)
c_HIGH_REGOLITH = .88  # J/(gK)
DESIRED_T = 873.15  # K, 600 C
AMBIENT_T = 400.15  # K, 127 C
DELTA_T = DESIRED_T - AMBIENT_T  # dT

kWH_PRICE = .1  # $USD/kWh
J_PER_kWH = 3.6e6  # J/kWh
REVENUE_DESIRED = 1e9  # $

DAYS_IN_YEAR = 365.24
# --- CONSTANTS --- #

volatile_he3_ratio = {
    "N2": 500,
    "CH4": 1600,
    "CO2": 1700,
    "CO": 1900,
    "He-4": 3100,
    "H2O": 3300,
    "H2": 6100
}
