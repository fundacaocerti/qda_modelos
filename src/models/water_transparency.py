# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy

numpy.seterr(divide="ignore", invalid="ignore")


def giardino_et_al_2001(reflectance_560nm_wavelength, reflectance_485nm_wavelength):
    return reflectance_485nm_wavelength.astype(float) / reflectance_560nm_wavelength


def harma_et_al_2001(
    reflectance_754nm_wavelength,
    reflectance_620nm_wavelength,
    reflectance_490nm_wavelength,
):
    return (
        reflectance_490nm_wavelength.astype(float)
        - reflectance_754nm_wavelength.astype(float)
    ) / (reflectance_620nm_wavelength - reflectance_754nm_wavelength)


def guimaraes_et_al_2016(reflectance_655nm_wavelength):

    return reflectance_655nm_wavelength
