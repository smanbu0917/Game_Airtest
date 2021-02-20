
from airtest.core.api import *

from Common.basepage import BasePage
from PageLocators.indexpage_loc import IndexPageLocator


class IndexPage(BasePage):
    # 点击start按钮
    def click_start_btn(self):
        IndexPageLocator.btn_start.click()
        sleep()
