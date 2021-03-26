# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################
"""
This module implements the Reservoir Water Quality Index as
presented by the Instituto Ambiental do Paraná, described in
http://pnqa.ana.gov.br/indicadores-qualidade-agua.aspx.
"""

import operator
import numpy

numpy.seterr(divide='ignore', invalid='ignore')


def _index_classification(index, possible_outputs, limits, conditional):
    """This private function classify a numpy array according to the limits, conditionals and
    possible outputs defined in the arguments. This is basically a numpy.select, that
    is not the fastest approach, but it serves the current purpose.

    :param index: This is the array to be classified. Called index due to the context of this module
    :type index: numpy array, mandatory
    :param possible_outputs: This array defines the classification values
    :type possible_outputs: array, mandatory
    :param limits: This is an array with the thresholds to be compared in each cell of index
    :type limits: array, mandatory
    :param conditional: This is the conditional to be applied between the index cells and limits
    :type conditional: operator, mandatory
    :return: Returns a classified numpy array
    :rtype: numpy array
    """
    conditional_list = []
    opposite_operators = {
        operator.eq: operator.ne,
        operator.ge: operator.lt,
        operator.gt: operator.le,
        operator.le: operator.gt,
        operator.lt: operator.ge,
        operator.ne: operator.eq
    }

    operators = [conditional] * len(limits)
    for i in range(len(operators)):
        conditional_list.append(condition(index, limits[i]))
    conditional_list.append(opposite_operators[conditional](index, limits[-1]))

    return numpy.select(conditional_list, possible_outputs)


def instituto_ambiental_parana_2004(
        dissolved_oxygen_deficit,
        total_phosphorus,
        total_inorganic_nitrogen,
        chlorophylla,
        water_transparency,
        chemical_oxygen_demand,
        residence_time,
        underwater_depth,
        cyanobacteria,
):
    """This function implements the Reservoir Water Quality Index in accordance with
    what is defined by the Instituto Ambiental do Paraná. This model basically classifies
    some water indexes and, by weighting them, provides a score for the reservoir.

    :param dissolved_oxygen_deficit: Dissolved oxygen deficit (%)
    :type dissolved_oxygen_deficit: numpy array, mandatory
    :param total_phosphorus: Total phosphorus in mg/L
    :type total_phosphorus: numpy array, mandatory
    :param total_inorganic_nitrogen: Total inorganic nitrogen in N-mg/L
    :type total_inorganic_nitrogen: numpy array, mandatory
    :param chlorophylla: Chlorophylla in µg/L
    :type chlorophylla: numpy array, mandatory
    :param water_transparency: Secchi disk in meters (m)
    :type water_transparency: numpy array, mandatory
    :param chemical_oxygen_demand: Chemical oxygen demand in mg/L
    :type chemical_oxygen_demand: numpy array, mandatory
    :param residence_time: Residence time in days
    :type residence_time: numpy array, mandatory
    :param underwater_depth: Underwater depth in meters (m)
    :type underwater_depth: numpy array, mandatory
    :param cyanobacteria: Cyanobacteria in number of cells/mL
    :type cyanobacteria: numpy array, mandatory
    :return: Array with each cell scored according to the index weighting function
    :rtype: numpy array
    """
    classes = [1, 2, 3, 4, 5, 6]  # Class I to VI

    # This table is part of the index: http://pnqa.ana.gov.br/indicadores-qualidade-agua.aspx
    indexes_table = {
        1: {
            'index': dissolved_oxygen_deficit,
            'weight': 17,
            'limits': [5., 20., 35., 50., 70.],
            'conditional': operator.le
        },
        2: {
            'index': total_phosphorus,
            'weight': 12,
            'limits': [0.01, 0.025, 0.040, 0.085, 0.21],
            'conditional': operator.lt
        },
        3: {
            'index': total_inorganic_nitrogen,
            'weight': 8,
            'limits': [0.15, 0.25, 0.6, 2.0, 5.0],
            'conditional': operator.le
        },
        4: {
            'index': chlorophylla,
            'weight': 15,
            'limits': [1.5, 3.0, 5.0, 10.0, 32.0],
            'conditional': operator.le
        },
        5: {
            'index': water_transparency,
            'weight': 12,
            'limits': [3.0, 2.3, 1.2, 0.6, 0.3],
            'conditional': operator.ge
        },
        6: {
            'index': chemical_oxygen_demand,
            'weight': 12,
            'limits': [3.0, 5.0, 8.0, 14.0, 30.0],
            'conditional': operator.le
        },
        7: {
            'index': residence_time,
            'weight': 10,
            'limits': [10, 40, 120, 365, 550],
            'conditional': operator.le
        },
        8: {
            'index': underwater_depth,
            'weight': 6,
            'limits': [35.0, 15.0, 7.0, 3.1, 1.1],
            'conditional': operator.ge
        },
        9: {
            'index': cyanobacteria,
            'weight': 8,
            'limits': [1.0, 5.0, 20., 50.0, 100.0],
            'conditional': operator.le
        }
    }

    weighted_sum = numpy.zeros_like(dissolved_oxygen_deficit)
    wi_sum = 0

    for iterator in indexes_table:
        qi = _index_classification(
            indexes_table[iterator]['index'],
            classes,
            indexes_table[iterator]['limits'],
            indexes_table[iterator]['conditional']
        )
        weighted_sum += (indexes_table[iterator]['weight'] * qi)
        wi_sum += indexes_table[iterator]['weight']

    return weighted_sum / wi_sum
