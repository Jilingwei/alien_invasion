import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """ 管理游戏资源和行为的类 """

    def __init__(self):
        pygame.init()  # 初始化背景设置
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))  # 创建一个显示窗口
        pygame.display.set_caption("Alien Invasion")

        self.bg_color = self.settings.bg_color  # 设置背景颜色

        self.ship = Ship(self)  # 构建飞船类

    def run_game(self):
        """ 游戏的主循环 """
        while True:
            """ 监听键盘和鼠标的事件 """
            self._check_events()
            self._update_screen()
            self.ship.update()

    def _check_events(self):
        """ 获取事件列表 """
        for event in pygame.event.get():  # get events from the queue
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        """ 更新屏幕 """
        self.screen.fill(self.bg_color)  # 重新绘制屏幕
        self.ship.blitme()  # 重新绘制飞船

        pygame.display.flip()  # Update the full display Surface to the screen


if __name__ == "__main__":
    # 创建AlienInvasion实例
    ai = AlienInvasion()
    # 运行AlienInvasion
    ai.run_game()
