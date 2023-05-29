import queue

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class GameState:
    def __init__(self):

        self.map = [
            ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1"],
            ["w1", "p1", "f1", "f1", "f1", "m1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "b1", "f1", "w1", "f1", "f1", "f1", "m2", "f1", "f1", "f1", "w1"],
            ["w1", "w1", "w1", "w1", "f1", "f1", "f1", "m1", "f1", "m1", "f1", "w1", "f1", "b1", "f1", "w1", "b1", "f1", "w1", "w1", "f1", "w1", "w1", "w1"],
            ["w1", "w1", "w1", "w1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "w1", "b1", "f1", "f1", "f1", "f1", "f1", "w1", "f1", "m2", "f1", "w1", "w1"],
            ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "f1", "b1", "f1", "b1", "f1", "f1", "w1", "f1", "m2", "f1", "w1", "w1"],
            ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "f1", "f1", "w1", "w1"],
            ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "f1", "m2", "w1", "w1"],
            ["w1", "w1", "f1", "k1", "w1", "h1", "w1", "k1", "f1", "f1", "f1", "m1", "f1", "f1", "f1", "w1", "w1", "w1", "w1", "w1", "h1", "f1", "w1", "w1"],
            ["w1", "f1", "f1", "f1", "f1", "f1", "w1", "h1", "f1", "m1", "f1", "f1", "f1", "m1", "f1", "w1", "w1", "w1", "w1", "w1", "w1", "c1", "w1", "w1"],
            ["w1", "f1", "f1", "f1", "f1", "f1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "f1", "w1", "w1", "w1", "f1", "f1", "f1", "f1", "f1", "w1"],
            ["w1", "f1", "f1", "m3", "f1", "f1", "f1", "w1", "f1", "f1", "f1", "f1", "w1", "w1", "f1", "w1", "w1", "f1", "f1", "f1", "w1", "w1", "f1", "w1"],
            ["w1", "m2", "f1", "w1", "f1", "w1", "f1", "f1", "f1", "f1", "f1", "f1", "w1", "w1", "f1", "w1", "w1", "f1", "m2", "f1", "w1", "f1", "m3", "w1"],
            ["w1", "w1", "d1", "w1", "f1", "w1", "f1", "f1", "f1", "f1", "f1", "f1", "c1", "d1", "f1", "f1", "d1", "f1", "w1", "f1", "f1", "f1", "f1", "w1"],
            ["w1", "f1", "f1", "w1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "w1", "w1", "f1", "w1", "w1", "f1", "f1", "f1", "w1", "f1", "f1", "w1"],
            ["w1", "treasure1", "f1", "w1", "f1", "m3", "f1", "w1", "f1", "f1", "f1", "f1", "w1", "w1", "f1", "w1", "w1", "f1", "f1", "h1", "w1", "f1", "k1", "w1"],
            ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1"]]

        # self.map = [
        #     ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1"],
        #     ["w1", "p1", "f1", "f1", "f1", "w1", "f1", "f1", "f1", "f1", "h1", "f1", "f1", "w1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "w1"],
        #     ["w1", "w1", "w1", "f1", "f1", "w1", "f1", "m2", "f1", "w1", "f1", "m2", "f1", "w1", "f1", "m1", "f1", "m1", "f1", "m1", "f1", "f1", "f1", "w1"],
        #     ["w1", "w1", "w1", "f1", "f1", "f1", "f1", "f1", "f1", "w1", "h1", "f1", "f1", "c1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "w1"],
        #     ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "m1", "f1", "w1"],
        #     ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "f1", "f1", "f1", "f1", "f1", "w1", "f1", "f1", "f1", "f1", "f1", "w1", "w1", "f1", "f1", "w1"],
        #     ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "f1", "f1", "f1", "f1", "f1", "w1", "f1", "f1", "f1", "f1", "f1", "w1", "w1", "w1", "m1", "w1"],
        #     ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "f1", "f1", "f1", "f1", "f1", "w1", "f1", "f1", "f1", "f1", "f1", "w1", "w1", "w1", "f1", "w1"],
        #     ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "f1", "w1"],
        #     ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "d2", "w1", "w1", "w1", "w1", "w1", "w1", "d2", "w1", "w1", "w1", "w1", "w1", "w1", "w1"],
        #     ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1"],
        #     ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1"],
        #     ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1"],
        #     ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1"],
        #     ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1"],
        #     ["w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1", "w1"]]
        self.health_bar = ["heart1", "heart1", "heart1"]

        self.player1Position = (1, 1)
        self.game_over = False
        self.die = False
        self.health = 3
        self.monster_list = [["m1", 0, 1, 5, -1, 0, 6, False], ["m1", 1, 2, 7, -1, 0, 5, False],
                             ["m1", 2, 2, 9, -1, 0, 4, False], ["m2", 3, 1, 19, 0, -1, 4, False],
                             ["m2", 4, 3, 20, 0, 1, 10, False], ["m2", 5, 4, 20, 0, -1, 15, False],
                             ["m2", 6, 6, 21, 0, -1, 8, False], ["m2", 7, 11, 18, 0, -1, 7, False],
                             ["m3", 8, 11, 22, (8, 16), (15, 23), 15, False], ["m1", 9, 8, 13, 1, 0, 10, False],
                             ["m1", 10, 7, 11, -1, 0, 11, False], ["m1", 11, 8, 9, 1, 0, 6, False],
                             ["m3", 12, 14, 5, (6, 0), (15, 12), 10, False],
                             ["m3", 13, 10, 3, (6, 0), (15, 12), 12, False], ["m2", 14, 11, 1, 0, -1, 7, False]]

        # self.monster_list = [["m2", 0, 2, 7, 0, 1, 3, False], ["m2", 1, 2, 11, 0, -1, 3, False],
        #                      ["m1", 2, 2, 15, 1, 0, 5, False], ["m1", 3, 2, 17, -1, 0, 3, False],
        #                      ["m1", 4, 2, 19, 1, 0, 4, False], ["m1", 5, 4, 21, 1, 0, 7, False],
        #                      ["m1", 6, 6, 22, 1, 0, 7, False], ["d2", 7, 9, 16, 0, 0, 30, True],
        #                      ["d2", 8, 9, 9, 0, 0, 26, True]]
        # [ name, id, row, col, direc_x, direc_y, 1/speed ]
        self.time = 0
        self.checkpoint = (1, 1)
        self.win = False
        self.save_state = True
        self.have_key = False
        self.checkpoint_control = [[0, 0], [0, 6], [7, 11], [12, 14], [0, 0]]
        self.number_of_checkpoints = 0

    def make_move(self, obj, move, id=0):
        if obj == 'player':
            row = self.player1Position[0]
            col = self.player1Position[1]
            endrow = row + move[0]
            endcol = col + move[1]
            if self.map[endrow][endcol] == 'f1':  # nếu không có chướng ngại vật
                self.let_go(endrow, endcol, row, col)
            elif self.map[endrow][endcol][0] == 'm':  # nếu gặp quái vật
                self.map[self.player1Position[0]][self.player1Position[1]] = 'f1'
                self.map[self.checkpoint[0]][self.checkpoint[1]] = 'p1'
                self.player1Position = self.checkpoint
                if self.health == 1:
                    self.game_over = True
                else:
                    self.die = True
            elif self.map[endrow][endcol] == 'treasure1':  # nếu đến đích
                self.map[endrow][endcol] = 'treasure2'
                self.win = True
            elif self.map[endrow][endcol] == 'b1':  # nếu gặp hộp có thể đẩy
                neighbor_row = endrow + move[0]
                neighbor_col = endcol + move[1]
                if self.map[neighbor_row][neighbor_col] == 'f1':
                    self.map[neighbor_row][neighbor_col] = 'b1'
                    self.let_go(endrow, endcol, row, col)
            elif self.map[endrow][endcol] == 'h1':  # nếu gặp healer
                if self.health < 3:
                    self.health += 1
                    self.health_bar[self.health - 1] = 'heart1'
                self.let_go(endrow, endcol, row, col)
            elif self.map[endrow][endcol][0] == 'c':  # nếu gặp checkpoint
                self.checkpoint = (endrow, endcol)
                self.save_state = True
                self.let_go(endrow, endcol, row, col)
            elif self.map[endrow][endcol] == 'k1':  # nếu gặp chìa khóa
                self.have_key = True
                self.let_go(endrow, endcol, row, col)
            elif self.map[endrow][endcol] == 'd1':  # nếu gặp cửa khóa
                if self.have_key:
                    self.have_key = False
                    x_new = 2 * endrow - row
                    y_new = 2 * endcol - col
                    if self.map[x_new][y_new][0] == 'c':
                        self.checkpoint = (x_new, y_new)
                        self.save_state = True
                    self.let_go(x_new, y_new, row, col)
            elif self.map[endrow][endcol] == 'f2': # nếu gặp lửa
                self.map[self.player1Position[0]][self.player1Position[1]] = 'f2'
                self.map[self.checkpoint[0]][self.checkpoint[1]] = 'p1'
                self.player1Position = self.checkpoint
                if self.health == 1:
                    self.game_over = True
                else:
                    self.die = True

        elif obj == 'm1' or obj == 'm2':  # di chuyển dọc, ngang
            if self.time % self.monster_list[id][6] == 0:
                row = self.monster_list[id][2]
                col = self.monster_list[id][3]  # tọa độ hiện tại của monster1, 2
                endrow = row + self.monster_list[id][4]
                endcol = col + self.monster_list[id][5]
                if self.map[endrow][endcol] == 'w1':
                    self.monster_list[id][4] *= -1
                    self.monster_list[id][5] *= -1
                elif self.map[endrow][endcol] == 'f1':
                    self.map[endrow][endcol] = obj
                    self.map[row][col] = 'f1'
                    self.monster_list[id][2] = endrow
                    self.monster_list[id][3] = endcol
                elif self.map[endrow][endcol][0] == 'p':
                    self.map[self.player1Position[0]][self.player1Position[1]] = 'f1'
                    self.map[self.checkpoint[0]][self.checkpoint[1]] = 'p1'
                    self.player1Position = self.checkpoint
                    if self.health == 1:
                        self.game_over = True
                    else:
                        self.die = True

                elif self.map[endrow][endcol] == 'b1':
                    self.monster_list[id][4] *= -1
                    self.monster_list[id][5] *= -1
                    self.make_move(obj, move, id)

        elif obj == 'm3':
            if self.time % self.monster_list[id][6] == 0:
                ai_move = self.bfs(self.monster_list[id][2], self.monster_list[id][3], self.monster_list[id][4][0], self.monster_list[id][4][1], self.monster_list[id][5][0], self.monster_list[id][5][1])
                if ai_move != -1:
                    self.monster_list[id][2] += direction[ai_move][0]
                    self.monster_list[id][3] += direction[ai_move][1]
                    x = self.monster_list[id][2]
                    y = self.monster_list[id][3]
                    if self.map[x][y][0] == 'p':
                        self.map[self.player1Position[0]][self.player1Position[1]] = 'f1'
                        self.map[self.checkpoint[0]][self.checkpoint[1]] = 'p1'
                        self.player1Position = self.checkpoint
                        if self.health == 1:
                            self.game_over = True
                        else:
                            self.die = True
                    else:
                        self.map[x][y] = 'm3'
                        self.map[x - direction[ai_move][0]][y - direction[ai_move][1]] = 'f1'
        elif obj == 'd2':
            tmp = self.monster_list[id][6]
            if self.time % tmp == 0:
                row = self.monster_list[id][2]
                col = self.monster_list[id][3]
                for c in range(col, col+3, 1):
                    for r in range(row-1, 0, -1):
                        if self.map[r][c][0] == 'f':
                            self.map[r][c] = 'f2'
                        elif self.map[r][c][0] == 'p':
                            self.map[self.player1Position[0]][self.player1Position[1]] = 'f2'
                            self.map[self.checkpoint[0]][self.checkpoint[1]] = 'p1'
                            self.player1Position = self.checkpoint
                            if self.health == 1:
                                self.game_over = True
                            else:
                                self.die = True
                        elif self.map[r][c][0] == 'w':
                            break
            elif self.time % tmp == tmp//2:
                row = self.monster_list[id][2]
                col = self.monster_list[id][3]
                for c in range(col, col+3, 1):
                    for r in range(row-1, 0, -1):
                        if self.map[r][c] == 'f2':
                            self.map[r][c] = 'f1'
                        elif self.map[r][c][0] == 'w':
                            break




    def let_go(self, a, b, c, d):
        self.map[a][b] = 'p1'
        self.map[c][d] = 'f1'
        self.player1Position = (a, b)

    def bfs(self, start_row, start_col, a, b, c, x):
        trace = {}
        visited = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        q = queue.Queue()
        q.put((start_row, start_col))
        visited[start_row][start_col] = 1
        for i in range(4):
            trace[(start_row + direction[i][0], start_col + direction[i][1])] = i
        while q.qsize() != 0:
            pos = q.get()
            endrow = pos[0]
            endcol = pos[1]
            if endrow == self.player1Position[0] and endcol == self.player1Position[1]:
                return trace[(endrow, endcol)]
            for d in direction:
                endrow += d[0]
                endcol += d[1]
                if self.map[endrow][endcol] != 'w1' and (endrow > a) and (endrow < c) and (endcol > b) and (endcol < x):
                    if visited[endrow][endcol] == 0:
                        if endrow - d[0] != start_row or endcol - d[1] != start_col:
                            trace[(endrow, endcol)] = trace[(endrow - d[0], endcol - d[1])]
                        visited[endrow][endcol] = 1
                        if self.map[endrow][endcol] == 'f1' or self.map[endrow][endcol] == 'p1':
                            q.put((endrow, endcol))
                endrow -= d[0]
                endcol -= d[1]
        return -1
