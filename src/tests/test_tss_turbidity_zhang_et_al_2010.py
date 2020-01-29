# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import rasterio as rio
import pytest
from src.models import total_suspended_solids_turbidity as turbidity


class TestTSSTurbidityZhangEtAl2010:

    def test_expected_result_type(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        B04 = R20m_bands['B04']
        B02 = R20m_bands['B02']

        zhang_et_al_2010_result = turbidity.zhang_et_al_2010(B04, B02)

        assert isinstance(zhang_et_al_2010_result,
                          numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        B04 = R20m_bands['B04']
        B02 = R20m_bands['B02']

        zhang_et_al_2010_result = turbidity.zhang_et_al_2010(B04, B02)

        assert zhang_et_al_2010_result.shape == B04.shape

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        R20m_bands = setup_bands["20m"]
        B04 = R20m_bands['B04']

        with pytest.raises(TypeError):
            turbidity.zhang_et_al_2010(B04)

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        R20m_bands = setup_bands["20m"]

        B04 = setup_bands['20m']['B04']
        B02 = setup_bands['10m']['B02']

        with pytest.raises(ValueError):
            turbidity.zhang_et_al_2010(B04, B02)
