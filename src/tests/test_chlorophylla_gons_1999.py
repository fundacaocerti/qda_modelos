# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from models import chlorophylla


class TestChlorophyllaGons1999:
    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        gons_1999_result = chlorophylla.gons_1999(R20m_bands["B05"], R20m_bands["B04"])

        assert isinstance(gons_1999_result, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        gons_1999_result = chlorophylla.gons_1999(R20m_bands["B05"], R20m_bands["B04"])

        assert gons_1999_result.shape == R20m_bands["B05"].shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        B05 = setup_bands["20m"]["B05"]

        with pytest.raises(TypeError):
            chlorophylla.gons_1999(B05)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        B05 = setup_bands["20m"]["B05"]
        B04 = setup_bands["10m"]["B04"]

        with pytest.raises(ValueError):
            chlorophylla.gons_1999(B05, B04)
