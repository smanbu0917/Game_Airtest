import pytest

from PageLocators.gamepage_loc import GamePageLoc
from PageObjects.game_page import GamePage
from PageObjects.gamelist_page import GameListPage, assert_equal
from PageObjects.index_page import IndexPage

@pytest.mark.usefixtures("start_app")
class TestDragAndDrop:
    def test_drag_drop(self):
        IndexPage.click_start_btn(self)
        GameListPage.click_drag_drop(self)
        GamePage.drag_and_drop(self)
        value = GamePageLoc.score.attr("text")
        assert_equal(value, "100", "断言分数为100")
