# -*- coding: utf-8 -*-

from sbdc.preprocessing import ContiguousSegmentSet
from sbdc.datasets import bbc_load

X = bbc_load()

cs = ContiguousSegmentSet(
    min_segment_length=100,
    small_segment_vanish_strategy="top")
cs.fit(X[:, 2])

text_segments = cs.transform()
print text_segments[:2]
