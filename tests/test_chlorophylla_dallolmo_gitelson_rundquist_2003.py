# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from qda_modelos import chlorophylla


class TestChlorophyllaDallOlmoGitelsonRundquist2003:
    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        dallolmo_gitelson_rundquist_2003_result = chlorophylla.dallolmo_gitelson_rundquist_2003(
            R20m_bands["B06"], R20m_bands["B05"], R20m_bands["B04"]
        )

        assert isinstance(dallolmo_gitelson_rundquist_2003_result, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        dallolmo_gitelson_rundquist_2003_result = chlorophylla.dallolmo_gitelson_rundquist_2003(
            R20m_bands["B06"], R20m_bands["B05"], R20m_bands["B04"]
        )

        assert dallolmo_gitelson_rundquist_2003_result.shape == R20m_bands["B06"].shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        B06 = setup_bands["20m"]["B06"]

        with pytest.raises(TypeError):
            chlorophylla.dallolmo_gitelson_rundquist_2003(B06)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        B06 = setup_bands["20m"]["B06"]
        B05 = setup_bands["20m"]["B05"]
        B04 = setup_bands["10m"]["B04"]

        with pytest.raises(ValueError):
            chlorophylla.dallolmo_gitelson_rundquist_2003(B06, B05, B04)
