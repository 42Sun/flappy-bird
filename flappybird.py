
import pygame
import sys
import random



# 定义鸡类
class Chick(object):
    def __init__(self):

        self.chickRect = pygame.Rect(200, 350, 92, 102)#鸡的矩形

        self.chickStatus = [pygame.image.load("1.png"),
                           pygame.image.load("dead.png")]#鸡的活和死的状态
        self.status = 0
        self.chickX = 200      #初始X位置
        self.chickY = 350#初始Y位置
        self.jump = False#跳跃状态
        self.jumpSpeed = 10#跳跃速度（向上速度）
        self.gravity = 5#重力（向下速度）
        self.dead = False#初始是活着的
    # 鸡的位置状态更新
    def chickUpdate(self):
        if self.jump:#判定跳跃

            self.jumpSpeed -= 1
            self.chickY -= self.jumpSpeed
        else:
            # 小鸡坠落
            self.gravity += 0.2
            self.chickY += self.gravity
        self.chickRect[1] = self.chickY#更新小鸡状态

# 对管道的位置进行随机
def pipelineRandom():

     return -400
#管道类
class Pipeline(object):
    def __init__(self):
        """定义初始化方法"""
        self.wallx = 800
        self.pineUp = pygame.image.load("top2.png")
        self.pineDown = pygame.image.load("bottom2.png")
        self.wally = -300

    def updatePipeline(self):
        #管道移动
        self.wallx -= 10
        #管道的更新
        if self.wallx < -70:
            global score
            score += 1
            self.wallx = 800
            self.wally = random.randint(-400,-200)




#图像创建
def createMap():
    screen.fill((255,255,255))#默认颜色
    screen.blit(background,(0,0))#描绘背景
    # screen.blit(background,(0,0))#描绘背景

    screen.blit(Pipeline.pineUp,(Pipeline.wallx, Pipeline.wally))#上管道
    screen.blit(Pipeline.pineDown,(Pipeline.wallx, Pipeline.wally +850))#下管道
    Pipeline.updatePipeline()#更新管道


    if Chick.dead:
        Chick.status = 1
    elif Chick.jump:
        Chick.status = 0
    #描绘小鸡
    screen.blit(Chick.chickStatus[Chick.status],(Chick.chickX, Chick.chickY))
    #小鸡位置更新
    Chick.chickUpdate()
    screen.blit(font.render('得分:' +str(score), -1, (165, 42 ,42)), (320, 70))
    pygame.display.update()#刷新图像

#死亡检测
def checkDead():
    #上管矩形
    upRect = pygame.Rect(Pipeline.wallx, Pipeline.wally,98,495)
    #下管矩形
    downRect = pygame.Rect(Pipeline.wallx, Pipeline.wally + 850,94,499)
    #碰撞检测：碰到上管，碰到下管。碰到上边缘，碰到下边缘
    if upRect.colliderect(Chick.chickRect) or downRect.colliderect(Chick.chickRect) or Chick.chickRect[1] > height:
        Chick.dead = True
    if Chick.chickRect[1] > height:
        return True
    else:
        return False





def getResult():
    #游戏结束的文字
    final_text1 = "游戏结束"

    ft1_font = pygame.font.SysFont('simsunnsimsun', 70)
    ft1_surf = ft1_font.render(final_text1, 1, (242, 3, 36))

    screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 120])  # 设置第一行文字显示位置


    pygame.display.flip()






if __name__ == '__main__':
    #初始化
    pygame.init()
    pygame.font.init()
    #设定文字
    font = pygame.font.SysFont("simsunnsimsun",50)
    size = (width, height) = (800, 700)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Pipeline = Pipeline()
    Chick = Chick()
    score = 0
    i = 1
    #无限循环，直到游戏结束
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN)and not Chick.dead:
                Chick.status = 0
                Chick.jump = True
                Chick.gravity = 5
                Chick.jumpSpeed = 10

        if i == 1777:
            i = 1
        name = 'back/a (' + str(i) + ').jpg'
        background = pygame.image.load(name)

        i += 1

        if checkDead():
            getResult()
        else:
            createMap()

    pygame.quit()



