# -*- coding: utf-8 -*-

__all__ = ['NotFittedError', ]


class NotFittedError(ValueError, AttributeError):
    """Exception class to raise if estimator is used before fitting.
    This class inherits from both ValueError and AttributeError to help with
    exception handling and backward compatibility.
    Examples
    --------
    >>> from sdbc.preprocessing import ContiguousSegmentSet
    >>> from sdbc.exceptions import NotFittedError
    >>> try:
    ...     ContiguousSegmentSet().predict([["hello world"]])
    ... except NotFittedError as e:
    ...     print(repr(e))
    """
