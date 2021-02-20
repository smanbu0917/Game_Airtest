import pytest

from Common.basepage import BasePage


@pytest.fixture("class")
def start_app():
    BasePage.poco_android("poco").click()


