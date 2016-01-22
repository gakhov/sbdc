# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
import glob
import numpy as np

from .utils import dowload

"""
BBC News dataset.

This dataset consists of 2225 documents from the BBC news website
corresponding to stories in five topical areas from 2004-2005.

Natural Classes: 5 (business, entertainment, politics, sport, tech)

Official website: http://mlg.ucd.ie/datasets/bbc.html

References
----------
[1] D. Greene and P. Cunningham.
    Practical Solutions to the Problem of Diagonal Dominance
    in Kernel Document Clustering", Proc. ICML 2006.
"""

DATASET_CLASSES = set([
    'business',
    'entertainment',
    'politics',
    'sport',
    'tech'
])
DATASET_URL = "http://mlg.ucd.ie/files/datasets/bbc-fulltext.zip"


def load(classes=None):
    """Load BBC News dataset.

    Read more with the http://mlg.ucd.ie/datasets/bbc.html

    Parameters
    ----------
    classes: iterable or None, optional (default=None)
        List of required classes to load. If None, all classes will be loaded.

    Returns
    -------
    documents: array-like, shape (n_documents, 3)
        Return matrix with 3 columns: class, title, text

    """

    path = dowload(DATASET_URL, "bbc")

    classes = DATASET_CLASSES & set(classes) if classes else DATASET_CLASSES
    if not classes:
        return None

    documents = []
    for cls in classes:
        files = os.path.join(path, "bbc", cls, "*.txt")
        for filepath in glob.glob(files):
            with open(filepath) as f:
                title, text = f.read().split("\n", 1)
                documents.append([cls, title.strip(), text.strip()])

    return np.array(documents)
