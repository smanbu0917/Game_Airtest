from PageLocators.gamepage_loc import GamePageLoc


class GamePage:

    # 拖动星星到贝壳
    def drag_and_drop(self):
        for star in GamePageLoc.star:
            star.drag_to(GamePageLoc.shell)
