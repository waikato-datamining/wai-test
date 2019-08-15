import functools

from .. import AbstractTest
from .._constants import IS_TEST_ATTRIBUTE
from .._functions import is_test


def Test(method):
    """
    Decorator which marks a class method as a unit test.

    :param method:  The class method to mark.
    """
    # Abort if the method is already a test
    if is_test(method):
        return method

    # Label the method as a test (will be inherited by wrapper)
    setattr(method, IS_TEST_ATTRIBUTE, True)

    # Wrap the method in the testing infrastructure
    @functools.wraps(method)
    def when_called(test: AbstractTest):
        subject = test.subject()
        resources = test.load_common_resources()

        return method(test, subject, *resources)

    return when_called
