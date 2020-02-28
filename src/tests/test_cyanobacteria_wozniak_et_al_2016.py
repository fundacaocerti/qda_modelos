# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from models import cyanobacteria


class TestCyanobacteriaWozniakEtAl2016:
    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        wozniak_et_al_2016_result = cyanobacteria.wozniak_et_al_2016(
            R20m_bands["B04"], R20m_bands["B03"]
        )

        assert isinstance(wozniak_et_al_2016_result, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        wozniak_et_al_2016_result = cyanobacteria.wozniak_et_al_2016(
            R20m_bands["B04"], R20m_bands["B03"]
        )

        assert wozniak_et_al_2016_result.shape == R20m_bands["B04"].shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        B04 = setup_bands["20m"]["B04"]

        with pytest.raises(TypeError):
            cyanobacteria.wozniak_et_al_2016(B04)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        B04 = setup_bands["20m"]["B04"]
        B03 = setup_bands["10m"]["B03"]

        with pytest.raises(ValueError):
            cyanobacteria.wozniak_et_al_2016(B04, B03)

