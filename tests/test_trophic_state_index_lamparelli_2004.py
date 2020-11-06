# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from qda_modelos import trophic_state_index


class TestTrophicStateIndexLamparelli2004:
    def test_expected_result_type(self, milligrams_per_liter_array):
        lamparelli_2004_result = trophic_state_index.lamparelli_2004(
            milligrams_per_liter_array, milligrams_per_liter_array
        )

        assert isinstance(lamparelli_2004_result, numpy.ndarray)

    def test_expected_result_shape(self, milligrams_per_liter_array):
        lamparelli_2004_result = trophic_state_index.lamparelli_2004(
            milligrams_per_liter_array, milligrams_per_liter_array
        )

        assert lamparelli_2004_result.shape == milligrams_per_liter_array.shape

    def test_expected_error_for_arrays_of_different_shapes(self, setup_bands, milligrams_per_liter_array):
        different_shape_array = setup_bands["10m"]["B02"]

        with pytest.raises(ValueError):
            trophic_state_index.lamparelli_2004(milligrams_per_liter_array, different_shape_array)

