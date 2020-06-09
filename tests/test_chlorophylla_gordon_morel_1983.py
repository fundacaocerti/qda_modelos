# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from qda_modelos import chlorophylla


class TestChlorophyllaGordonMorel1983:
    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        goldon_morel_1983_result = chlorophylla.gordon_morel_1983(
            R20m_bands["B03"], R20m_bands["B01"]
        )

        assert isinstance(goldon_morel_1983_result, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        goldon_morel_1983_result = chlorophylla.gordon_morel_1983(
            R20m_bands["B03"], R20m_bands["B01"]
        )

        assert goldon_morel_1983_result.shape == R20m_bands["B03"].shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        B03 = setup_bands["20m"]["B03"]

        with pytest.raises(TypeError):
            chlorophylla.gordon_morel_1983(B03)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        B03 = setup_bands["20m"]["B03"]
        B01 = setup_bands["10m"]["B01"]

        with pytest.raises(ValueError):
            chlorophylla.gordon_morel_1983(B03, B01)
