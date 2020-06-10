# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from qda_modelos import water_transparency as transparency


class TestWaterTransparencyHarmaEtAl2001:
    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        harma_et_al_2001_result = transparency.harma_et_al_2001(
            R20m_bands["B06"], R20m_bands["B04"], R20m_bands["B02"]
        )

        assert isinstance(harma_et_al_2001_result, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        harma_et_al_2001_result = transparency.harma_et_al_2001(
            R20m_bands["B06"], R20m_bands["B04"], R20m_bands["B02"]
        )

        assert harma_et_al_2001_result.shape == R20m_bands["B04"].shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        B04 = setup_bands["20m"]["B04"]

        with pytest.raises(TypeError):
            transparency.harma_et_al_2001(B04)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        B06 = setup_bands["20m"]["B06"]
        B04 = setup_bands["20m"]["B04"]
        B02 = setup_bands["10m"]["B02"]

        with pytest.raises(ValueError):
            transparency.harma_et_al_2001(B06, B04, B02)
