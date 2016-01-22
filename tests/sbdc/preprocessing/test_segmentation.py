# -*- coding: utf-8 -*-
from __future__ import absolute_import

import pytest
import numpy as np

from sbdc.preprocessing import ContiguousSegmentSet
from sbdc.exceptions import NotFittedError


_segments = [
    (
        'Lorem Ipsum is simply dummy text of the printing'
        ' and typesetting industry.'
    ),
    (
        'Lorem Ipsum has been the industry\'s standard dummy text ever'
        ' since the 1500s, when an unknown printer took a galley of type'
        ' and scrambled it to make a type specimen book.'
    ),
    (
        'It has survived not only five centuries, but also the leap into'
        ' electronic typesetting, remaining essentially unchanged.'
    ),
    (
        'It was popularised in the 1960s with the release of Letraset sheets'
        ' containing Lorem Ipsum passages, and more recently with desktop'
        ' publishing software like Aldus PageMaker including versions'
        ' of Lorem Ipsum.'
    ),
    (
        'The first line of Lorem Ipsum, "Lorem ipsum'
        ' dolor sit amet..", comes from a line in section 1.10.32.'
    )
]
_dataset = np.array(["\n\n".join(_segments), ])


def test_segments_default():
    segment_set = ContiguousSegmentSet()
    segment_set.fit(_dataset)
    segments = segment_set.transform()
    assert segments.shape == _dataset.shape
    assert len(segments[0]) == 5


def test_segments_defailt_fit_transform():
    segment_set = ContiguousSegmentSet()
    segments = segment_set.fit_transform(_dataset)
    assert segments.shape == _dataset.shape
    assert len(segments[0]) == 5


def test_segments_default_not_fitted():
    segment_set = ContiguousSegmentSet()
    with pytest.raises(NotFittedError):
        segment_set.transform()


def test_segments_min_length_vanish():
    segment_set = ContiguousSegmentSet(
        min_segment_length=150)
    segments = segment_set.fit_transform(_dataset)
    assert segments.shape == _dataset.shape
    assert len(segments[0]) == 2
    assert _segments[0] not in segments[0]
    assert _segments[1] in segments[0]
    assert _segments[2] not in segments[0]
    assert _segments[3] in segments[0]
    assert _segments[4] not in segments[0]


def test_segments_min_length_top():
    segment_set = ContiguousSegmentSet(
        min_segment_length=150,
        small_segment_vanish_strategy="top")
    segments = segment_set.fit_transform(_dataset)
    assert segments.shape == _dataset.shape
    assert len(segments[0]) == 2
    assert _segments[0] not in segments[0]
    assert "\n\n".join(_segments[1:3]) in segments[0]
    assert "\n\n".join(_segments[3:5]) in segments[0]


def test_segments_min_length_bottom():
    segment_set = ContiguousSegmentSet(
        min_segment_length=150,
        small_segment_vanish_strategy="bottom")
    segments = segment_set.fit_transform(_dataset)
    assert segments.shape == _dataset.shape
    assert len(segments[0]) == 2
    assert "\n\n".join(_segments[0:2]) in segments[0]
    assert "\n\n".join(_segments[2:4]) in segments[0]
    assert _segments[4] not in segments[0]


if __name__ == '__main__':
    pytest.main([__file__])
