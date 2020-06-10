# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy

numpy.seterr(divide="ignore", invalid="ignore")


def doxaran_et_al_2003(reflectance_859nm_wavelength, reflectance_555nm_wavelength):

    return reflectance_859nm_wavelength.astype(float) / reflectance_555nm_wavelength


def miller_mckee_2004(reflectance_645nm_wavelength):

    return reflectance_645nm_wavelength


def liu_et_al_2006(reflectance_859nm_wavelength, reflectance_645nm_wavelength):

    return (reflectance_645nm_wavelength.astype(float) -
            reflectance_859nm_wavelength.astype(float)) / (reflectance_645nm_wavelength + reflectance_859nm_wavelength) 


def doxaran_et_al_2009(reflectance_859nm_wavelength, reflectance_645nm_wavelength):

    return reflectance_859nm_wavelength.astype(float) / reflectance_645nm_wavelength


def tarrant_et_al_2010(reflectance_859nm_wavelength_, reflectance_645nm_wavelength):

    return reflectance_645nm_wavelength.astype(float) - reflectance_859nm_wavelength_


def zhang_et_al_2010(reflectance_645nm_wavelength, reflectance_469nm_wavelength):

    return (reflectance_469nm_wavelength.astype(float) -
            reflectance_645nm_wavelength.astype(float)) / (reflectance_469nm_wavelength + reflectance_645nm_wavelength)


def tang_et_al_2010(reflectance_560nm_wavelength, reflectance_490nm_wavelength):

    return reflectance_560nm_wavelength.astype(float) / reflectance_490nm_wavelength
