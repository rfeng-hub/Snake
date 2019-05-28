"""
贪吃蛇小游戏
"""
import sys
import time
import random
import pygame
from pygame.locals import *

# 定义颜色变量
RED = pygame.Color(255, 0, 0)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
GREY = pygame.Color(150, 150, 150)


def game_over(play_surface, score):
    game_over_font = pygame.font.SysFont('arial.tff', 54)  # 游戏结束字体和大小
    game_over_surf = game_over_font.render('Game Over!', True, GREY)  # 游戏结束内容显示
    game_over_rect = game_over_surf.get_rect()
    game_over_rect.midtop = (300, 10)  # 显示位置
    play_surface.blit(game_over_surf, game_over_rect)
    score_font = pygame.font.SysFont('arial.ttf', 54)  # 得分情况显示
    score_surf = score_font.render('Score:' + str(score), True, GREY)
    score_rect = score_surf.get_rect()
    score_rect.midtop = (300, 50)
    play_surface.blit(score_surf, score_rect)
    pygame.display.flip()  # 刷新显示界面
    time.sleep(5)  # 休眠五秒钟自动退出界面
    pygame.quit()
    sys.exit()


def main():
    # 初始化pygame
    pygame.init()
    fpsClock = pygame.time.Clock()
    # 创建pygame显示层
    playSurface = pygame.display.set_mode((600,460))
    pygame.display.set_caption('Snake Game')
    # 初始化变量
    snakePosition = [100,100] #贪吃蛇 蛇头的位置
    snakeSegments = [[100,100]] #贪吃蛇 蛇的身体，初始为一个单位
    raspberryPosition = [300,300] #树莓的初始位置
    raspberrySpawned = 1 #树莓的个数为1
    direction = 'right' #初始方向为右
    changeDirection = direction
    score = 0 #初始得分
    while True:
        # 检测例如按键等pygame事件
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # 判断键盘事件
                if event.key == K_RIGHT or event.key == ord('d'):
                    changeDirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changeDirection = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    changeDirection = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        # 判断是否输入了反方向
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection
        # 根据方向移动蛇头的坐标
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20
        # 增加蛇的长度
        snakeSegments.insert(0,list(snakePosition))
        # 判断是否吃掉了树莓
        if snakePosition[0] == raspberryPosition[0] and snakePosition[1] == raspberryPosition[1]:
            raspberrySpawned = 0
        else:
            snakeSegments.pop()
        # 如果吃掉树莓，则重新生成树莓
        if raspberrySpawned == 0:
            x = random.randrange(1,30)
            y = random.randrange(1,23)
            raspberryPosition = [int(x*20),int(y*20)]
            raspberrySpawned = 1
            score += 1
        # 绘制pygame显示层
        playSurface.fill(BLACK)
        for position in snakeSegments:
            pygame.draw.rect(playSurface,WHITE,Rect(position[0],position[1],20,20))
            pygame.draw.rect(playSurface,RED,Rect(raspberryPosition[0], raspberryPosition[1],20,20))
        # 刷新pygame显示层
        pygame.display.flip()
        # 判断是否死亡
        if snakePosition[0] > 600 or snakePosition[0] < 0:
            game_over(playSurface,score)
        if snakePosition[1] > 460 or snakePosition[1] < 0:
            game_over(playSurface,score)
        for snakeBody in snakeSegments[1:]:
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                game_over(playSurface,score)
        # 控制游戏速度
        fpsClock.tick(5)


if __name__ == '__main__':
    main()