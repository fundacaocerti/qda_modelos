# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy

numpy.seterr(divide="ignore", invalid="ignore")


def gordon_morel_1983(reflectance_550nm_wavelength, reflectance_440nm_wavelength):

    return reflectance_440nm_wavelength.astype(float) / reflectance_550nm_wavelength


def gons_1999(reflectance_704nm_wavelength, reflectance_672nm_wavelength):

    return reflectance_704nm_wavelength.astype(float) / reflectance_672nm_wavelength


def dallolmo_gitelson_rundquist_2003(
    reflectance_745nm_wavelength,
    reflectance_725nm_wavelength,
    reflectance_665nm_wavelength,
):

    return (
        reflectance_745nm_wavelength.astype(float) / reflectance_665nm_wavelength
    ) - (reflectance_745nm_wavelength.astype(float) / reflectance_725nm_wavelength)


def gitelson_et_al_2007(
    reflectance_730nm_wavelength,
    reflectance_695nm_wavelength,
    reflectance_675nm_wavelength,
):

    return (
        reflectance_730nm_wavelength.astype(float) / reflectance_675nm_wavelength
    ) - (reflectance_730nm_wavelength.astype(float) / reflectance_695nm_wavelength)


def le_et_al_2009(
    reflectance_740nm_wavelength,
    reflectance_705nm_wavelength,
    reflectance_693nm_wavelength,
    reflectance_662nm_wavelength,
):

    return (
        (reflectance_662nm_wavelength.astype(float) ** -1)
        - (reflectance_693nm_wavelength.astype(float) ** -1)
    ) / (
        (reflectance_740nm_wavelength.astype(float) ** -1)
        - (reflectance_705nm_wavelength.astype(float) ** -1)
    )


def mishra_mishra_2012(reflectance_708nm_wavelength, reflectance_665nm_wavelength):

    return (
        reflectance_708nm_wavelength.astype(float)
        - reflectance_665nm_wavelength.astype(float)
    ) / (reflectance_708nm_wavelength + reflectance_665nm_wavelength)


def rodrigues_et_al_2016(reflectance_893nm_wavelength, reflectance_838nm_wavelength):

    return reflectance_838nm_wavelength.astype(float) / reflectance_893nm_wavelength


def chavula_et_al_2009(reflectance_551nm_wavelength, reflectance_443nm_wavelength):

    return reflectance_443nm_wavelength.astype(float) / reflectance_551nm_wavelength


def allan_hicks_brabyn_2006(reflectance_665nm_wavelength, reflectance_485nm_wavelength):

    return reflectance_485nm_wavelength.astype(float) / reflectance_665nm_wavelength


def gower_et_al_2005(
    reflectance_753nm_wavelength,
    reflectance_709nm_wavelength,
    reflectance_681nm_wavelength,
    r753_adapted_wavelength,
    r709_adapted_wavelength,
    r681_adapted_wavelength,
):

    return (
        reflectance_709nm_wavelength.astype(float)
        - reflectance_681nm_wavelength.astype(float)
        - (
            (
                (r709_adapted_wavelength - r681_adapted_wavelength)
                / (r753_adapted_wavelength - r681_adapted_wavelength)
            )
            * (
                reflectance_753nm_wavelength.astype(float)
                - reflectance_681nm_wavelength.astype(float)
            )
        )
    )
