class Tile(object):
        def __init__(self):
                self.up = False
                self.contents = '0'
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

class Board(object):
        def __init__(self):
                self.T = [Tile() for n in xrange(25)]
        def __str__(self):
                border = '+ --- + --- + --- + --- + --- +'
                mini_border = '+ --- +'
                output = ''

                #
                ##
                ### Crafts the board
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
                                output += '| | ~~~ |\n'

                        # /end line
                        
                # /end row
                output += border + ' ' + mini_border

                # prints bottom data
                output += '\n' + border + '\n'
                for thingy in xrange(3):
                        output += ('| ~~~ ' * 5) + '|\n'
                output += border
                return output

        def reset(self):
                for tile in self.T:
                        tile.flip(False)

B = Board()
