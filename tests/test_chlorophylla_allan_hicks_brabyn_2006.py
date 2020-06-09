# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from qda_modelos import chlorophylla


class TestChlorophyllaAllanHicksBrabyn2006:
    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        allan_hicks_brabyn_2006_result = chlorophylla.allan_hicks_brabyn_2006(
            R20m_bands["B04"], R20m_bands["B02"]
        )

        assert isinstance(allan_hicks_brabyn_2006_result, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        allan_hicks_brabyn_2006_result = chlorophylla.allan_hicks_brabyn_2006(
            R20m_bands["B04"], R20m_bands["B02"]
        )

        assert allan_hicks_brabyn_2006_result.shape == R20m_bands["B04"].shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        B04 = setup_bands["20m"]["B04"]

        with pytest.raises(TypeError):
            chlorophylla.allan_hicks_brabyn_2006(B04)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        B04 = setup_bands["20m"]["B04"]
        B02 = setup_bands["10m"]["B02"]

        with pytest.raises(ValueError):
            chlorophylla.allan_hicks_brabyn_2006(B04, B02)
