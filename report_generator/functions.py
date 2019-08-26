from report_generator import constants as cs


# functions


def specific_heat(m, c, dT):
    """
    Returns the heat needed in Joules
    :param m: mass in g
    :param c: specific heat in J/(gK)
    :param dT: change in temperature in kelvin/celsius
    :return: energy required in joules
    """
    return m * c * dT


def mass_regolith_to_retrieve_mass_he3(mass_he3):
    """
    returns the mass of regolith needed to retrieve the mass of he3 specified with inefficiencies
    output units are the same as the input units
    :param mass_he3: mass of he3 in grams
    :return: the mass of regolith required in grams
    """
    return mass_he3 / (cs.He3_CONCENTRATION * cs.REGOLITH_CONVERSION_COEFFICIENT)


def energy_from_mass_he3(mass_he3):
    """
    returns quantity that is generated from a mass of he3 in grams with inefficiencies
    :param mass_he3: mass of he3 in grams
    :return: energy generated in joules
    """
    return (mass_he3/cs.He3_MOLAR_MASS) * cs.AVOGADROS_NUMBER * \
           cs.D_He3_eV_PER_REACTION * cs.eV * cs.D_He3_ELECTRICAL_CONVERSION_COEFFICIENT


def mass_he3_required_for_energy(energy):
    """
    returns the mass of he3 required to generate :param energy from fusion
    :param energy: amount of energy wanted in joules
    :return: mass of He3 in grams
    """
    return (energy / energy_from_mass_he3(cs.He3_MOLAR_MASS)) * cs.He3_MOLAR_MASS


def energy_needed_for_revenue(revenue):
    """
    returns the energy needed to generate the wanted revenue at a set kWh price
    :param revenue: revenue wanted
    :return: energy needed
    """
    return revenue * cs.J_PER_kWH / cs.kWH_PRICE
