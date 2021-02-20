from airtest.core.api import *
from poco.drivers.unity3d import UnityPoco
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


class BasePage:
    auto_setup(__file__)
    poco_unity = UnityPoco()
    poco_android = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
