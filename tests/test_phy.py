# -*- coding: utf-8 -*-
# @Author: gviejo
# @Date:   2022-04-04 22:40:51
# @Last Modified by:   Guillaume Viejo
# @Last Modified time: 2023-06-08 17:09:40

"""Tests of phy loader for `nwbmatic` package."""

import nwbmatic as ntm
import pynapple as nap
import numpy as np
import pandas as pd
import pytest
import warnings


@pytest.mark.filterwarnings("ignore")
def test_load_session():
    try:
        data = ntm.load_session("nwbfilestest/phy", "phy")
    except:
        data = ntm.load_session("tests/nwbfilestest/phy", "phy")


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        data = ntm.load_session("nwbfilestest/phy", "phy")
    except:
        data = ntm.load_session("tests/nwbfilestest/phy", "phy")


@pytest.mark.parametrize("data", [data])
class Test_PHY:
    def test_epochs(self, data):
        epochs = data.epochs
        assert isinstance(epochs, dict)
        assert "wake" in epochs.keys()
        for k in epochs.keys():
            assert isinstance(epochs[k], nap.IntervalSet)

    def test_spikes(self, data):
        assert isinstance(data.spikes, nap.TsGroup)
        assert len(data.spikes) == 3
        for i in data.spikes.keys():
            assert len(data.spikes[i])
