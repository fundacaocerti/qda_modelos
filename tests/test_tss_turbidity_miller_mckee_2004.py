# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import rasterio as rio
import pytest
from qda_modelos.models import total_suspended_solids_turbidity as turbidity


class TestTSSTurbidityMillerMckee2004:

    def test_expected_result(self, setup_bands):
        B04 = setup_bands["20m"]['B04']

        miller_mckee_2004_result = turbidity.miller_mckee_2004(B04)

        assert (miller_mckee_2004_result == B04).all()

    def test_expected_result_type(self, setup_bands):

        B04 = setup_bands["20m"]['B04']

        miller_mckee_2004_result = turbidity.miller_mckee_2004(B04)

        assert isinstance(miller_mckee_2004_result,
                          numpy.ndarray), "The function should return an instance of numpys ndarray"
