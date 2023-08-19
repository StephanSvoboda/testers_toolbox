import datetime
import pytest
from testers_toolbox import waiting


def test_wait_until_success():
    def assertion():
        assert True

    waiting.wait_until(assertion=assertion)


def test_wait_until_timeout():
    def assertion():
        assert False

    with pytest.raises(AssertionError):
        waiting.wait_until(assertion=assertion, timeout=0.5)


def test_wait_until_delayed_succesful_assertion():
    timeout = 0.5
    start = datetime.datetime.now()

    def assertion():
        if datetime.datetime.now() - start > datetime.timedelta(seconds=timeout/2):
            assert True
            return
        assert False

    waiting.wait_until(assertion=assertion, timeout=timeout)


def test_wait_until_nice_reporting():
    def assertion():
        assert 1 == 2, f"Actual was 1 but expected was 2"

    with pytest.raises(
        AssertionError,
        match="Timeout of 0.5 seconds exceeded.\nActual was 1 but expected was 2\nassert 1 == 2",
    ):
        waiting.wait_until(assertion=assertion, timeout=0.5)
