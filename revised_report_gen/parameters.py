import constants_rev as cs
import functions as f
import si_formatter as si
from enum import Enum


class ParamMode(Enum):
    FLIGHT_BUDGET = 0
    OPERATION_BUDGET = 1
    PAYLOAD_MASS = 2


class Parameters:
    # constant init
    __flight_budget = __operation_budget = __payload_tonnage = __volatile_tonnage_needed = __total_launches = 0
    # Budgets are in $
    # Payload tonnage in tons

    def __init__(self, mode, value):
        value = float(value)
        """
        Constructor
        :param mode: One of the param modes
        :param value: value to assign for that param
        """
        if mode == ParamMode.FLIGHT_BUDGET:
            self.__flight_budget = value
            self.__operation_budget = self.__flight_budget * cs.FLIGHT_BUDGET_MULT
            self.__payload_tonnage = self.__flight_budget / cs.COST_PER_TON
        elif mode == ParamMode.OPERATION_BUDGET:
            self.__operation_budget = value
            self.__flight_budget = self.__operation_budget / cs.FLIGHT_BUDGET_MULT
            self.__payload_tonnage = self.__flight_budget / cs.COST_PER_TON
        elif mode == ParamMode.PAYLOAD_MASS:
            self.__payload_tonnage = value
            self.__flight_budget = self.__payload_tonnage * cs.COST_PER_TON
            self.__operation_budget = self.__flight_budget * cs.FLIGHT_BUDGET_MULT

        self.__volatile_tonnage_needed = self.__operation_budget / cs.COST_PER_TON
        self.__total_launches = self.__flight_budget / cs.COST_PER_LAUNCH

    def print_report(self):
        """
        Print information log
        :return: printed log
        """
        self._print_primary_params()
        self._print_regolith_params()
        self._print_volatile_params()

    def _print_primary_params(self):
        print("--- PARAMETERS ---\n"
              "Flight Budget           : %s\n"
              "Operation Budget        : %s\n"
              "Payload Tonnage         : %s\n"
              "Volatile Tonnage Needed : %s\n"
              "Total # of Launches     : %s" % (f.convert_to_dollar_value(self.__flight_budget),
                                                f.convert_to_dollar_value(self.__operation_budget),
                                                self.__payload_tonnage, self.__volatile_tonnage_needed,
                                                self.__total_launches))

    def _print_regolith_params(self):
        _annual_tonnage = (self.__volatile_tonnage_needed / cs.TOTAL_VOLATILE_RATIO) \
                          * (cs.DAYS_PER_YEAR / cs.MISSION_LENGTH)
        print("\n--- REGOLITH PROCESSED ---")
        print("Annually      : %s tpy" % _annual_tonnage)
        print("Year Round    : %s tpd" % (_annual_tonnage / cs.DAYS_PER_YEAR))
        print("Sunlight Only : %s tpd" % (2 * _annual_tonnage / cs.DAYS_PER_YEAR))

    def _print_volatile_params(self):
        _regolith_tonnage = (self.__volatile_tonnage_needed / cs.TOTAL_VOLATILE_RATIO)
        print("\n--- VOLATILES PROCURED ---")
        for volatile in cs.VOLATILE_REGOLITH_RATIO.keys():
            print("%s of" % si.return_with_si(
                _regolith_tonnage * 1e6 * cs.VOLATILE_REGOLITH_RATIO[volatile] *
                cs.REGOLITH_RETAINMENT_RATE, 'g'), volatile)

