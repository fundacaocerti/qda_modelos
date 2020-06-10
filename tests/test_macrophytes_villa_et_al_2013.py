# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from qda_modelos import macrophytes


class TestMacrophytesVillaEtAl2013:
    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        villa_et_al_2013_result = macrophytes.villa_et_al_2013(
            R20m_bands["B8A"], R20m_bands["B02"]
        )

        assert isinstance(villa_et_al_2013_result, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        villa_et_al_2013_result = macrophytes.villa_et_al_2013(
            R20m_bands["B8A"], R20m_bands["B02"]
        )

        assert villa_et_al_2013_result.shape == R20m_bands["B8A"].shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        B8A = setup_bands["20m"]["B8A"]

        with pytest.raises(TypeError):
            macrophytes.villa_et_al_2013(B8A)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        B8A = setup_bands["20m"]["B8A"]
        B02 = setup_bands["10m"]["B02"]

        with pytest.raises(ValueError):
            macrophytes.villa_et_al_2013(B8A, B02)
