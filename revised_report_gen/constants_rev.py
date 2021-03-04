# CONSTANTS
FLIGHT_BUDGET_MULT = 3.3
COST_PER_TON = 24e6
COST_PER_LAUNCH = 30e6

MISSION_LENGTH = 1100  # in days on the moon
DAYS_PER_YEAR = 365.24

REGOLITH_RETAINMENT_RATE = .5

VOLATILE_REGOLITH_RATIO = {
    # per unit of regolith heated to 700 C
    "N2": 4e-6,
    "CH4": 11e-6,
    "CO2": 12e-6,
    "CO": 13.41e-6,
    "He": 22e-6,
    "He-3": 15.1e-9,
    "H2O": 23e-6,
    "H2": 43e-6
}
# Total = 115e-6
TOTAL_VOLATILE_RATIO = 60e-6
