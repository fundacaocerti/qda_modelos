# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy

numpy.seterr(divide="ignore", invalid="ignore")


def tucker_1979(reflectance_nir_wavelength, reflectance_red_wavelength):
    return (
        reflectance_nir_wavelength.astype(float)
        - reflectance_red_wavelength.astype(float)
    ) / (reflectance_nir_wavelength + reflectance_red_wavelength)


def huete_et_al_1997(
    reflectance_nir_wavelength, reflectance_red_wavelength, reflectance_blue_wavelength,
):
    return (
        2.5
        * (
            reflectance_nir_wavelength.astype(float)
            - reflectance_red_wavelength.astype(float)
        )
        / (
            reflectance_nir_wavelength
            + (6 * reflectance_red_wavelength)
            - (7.5 * reflectance_blue_wavelength)
            + 1
        )
    )


def villa_et_al_2013(reflectance_860nm_wavelength, reflectance_490nm_wavelength):
    return (
        reflectance_860nm_wavelength.astype(float)
        - reflectance_490nm_wavelength.astype(float)
    ) / (reflectance_860nm_wavelength + reflectance_490nm_wavelength)


def villa_et_al_2014(
    reflectance_859nm_wavelength, reflectance_490nm_wavelength, correction_factor_L
):
    return (
        (1 + correction_factor_L)
        * (
            reflectance_859nm_wavelength.astype(float)
            - reflectance_490nm_wavelength.astype(float)
        )
        / (
            reflectance_859nm_wavelength
            + reflectance_490nm_wavelength
            + correction_factor_L
        )
    )
