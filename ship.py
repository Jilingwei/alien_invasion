import pygame


class Ship:
    """ 飞船类 """

    def __init__(self, ai_game):

        self.screen = ai_game.screen  # 把屏幕赋值一份到ship属性，方便访问
        self.screen_rect = ai_game.screen.get_rect()  # 返回渲染文本的大小和偏移量

        self.settings = ai_game.settings
        self.image = pygame.image.load('imgaes/ship.bmp')  # 获取图片

        self.rect = self.image.get_rect()

        # 飞船的初始化位置
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """ 指定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ 根据移动标志调整飞船位置 """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.speed

        self.rect.x = self.x
