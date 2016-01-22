# -*- coding: utf-8 -*-
from __future__ import absolute_import

import pytest
from sbdc.datasets import bbc_load


def test_bbc_default():
    data_all_classes = bbc_load()
    assert data_all_classes is not None
    assert data_all_classes.shape[0] == 2225
    assert data_all_classes.shape[1] == 3


def test_bbc_custom_classes():
    data_politics = bbc_load(classes=["politics"])
    assert data_politics is not None
    assert data_politics.shape[0] == 417
    assert data_politics.shape[1] == 3


def test_bbc_invalid_custom_classes():
    data_politics = bbc_load(classes=["i_am_invalid"])
    assert data_politics is None

if __name__ == '__main__':
    pytest.main([__file__])
