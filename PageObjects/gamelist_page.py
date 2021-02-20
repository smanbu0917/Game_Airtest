from airtest.core.api import *

from Common.basepage import BasePage
from PageLocators.gamelistpage_loc import GameListPageLocator


class GameListPage:

    # 点击drag drop游戏按钮
    def click_drag_drop(self):
        GameListPageLocator.drag_and_drop.click()
        sleep()
