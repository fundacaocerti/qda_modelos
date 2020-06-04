# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from models import chlorophylla


class TestChlorophyllaChavulaEtAl2009:
    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        chavula_et_al_2009_result = chlorophylla.chavula_et_al_2009(
            R20m_bands["B03"], R20m_bands["B01"]
        )

        assert isinstance(chavula_et_al_2009_result, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        chavula_et_al_2009_result = chlorophylla.chavula_et_al_2009(
            R20m_bands["B03"], R20m_bands["B01"]
        )

        assert chavula_et_al_2009_result.shape == R20m_bands["B03"].shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        B03 = setup_bands["20m"]["B03"]

        with pytest.raises(TypeError):
            chlorophylla.chavula_et_al_2009(B03)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        B03 = setup_bands["20m"]["B03"]
        B01 = setup_bands["10m"]["B01"]

        with pytest.raises(ValueError):
            chlorophylla.chavula_et_al_2009(B03, B01)
