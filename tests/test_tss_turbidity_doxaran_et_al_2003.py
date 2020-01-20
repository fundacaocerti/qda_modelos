# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import rasterio as rio
import pytest
from qda_modelos.models import total_suspended_solids_turbidity as turbidity


class TestTSSTurbidityDoxaranEtAl2003:

    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        doxaran_et_al_2003_result = turbidity.doxaran_et_al_2003(
            R20m_bands["B8A"], R20m_bands["B03"])

        assert isinstance(doxaran_et_al_2003_result,
                          numpy.ndarray), "The function should return an instance of numpys ndarray"

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        doxaran_et_al_2003_result = turbidity.doxaran_et_al_2003(
            R20m_bands["B8A"], R20m_bands["B03"])

        assert doxaran_et_al_2003_result.shape == R20m_bands["B8A"].shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        B8A = setup_bands['20m']['B8A']

        with pytest.raises(TypeError):
            turbidity.doxaran_et_al_2003(B8A)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        B8A = setup_bands['20m']['B8A']
        B03 = setup_bands['10m']['B03']

        with pytest.raises(ValueError):
            turbidity.doxaran_et_al_2003(B8A, B03)
