# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from models import cyanobacteria


class TestCyanobacteriaDashEtAl2011:
    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        dash_et_al_2011_result = cyanobacteria.dash_et_al_2011(
            R20m_bands["B03"], R20m_bands["B02"]
        )

        assert isinstance(dash_et_al_2011_result, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        dash_et_al_2011_result = cyanobacteria.dash_et_al_2011(
            R20m_bands["B03"], R20m_bands["B02"]
        )

        assert dash_et_al_2011_result.shape == R20m_bands["B03"].shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        B03 = setup_bands["20m"]["B03"]

        with pytest.raises(TypeError):
            cyanobacteria.dash_et_al_2011(B03)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        B03 = setup_bands["20m"]["B03"]
        B02 = setup_bands["10m"]["B02"]

        with pytest.raises(ValueError):
            cyanobacteria.dash_et_al_2011(B03, B02)
