import constants as cs
import functions as fn
import si_formatter as si

print("Welcome to Mars Colony::Project HELIOS Calculations")


def print_report(revenue_desired=cs.REVENUE_DESIRED):
    """
    generates report
    :param revenue_desired: revenue desired
    :return: prints the report
    """
    # Prints information about He-3 Fusion
    print("%s of energy per 3g He-3" % si.return_with_si(fn.energy_from_mass_he3(cs.He3_MOLAR_MASS), 'J'))

    print("\nFor $ %s" % "{:,} in revenue:".format(revenue_desired))

    energy_required = fn.energy_needed_for_revenue(revenue_desired)
    print("  %s of energy required" % si.return_with_si(energy_required, 'J'))

    he3_mass = fn.mass_he3_required_for_energy(energy_required)
    print("  %s of mass of He3 required" % si.return_with_si(he3_mass, 'g'))

    regolith_mass = fn.mass_regolith_to_retrieve_mass_he3(he3_mass)
    print("  %s of mass of regolith required" % si.return_with_si(regolith_mass, 'g'))
    print("    Rate per day of %s [D+N]" %
          si.return_with_si(regolith_mass / cs.DAYS_IN_YEAR, 'g'))
    print("    Rate per day of %s [D only]" %
          si.return_with_si(2 * regolith_mass / cs.DAYS_IN_YEAR, 'g'))

    print("Volatiles Generated: ")
    for volatile in cs.volatile_he3_ratio.keys():
        print("  %s of" % si.return_with_si(he3_mass * cs.VOLATILE_He3_RATIO[volatile], 'g'), volatile)


# print("%s of regolith per ton He-3" %
#       return_with_si_units(affix_si_prefix(mass_regolith_to_retrieve_mass_he3(ONE_TON)), 'g'))  # Mass in grams

print_report(1e9)  # one billion dollars

# Find energy required to create desired revenue
# Find mass of He3 in g to create needed amount of energy

