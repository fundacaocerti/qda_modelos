# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from src.models import chlorophylla


class TestChlorophyllaRodriguesEtAl2016:

    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        rodrigues_et_al_2016_result = chlorophylla.rodrigues_et_al_2016(
            R20m_bands["B8A"], R20m_bands["B08"])

        assert isinstance(rodrigues_et_al_2016_result,
                          numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        rodrigues_et_al_2016_result = chlorophylla.rodrigues_et_al_2016(
            R20m_bands["B8A"], R20m_bands["B08"])

        assert rodrigues_et_al_2016_result.shape == R20m_bands["B8A"].shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        B8A = setup_bands['20m']['B8A']

        with pytest.raises(TypeError):
            chlorophylla.rodrigues_et_al_2016(B8A)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        B8A = setup_bands['20m']['B8A']
        B08 = setup_bands['10m']['B08']

        with pytest.raises(ValueError):
            chlorophylla.rodrigues_et_al_2016(B8A, B08)
