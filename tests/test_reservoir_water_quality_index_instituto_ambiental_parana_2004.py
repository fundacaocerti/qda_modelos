# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from qda_modelos import reservoir_water_quality_index as rwqi


class TestReservoirWaterQualityIndexIAP2004:
    def test_expected_result_type(self, milligrams_per_liter_array):
        instituto_ambiental_parana_2004_result = rwqi.instituto_ambiental_parana_2004(
            milligrams_per_liter_array, milligrams_per_liter_array, milligrams_per_liter_array,
            milligrams_per_liter_array, milligrams_per_liter_array, milligrams_per_liter_array,
            milligrams_per_liter_array, milligrams_per_liter_array, milligrams_per_liter_array
        )

        assert isinstance(instituto_ambiental_parana_2004_result, numpy.ndarray)

    def test_expected_result_shape(self, milligrams_per_liter_array):
        instituto_ambiental_parana_2004_result = rwqi.instituto_ambiental_parana_2004(
            milligrams_per_liter_array, milligrams_per_liter_array, milligrams_per_liter_array,
            milligrams_per_liter_array, milligrams_per_liter_array, milligrams_per_liter_array,
            milligrams_per_liter_array, milligrams_per_liter_array, milligrams_per_liter_array
        )

        assert instituto_ambiental_parana_2004_result.shape == milligrams_per_liter_array.shape

    def test_expected_error_for_arrays_of_different_types(
            self, setup_bands, milligrams_per_liter_array):
        different_type_array = setup_bands["10m"]["B02"]

        with pytest.raises(TypeError):
            rwqi.instituto_ambiental_parana_2004(
                different_type_array, milligrams_per_liter_array, milligrams_per_liter_array,
                milligrams_per_liter_array, milligrams_per_liter_array, milligrams_per_liter_array,
                milligrams_per_liter_array, milligrams_per_liter_array, milligrams_per_liter_array
            )

    def test_expected_result(self):
        # The values bellow are in accordance to the model classification.
        # See http://pnqa.ana.gov.br/indicadores-qualidade-agua.aspx
        dod = numpy.array([4., 10., 30., 40., 60., 80.])
        ft = numpy.array([0.001, 0.015, 0.027, 0.042, 0.087, 0.22])
        nit = numpy.array([0.14, 0.24, 0.59, 1.8, 4.087, 6.22])
        cl = numpy.array([1.4, 2.24, 4.59, 8.8, 23.087, 36.22])
        tra = numpy.array([4., 2.4, 1.59, 0.8, 0.4, 0.1])
        dqo = numpy.array([1.4, 4., 6.59, 8.8, 23.087, 36.22])
        tre = numpy.array([5.4, 32.24, 114.59, 238.8, 423.087, 636.22])
        pro = numpy.array([36.8, 18.8, 8.8, 4.8, 2.8, 0.8])
        cia = numpy.array([0.4, 2.24, 14.59, 28.8, 63.087, 136.22])

        expected_result = numpy.array([1., 2., 3., 4., 5., 6.])

        result = rwqi.instituto_ambiental_parana_2004(dod, ft, nit, cl, tra, dqo, tre, pro, cia)

        assert (result == expected_result).all()
