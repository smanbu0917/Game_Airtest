from Common.basepage import BasePage


class GamePageLoc:
    # 贝壳
    shell = BasePage.poco_unity("shell")
    # play
    play = BasePage.poco_unity("play")
    # star
    star = BasePage.poco_unity('plays').offspring('star')
    # score
    score = BasePage.poco_unity("scoreVal")