import datetime
from typing import Callable


def wait_until(assertion: Callable, timeout: float = 5) -> None:
    """
    Waits until the assertion does not raise an AssertionError. If the timeout is reached the last AssertionError is raised.
    This can be used if state changes need some time to propagate.
    usage:
        def test_something():
            def my_assertion():
                assert actual == expected, f"Actual was {actual} but expected was {expected}"
            waiting.wait_until(my_assertion)
    Arguments:
        assertion: Callable: A function without argruments which has at least one assert statement
        timeout: int: The timeout in seconds
    """
    start = datetime.datetime.now()
    while True:
        try:
            assertion()
            break
        except AssertionError as ae:
            if datetime.datetime.now() - start > datetime.timedelta(seconds=timeout):
                raise AssertionError(
                    f"Timeout of {timeout} seconds exceeded.\n{ae}"
                ) from ae
