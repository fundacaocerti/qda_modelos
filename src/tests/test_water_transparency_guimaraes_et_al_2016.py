# ##################################################################################################
# Copyright (c) 2020 - Fundação CERTI
# All rights reserved.
# ##################################################################################################

import numpy
import pytest
from models import water_transparency as transparency


class TestWaterTransparencyGuimaraesEtAl2016:
    def test_expected_result(self, setup_bands):
        B04 = setup_bands["20m"]["B04"]

        guimaraes_et_al_2016_result = transparency.guimaraes_et_al_2016(B04)

        assert (guimaraes_et_al_2016_result == B04).all()

    def test_expected_result_type(self, setup_bands):

        B04 = setup_bands["20m"]["B04"]

        guimaraes_et_al_2016_result = transparency.guimaraes_et_al_2016(B04)

        assert isinstance(guimaraes_et_al_2016_result, numpy.ndarray)

