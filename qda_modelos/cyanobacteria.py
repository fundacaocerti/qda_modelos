# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy

numpy.seterr(divide="ignore", invalid="ignore")


def simis_et_al_2005(reflectance_709nm_wavelength, reflectance_620nm_wavelength):
    return reflectance_709nm_wavelength.astype(float) / reflectance_620nm_wavelength


def dash_et_al_2011(reflectance_556nm_wavelength, reflectance_510nm_wavelength):
    return (
        reflectance_556nm_wavelength.astype(float)
        - reflectance_510nm_wavelength.astype(float)
    ) / (556.4 - 510.6)


def wozniak_et_al_2016(reflectance_660nm_wavelength, reflectance_595nm_wavelength):
    return reflectance_595nm_wavelength.astype(float) / reflectance_660nm_wavelength
