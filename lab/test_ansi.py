# 清屏指令：清空屏幕并把光标移到左上角
CLEAR_SCREEN = '\033[2J\033[1;1f'

# 带颜色的方块
LIGHT_STATE = {
        0:'\033[30m■\033[0m',
        1:'\033[33m■\033[0m'
        }

print("一秒后清屏")
import time
time.sleep(1)
print(CLEAR_SCREEN)

# 彩色方块
print("关闭的灯: " , LIGHT_STATE[0])
print("关闭的灯: " , LIGHT_STATE[1])


