# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy

numpy.seterr(divide="ignore", invalid="ignore")


def lamparelli_2004(chlorophylla, phosphorus):

    trophic_state_index_chl = 10 * (6 - ((0.92 - 0.34 * numpy.log(chlorophylla)) / numpy.log(2)))
    trophic_state_index_pho = 10 * (6 - (1.77 - 0.42 * (numpy.log(phosphorus) / numpy.log(2))))

    return (trophic_state_index_chl / trophic_state_index_pho) / 2

