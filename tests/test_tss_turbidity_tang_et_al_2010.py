# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import rasterio as rio
import pytest
from qda_modelos import total_suspended_solids_turbidity as turbidity


class TestTSSTurbidityTangEtAl2010:
    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        B03 = R20m_bands["B03"]
        B02 = R20m_bands["B02"]

        tang_et_al_2010_result = turbidity.tang_et_al_2010(B03, B02)

        assert isinstance(tang_et_al_2010_result, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        B03 = R20m_bands["B03"]
        B02 = R20m_bands["B02"]

        tang_et_al_2010_result = turbidity.tang_et_al_2010(B03, B02)

        assert tang_et_al_2010_result.shape == B03.shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        B03 = setup_bands["20m"]["B03"]

        with pytest.raises(TypeError):
            turbidity.tang_et_al_2010(B03)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        B03 = setup_bands["20m"]["B03"]
        B02 = setup_bands["10m"]["B02"]

        with pytest.raises(ValueError):
            turbidity.tang_et_al_2010(B03, B02)
