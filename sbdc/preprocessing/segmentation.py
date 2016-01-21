# -*- coding: utf-8 -*-
from __future__ import absolute_import

import numpy as np

from ..exceptions import NotFittedError

"""
Every document could be considered as being composed of contiguous,
non-overlaping chunks of text, called segments. A set of segments
called segment-set.

A segment-set is called `contiguous` if there exists a permutation such that
segments in it are ordereed according to the document parsing order and
there are "gaps" between them.

References
----------
[1] A. Tagarelli, G. Karypis.
    A Segment-based Approach To Clustering Multi-Topic Documents.
    In "Knowledge and Information Systems", Vol. 34 (2013), No. 3, pp. 5s63-595
"""


class ContiguousSegmentSet(object):
    def __init__(self,
                 min_segment_length=None,
                 small_segment_vanish_strategy=None,
                 post_clustering=False,
                 n_clusters=None):
        """Document representation with contiguous segment-set.

        Segmentation of the document is done using paragraph-based
        segment definition. To ensure that segments contain different
        topics, it is possible to run post-clustering algorithm to
        cluster segments with the same topic into "super-segments"
        (also called segments at the end).

        Parameters
        ----------
        min_segment_length: int or None, optinal (default=None).
            Minimum length of the paragraph-based segment.
            If None, segments of any length are kept.

        small_segment_vanish_strategy: str or None, optinal (default=None)
            The strategy used to deal with small paragraph-based segments.
            It is ignored if ``min_segment_length`` is None.
                - If None, then ignore small segments completely.
                - If "top", then merge with previous segment (if any).
                - If "bottom", then merge with next segment (if any).

        post_clustering: boolean, optional (default=False).
            Apply clustering of similar-topic segments into supersegments.

        n_clusters: int, float or None, optional (default=None)
            The number of clusters in post-clustering algorithm:
                - If int, then cluster with `n_clusters` clusters.
                - If float, then `n_clusters` is a percentage and cluster with
                  `n_clusters * n_segments` clusters.

            Applicable only if ``post_clustering`` is True.
            If None then ``post_clustering`` will be ignored.
        """
        self._X_fit = None

        self.min_segment_length = min_segment_length
        self.small_segment_vanish_strategy = small_segment_vanish_strategy
        self.post_clustering = post_clustering
        self.n_clusters = n_clusters

    def fit(self, X, **params):
        """Fit the model from the array X of texts.

        Parameters
        ----------
        X: array-like, shape (n_samples, )
            Text vector, where n_samples is the number of texts.

        Returns
        -------
        self : object
            Returns the instance of itself.
        """
        self._X_fit = X

    def fit_transform(self, X, **params):
        """Fit the model from the text.

        Parameters
        ----------
        X: array-like, shape (n_samples, )
            Text vector, where n_samples is the number of texts.

        Returns
        --------
        segments: array-like, shape (n_samples, n_segments)
            Segment-set from each text in the X
        """
        self.fit(X, **params)

        segments = self.transform()
        return segments

    def transform(self):
        """Transform fitted vector with texts.

        Returns
        -------
        segments: array-like, shape (n_samples, n_segments)
            Segment-set from each text in the fitted X
        """
        if self._X_fit is None:
            raise NotFittedError("Model not fitted, "
                                 "call `fit` before exploiting the model.")

        segments = self._paragraph_based_segments(self._X_fit)
        return segments

    def _paragraph_based_segments(self, X):
        """Paragraph-based segmentation.

        Parameters
        ----------
        X: array-like, shape (n_samples, )
            Text vector, where n_samples is the number of texts.

        Returns
        --------
        segments: array-like, shape (n_samples, n_segments)
            Segment-set from each text in the X
        """

        def split_by_paragraph(text):
            segments = text.split("\n\n")
            return segments

        split_by_paragraph = np.vectorize(
            split_by_paragraph, otypes=[np.ndarray])
        return split_by_paragraph(X)
