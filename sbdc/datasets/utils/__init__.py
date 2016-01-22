# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import urllib
import zipfile

"""
Datasets Utils.

"""

__all__ = ["download_zip"]


def download_zip(origin, folder):
    """Download and extract file from the `origin` to the `folder`.

    Parameters
    ----------
    origin: str
        Origin URL of the file to download.

    folder: str
        Relative path of the folder where to store the results.

    Returns
    -------
    path: str
        Absolute path where results are stored.

    """
    exists, path = _prepare_sbdc_path(folder)
    if exists:
        return path

    filehandle, _ = urllib.urlretrieve(origin)
    zip_file_object = zipfile.ZipFile(filehandle, 'r')
    zip_file_object.extractall(path)

    return path


def _prepare_sbdc_path(folder):
    """Build the absolute path for the `folder` under sbdc path.

    Parameters
    ----------
    folder: str
        Relative path of the folder where to store the results.

    Returns
    -------
    (exists, path): tuple
        Absolute path of the folder and flag if it exists.

    """
    sbdc_home = os.path.expanduser(os.path.join('~', '.sbdc'))
    if not os.access(sbdc_home, os.W_OK):
        sbdc_home = os.path.join('/tmp', '.sbdc')

    datasets_home = os.path.join(sbdc_home, 'datasets')
    if not os.path.exists(datasets_home):
        os.makedirs(datasets_home)

    path = os.path.join(datasets_home, folder)
    return os.path.exists(path), path
