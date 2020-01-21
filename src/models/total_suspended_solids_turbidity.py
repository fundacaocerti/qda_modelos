# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy

numpy.seterr(divide="ignore", invalid="ignore")


def doxaran_et_al_2003(band8a, band3):

    return band8a.astype(float) / band3


def miller_mckee_2004(band4):

    return band4


def liu_et_al_2006(band8a, band4):

    return (band4.astype(float) -
            band8a.astype(float)) / (band4 + band8a)


def doxaran_et_al_2009(band8a, band4):

    return band8a.astype(float) / band4


def tarrant_et_al_2010(band8a, band4):

    return band4.astype(float) - band8a


def zhang_et_al_2010(band4, band2):

    return (band2.astype(float) -
            band4.astype(float)) / (band2 + band4)


def tang_et_al_2010(band3, band2):

    return band3.astype(float) / band2
