import msvcrt, time, os
from container import Container

score = 0
map_list = []
list_e = []
ct = Container(15, 25, map_list, list_e, score)

while 1:
    shut_down = ''
    if msvcrt.kbhit():
        lt = []
        try:
            control = msvcrt.getch().decode('utf-8')
            lt.append(control)
        except UnicodeDecodeError:
            pass

        i = 0
        while i < len(lt):
            if lt[i] == 'a':
                os.system('cls')
                st = ct.move_left()
                ct.view_print()
            elif lt[i] == 'd':
                os.system('cls')
                st = ct.move_right()
                ct.view_print()
            elif lt[i] == 's':
                os.system('cls')
                st = ct.trans_e()
                ct.view_print()
            elif lt[i] == 't':
                print('游戏结束，得分%s' %ct.score_get)
                exit()

            i += 2

    else:
        time.sleep(0.5)
        os.system('cls')
        st = ct.move_down()
        ct.view_print()
