import random, time

class Container():
    def __init__(self, width, height, map_list, list_e, score_get):
        self.width = width
        self.height = height
        self.map_list = map_list
        self.list_e = self.e_make()
        self.score_get = score_get

#判断I元素是否能移动，能动返回0，不能动返回1
    def state_e(self, list_e):
        set1 = set()
        for i in list_e:
            #不能往左移
            if ((i[1] - 1) < 0) or ([i[0],(i[1] - 1)] in self.map_list):
                set1.add(1)
            #不能往右移
            if ((i[1] + 1) > self.width) or ([i[0],(i[1] + 1)] in self.map_list):
                set1.add(2)
            #不能往下移
            if ((i[0] + 1) > self.height) or ([(i[0] + 1), i[1]] in self.map_list):
                set1.add(3)
            #左右下都不能移动
            if ([(i[0] + 1),i[1]] in self.map_list) and ([i[0],(i[1] - 1)] in self.map_list) and ([i[0],(i[1] + 1)] in self.map_list) and (((i[1] - 1) < 0)) and ((i[1] + 1) > self.width) and ((i[0] + 1) > self.height):
                set1.add(4)
            # elif i in self.map_list:
            #     return 1
        return set1

    #向下移动I元素，不能移动返回1
    def move_down(self):
        st = self.state_e(self.list_e)
        if (4 in st) or (3 in st):
            self.e_to_c(self.list_e)
            self.score()
            self.list_e = self.e_make()
            return 1
        elif 3 not in st:
            for i in self.list_e:
                i[0] += 1
            return 0

    #向左移动I元素，不能移动返回1
    def move_left(self):
        st = self.state_e(self.list_e)
        if (4 in st):
            self.e_to_c(self.list_e)
            self.score()
            self.list_e = self.e_make()
            return 1
        elif (1 in st):
            return 0
        elif 1 not in st:
            for i in self.list_e:
                i[1] -= 1

    #向右移动I元素，不能移动返回1
    def move_right(self):
        st = self.state_e(self.list_e)
        if (4 in st):
            self.e_to_c(self.list_e)
            self.score()
            self.list_e = self.e_make()
            return 1
        elif 2 in st:
            return 0
        elif 2 not in st:
            for i in self.list_e:
                i[1] += 1

    #元素变形；变形原理是线性变换，坐标轴的每个坐标点旋转90度后，x，y交换位置，y*（-1）；
    def trans_e(self):
        x, y, z, a, b= [], [], [], [], []
        for i in self.list_e:
            x.append(i[0])
            y.append(i[1])
            z.append([i[1] * (-1), i[0]])
        x.sort(); y.sort()
        max_num = max(x[3], y[3])
        min_num = min(x[3], y[3])
        mid_list = [[k[0] + max_num, k[1]] for k in z]
        for i in mid_list:
            a.append(i[0])
            b.append(i[1])
        a.sort(); b.sort()
        final_list = [[k[0] - a[0] + x[0],k[1] - b[0] + y[0]] for k in mid_list]
        if self.state_e(final_list):
            return
        else:
            self.list_e = final_list

    def e_to_c(self, list_e):
        for i in list_e:
            self.map_list.append(i)

    def score(self):
        count = 0
        row_del = []
        new_map = []
        self.map_list.sort()
        for i in range(self.height + 1):
            for j in range(self.width + 1):
                if [i, j] in self.map_list:
                    count += 1
            if count == self.width + 1:
                self.score_get += 10
                row_del.append(i)
                count = 0
            else:
                count = 0
        for row in row_del:
            for e in range(self.width + 1):
                self.map_list.remove([row, e])
        if row_del:
            for row in row_del:
                for i in range(len(self.map_list)):
                    if self.map_list[i][0] < row:
                        self.map_list[i][0] += 1

    def e_make(self):
        for a in self.map_list:
            if a[0] == 0:
                print("游戏结束，得分：%s" %self.score_get)
                exit()
        element = []
        element.append([[0, 3], [0, 4], [0, 5], [0, 6]]) #I
        element.append([[-3, 3], [-2, 3], [-1, 3], [0, 3]]) #I
        element.append([[0, 3], [0, 4], [0, 5], [1, 4]]) #T
        element.append([[0, 3], [0, 4], [0, 5], [-1, 4]]) #T
        element.append([[0, 3], [0, 4], [0, 5], [1, 5]]) #J
        element.append([[0, 3], [0, 4], [0, 5], [1, 3]]) #L
        element.append([[0, 3], [0, 4], [1, 3], [1, 4]]) #O
        element.append([[0, 3], [0, 4], [1, 3], [1, 4]]) #O
        element.append([[0, 3], [0, 4], [1, 2], [1, 3]]) #S
        element.append([[0, 3], [0, 4], [1, 4], [1, 5]]) #Z
        return random.choice(element)

    def view_print(self):
        all_list = self.map_list + self.list_e
        for i in range(self.height + 1):
            for j in range(self.width + 1):
                if ([i, j] in all_list):
                    print('口', end='')
                else:
                    print('--', end='')
            print()


