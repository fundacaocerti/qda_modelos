# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from models import chlorophylla


class TestChlorophyllaGowerEtAl2005:
    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        band_4 = R20m_bands["B04"]
        band_5 = R20m_bands["B05"]
        band_6 = R20m_bands["B06"]

        r681_adapted_wavelength = 665
        r709_adapted_wavelength = 705
        r753_adapted_wavelength = 740

        gower_et_al_2005_2016_result = chlorophylla.gower_et_al_2005(
            band_6,
            band_5,
            band_4,
            r753_adapted_wavelength,
            r709_adapted_wavelength,
            r681_adapted_wavelength,
        )

        assert isinstance(gower_et_al_2005_2016_result, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        band_4 = R20m_bands["B04"]
        band_5 = R20m_bands["B05"]
        band_6 = R20m_bands["B06"]

        r681_adapted_wavelength = 665
        r709_adapted_wavelength = 705
        r753_adapted_wavelength = 740

        gower_et_al_2005_2016_result = chlorophylla.gower_et_al_2005(
            band_6,
            band_5,
            band_4,
            r753_adapted_wavelength,
            r709_adapted_wavelength,
            r681_adapted_wavelength,
        )

        assert gower_et_al_2005_2016_result.shape == band_6.shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        band_4 = R20m_bands["B04"]
        band_5 = R20m_bands["B05"]

        r681_adapted_wavelength = 665
        r709_adapted_wavelength = 705
        r753_adapted_wavelength = 740

        with pytest.raises(TypeError):
            chlorophylla.gower_et_al_2005(
                band_5,
                band_4,
                r753_adapted_wavelength,
                r709_adapted_wavelength,
                r681_adapted_wavelength,
            )

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        band_4 = setup_bands["10m"]["B04"]
        band_5 = R20m_bands["B05"]
        band_6 = R20m_bands["B06"]

        r681_adapted_wavelength = 665
        r709_adapted_wavelength = 705
        r753_adapted_wavelength = 740

        with pytest.raises(ValueError):
            chlorophylla.gower_et_al_2005(
                band_6,
                band_5,
                band_4,
                r753_adapted_wavelength,
                r709_adapted_wavelength,
                r681_adapted_wavelength,
            )
