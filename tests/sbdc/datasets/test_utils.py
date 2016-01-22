# -*- coding: utf-8 -*-
from __future__ import absolute_import

import mock
import os
import pytest
from sbdc.datasets.utils import download_zip, _prepare_sbdc_path


@mock.patch('sbdc.datasets.utils.os')
def test_prepare_sbdc_path_tmp(mock_os):
    mock_os.access.return_value = False
    mock_os.path = os.path

    exists, path = _prepare_sbdc_path("unexisting_folder")
    assert path == "/tmp/.sbdc/datasets/unexisting_folder"
    assert exists is False


@mock.patch('sbdc.datasets.utils.os.path')
@mock.patch('sbdc.datasets.utils.os')
def test_prepare_sbdc_path_tmp_missing(mock_os, mock_path):
    mock_os.access.return_value = False
    mock_os.makedirs.return_value = True
    mock_path.exists.return_value = False
    mock_path.join = os.path.join

    exists, path = _prepare_sbdc_path("unexisting_folder")
    mock_os.makedirs.assert_called_with("/tmp/.sbdc/datasets")
    assert path == "/tmp/.sbdc/datasets/unexisting_folder"


@mock.patch('sbdc.datasets.utils.urllib')
@mock.patch('sbdc.datasets.utils.zipfile')
@mock.patch('sbdc.datasets.utils._prepare_sbdc_path')
def test_download_zip(mock_path, mock_zipfile, mock_urllib):
    mock_path.return_value = (False, "/tmp/.sbdc/datasets/folder")
    mock_urllib.urlretrieve.return_value = (True, True)
    mock_zipfile.ZipFile.return_value = mock.MagicMock(return_value=True)

    path = download_zip("http://test.url", "folder")
    mock_path.assert_called_with("folder")
    mock_urllib.urlretrieve.assert_called_with("http://test.url")
    assert path == "/tmp/.sbdc/datasets/folder"


if __name__ == '__main__':
    pytest.main([__file__])
