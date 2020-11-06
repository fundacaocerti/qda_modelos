# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from qda_modelos import thophic_state_index


class TestTrophicStateIndexLamparelli2004:
    def test_expected_result_type(self, setup_bands):
        assert isinstance(None, numpy.ndarray)

    def test_expected_result_shape(self, setup_bands):
        assert None.shape == None

    def test_expected_error_for_wrong_number_of_bands(self, setup_bands):
        with pytest.raises(TypeError):
            None

    def test_expected_error_for_bands_of_different_shapes(self, setup_bands):
        with pytest.raises(ValueError):
            None
