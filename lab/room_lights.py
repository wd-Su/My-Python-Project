import fileinput

# 房间布局模板，只使用字母A-D代表不同区域的灯
ROOM_LAYOUT = '''
    Living Room
  AAAAAAAA
  A      A
  A  Dining A
  A  BBBB A
  A  B  B A
  A  BBBB A
  A      A
  AAAAAAAA
    Bedroom
  DDDDDDDD
  D      D
  D  CCCC D
  D  C  C D
  D  CCCC D
  D      D
  DDDDDDDD
'''

# ANSI清屏转义码：清除屏幕并将光标移到左上角
CLEAR_SCREEN = '\033[2J\033[1;1f'

# 灯光状态：0表示关闭(暗)，1表示打开(亮)
LIGHT_STATE = {
    0: '\033[30m■\033[0m',  # 暗方块（黑色）
    1: '\033[33m■\033[0m'   # 亮方块（黄色）
}

# 从输入读取控制指令并执行
for line in fileinput.input():
    # 执行输入的指令，例如"A=1; B=0; C=1; D=0"
    exec(line.strip())
    
    # 渲染房间灯光状态
    room_view = ROOM_LAYOUT
    # 替换每个灯光区域的状态
    for light in set(ROOM_LAYOUT):
        # 只处理A-D这几个字母，忽略其他字符
        if light.isalpha() and light in ['A', 'B', 'C', 'D']:
            # 获取该灯光的状态（0或1）
            state = globals()[light]
            # 替换为对应的灯光显示
            room_view = room_view.replace(light, LIGHT_STATE[state])
    
    # 清屏并显示当前房间灯光状态
    print(CLEAR_SCREEN + room_view)

