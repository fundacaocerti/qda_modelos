# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from models import macrophytes


class TestMacrophytesTucker1979:
    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        reflectance_nir_wavelength = R20m_bands["B08"]
        reflectance_red_wavelength = R20m_bands["B04"]

        tucker_1979_result = macrophytes.tucker_1979(
            reflectance_nir_wavelength, reflectance_red_wavelength
        )

        assert isinstance(tucker_1979_result, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        reflectance_nir_wavelength = R20m_bands["B08"]
        reflectance_red_wavelength = R20m_bands["B04"]

        tucker_1979_result = macrophytes.tucker_1979(
            reflectance_nir_wavelength, reflectance_red_wavelength
        )

        assert tucker_1979_result.shape == reflectance_nir_wavelength.shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        reflectance_nir_wavelength = R20m_bands["B08"]

        with pytest.raises(TypeError):
            macrophytes.tucker_1979(reflectance_nir_wavelength)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        reflectance_nir_wavelength = R20m_bands["B08"]
        reflectance_red_wavelength = setup_bands["10m"]["B04"]

        with pytest.raises(ValueError):
            macrophytes.tucker_1979(
                reflectance_nir_wavelength, reflectance_red_wavelength
            )
