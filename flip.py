class Tile(object):
        def __init__(self):
                self.up = False
                self.contents = ' '
                self.string = '         '
                # self.string[i] notes
                # 0 = note: 0
                # 1 = decorative if flipped
                # 2 = note: 1
                # 3 = decorative if flipped
                # 4 = content
                # 5 = decorative if flipped
                # 6 = note: 2
                # 7 = decorative if flipped
                # 8 = note: 3
        def __str__(self):
                return self.string

        def _setstring(self,I,V):
                """T.setstring([index],[value]) -> Sets self.string's index to that value."""
                if   I not in range(9):
                        raise IndexError("Index must be [0:9]")
                elif type(V) != str:
                        raise TypeError("Value must be in string format")
                elif len(V) != 1:
                        raise TypeError("Value must be precisely one character")
                else:
                        self.string = self.string[:I] + str(V) + self.string[(I+1):]
        
        def note(self,n):
                """T.note([0,1,2 or 3]) -> Writes a note for the argument on the tile."""
                if self.up:
                        pass
                elif n == 0:
                        if self.string[0] == '0':
                                self._setstring(0,' ')
                        else:
                                self._setstring(0,'0')
                elif n == 1:
                        if self.string[2] == '1':
                                self._setstring(2,' ')
                        else:
                                self._setstring(2,'1')
                elif n == 2:
                        if self.string[6] == '2':
                                self._setstring(6,' ')
                        else:
                                self._setstring(6,'2')
                elif n == 3:
                        if self.string[8] == '3':
                                self._setstring(8,' ')
                        else:
                                self._setstring(8,'3')
                else:
                        raise TypeError("Tile object's note() requires 0,1,2,3 as input")

        def flip(self,ready=True):
                if not ready:
                        self.__init__()
                elif self.up == None:
                        pass
                elif self.up:
                        self.string = '         '
                        self.up = False
                else:
                        self.string = '*********'
                        self._setstring(4,self.contents)
                        self.up = True
class Data(object):
        def __init__(self):
                self.row = [[0,0] for i in xrange(5)]
                self.col = [[0,0] for i in xrange(5)]
        def reset(self):
                self.__init__()
        def collect_data(self,tiles):
                self.__init__()
                for t in xrange(len(tiles)):
                        self.row[t/5][1] += int(tiles[t].contents)
                        self.col[t%5][1] += int(tiles[t].contents)
                        if tiles[t].contents == '0':
                                self.row[t/5][0] += 1
                                self.col[t%5][0] += 1
                
class Board(object):
        def __init__(self):
                self.T = [Tile() for n in xrange(25)]
                self.score = 1
                self.data = Data()
        def __str__(self):
                border = '+ --- + --- + --- + --- + --- +'
                mini_border = '+ --- +'

                #
                ##
                ### Crafts the board

                # The Scoreboard
                output = 'Score: ' + str(self.score) + '\n'
                
                # For each row of tiles
                for Z in xrange(5):
                        output += border + ' ' + mini_border + '\n'

                        # For each inner line
                        for i in [0,3,6]:
                                
                                # For each tile
                                for t in xrange((Z*5),(Z*5)+5):
                                        output += '| ' + str(self.T[t])[i:i+3] + ' '

                                # /end tile
                                # prints side data
                                if   i == 0:      output += '| |S: **|\n'
                                elif i == 3:      output += '| | ~~~ |\n'
                                elif i == 6:      output += '| |0: **|\n'

                        # /end line
                        
                # /end row
                output += border + ' ' + mini_border

                # prints bottom data
                output += '\n' + border + '\n'
                
                # sums
                for c in xrange(5):
                        output += '|S: '
                        if (self.data.col[c][1])/10 < 1: output += ' '
                        output += str(self.data.col[c][1])
                output += '|\n' + ('| ~~~ ' * 5) + '|\n'
                
                # zeroes
                for c in xrange(5):
                        output += '|0:  ' + str(self.data.col[c][0])
                output += '|\n'
                output += border
                
                #
                return output

        def reset(self):
                self.score = 1
                self.data.reset()
                for tile in self.T:
                        tile.flip(False)
        def start_game(self):
                self.reset()
                
                from random import randint
                for tile in self.T:
                        tile.contents = str(randint(0,3))

                self.data.collect_data(self.T)
                print self
