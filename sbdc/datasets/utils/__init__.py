# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import urllib
import zipfile

"""
Datasets Utils

"""


def dowload(origin, folder):
    """Download and (if needed) extract file from the origin to the folder

    Parameters
    ----------
    origin: str
        Origin URL of the file to download

    folder: str
        Relative path of the folder where to store the result.

    Returns
    -------
    path: str
        Absolute path where result is stored

    """
    sbdc_home = os.path.expanduser(os.path.join('~', '.sbdc'))
    if not os.access(sbdc_home, os.W_OK):
        sbdc_home = os.path.join('/tmp', '.sbdc')

    datasets_home = os.path.join(sbdc_home, 'datasets')
    if not os.path.exists(datasets_home):
        os.makedirs(datasets_home)

    path = os.path.join(datasets_home, folder)
    if os.path.exists(path):
        return path

    filehandle, _ = urllib.urlretrieve(origin)
    zip_file_object = zipfile.ZipFile(filehandle, 'r')
    zip_file_object.extractall(path)

    return path
