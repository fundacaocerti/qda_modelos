# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################


import numpy
import pytest
from models import macrophytes


class TestMacrophytesHueteEtAl1997:
    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        reflectance_nir_wavelength = R20m_bands["B08"]
        reflectance_red_wavelength = R20m_bands["B04"]
        reflectance_blue_wavelength = R20m_bands["B02"]

        huete_et_al_1997_result = macrophytes.huete_et_al_1997(
            reflectance_nir_wavelength,
            reflectance_red_wavelength,
            reflectance_blue_wavelength,
        )

        assert isinstance(huete_et_al_1997_result, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        reflectance_nir_wavelength = R20m_bands["B08"]
        reflectance_red_wavelength = R20m_bands["B04"]
        reflectance_blue_wavelength = R20m_bands["B02"]

        huete_et_al_1997_result = macrophytes.huete_et_al_1997(
            reflectance_nir_wavelength,
            reflectance_red_wavelength,
            reflectance_blue_wavelength,
        )

        assert huete_et_al_1997_result.shape == reflectance_nir_wavelength.shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        reflectance_nir_wavelength = R20m_bands["B08"]
        reflectance_red_wavelength = R20m_bands["B04"]

        with pytest.raises(TypeError):
            macrophytes.huete_et_al_1997(
                reflectance_nir_wavelength, reflectance_red_wavelength,
            )

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        reflectance_nir_wavelength = R20m_bands["B08"]
        reflectance_red_wavelength = R20m_bands["B04"]
        reflectance_blue_wavelength = setup_bands["10m"]["B02"]

        with pytest.raises(ValueError):
            macrophytes.huete_et_al_1997(
                reflectance_nir_wavelength,
                reflectance_red_wavelength,
                reflectance_blue_wavelength,
            )

