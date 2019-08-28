import constants_rev as cs
import functions as f


class ParamMode:
    FLIGHT_BUDGET = 0
    OPERATION_BUDGET = 1
    PAYLOAD_MASS = 2


class Parameters:
    # constant init
    __flight_budget = __operation_budget = __payload_tonnage = __volatile_tonnage_needed = 0
    # Budgets are in $
    # Payload tonnage in tons

    def __init__(self, mode, value):
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

    def print_params(self):
        print("--- PARAMETERS ---\n"
              "Flight Budget           : %s\n"
              "Operation Budget        : %s\n"
              "Payload Tonnage         : %s\n"
              "Volatile Tonnage Needed : %s\n" % (f.convert_to_dollar_value(self.__flight_budget),
                                                  f.convert_to_dollar_value(self.__operation_budget),
                                                  self.__payload_tonnage, self.__volatile_tonnage_needed))

