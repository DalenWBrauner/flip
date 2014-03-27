from random import randint

class Tile(object):
    def __init__(self):
        self.up = False
        self.contents = ' '
        self._string = '         '
        # self._string[i] notes
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
        return self._string

    def _setstring(self,I,V):
        """T._setstring([index],[value])
        Sets self._string's index to that value."""
        if   I not in range(9):
            raise IndexError("Index must be [0:9]")
        elif type(V) != str:
            raise TypeError("Value must be in string format")
        elif len(V) != 1:
            raise TypeError("Value must be precisely one char")
        else:
            self._string = self._string[:I] + str(V) + self._string[(I+1):]
    
    def note(self,n):
        """T.note([0,1,2,3])
        Writes a note for the argument on the tile."""
        if self.up:
            pass
        elif n == '0':
            if self._string[0] == '0':
                self._setstring(0,' ')
            else:
                self._setstring(0,'0')
        elif n == '1':
            if self._string[2] == '1':
                self._setstring(2,' ')
            else:
                self._setstring(2,'1')
        elif n == '2':
            if self._string[6] == '2':
                self._setstring(6,' ')
            else:
                self._setstring(6,'2')
        elif n == '3':
            if self._string[8] == '3':
                self._setstring(8,' ')
            else:
                self._setstring(8,'3')
        else:
            ERR = "Tile object's note() requires 0,1,2,3 as input"
            ERR += ", not " + str(n) + " of type " + str(type(n))
            raise TypeError(ERR)

    def flip(self,ready=True):
        if not ready:
            self.__init__()
        elif self.up == None:
            pass
        elif self.up:
            self._string = '         '
            self.up = False
        else:
            self._string = '*********'
            self._setstring(4,self.contents)
            self.up = True
            return self.contents
        
class Data(object):
    """Collects the values in each row and col, along with
    how many zeroes."""
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
        self.maxscore = self.score = 1
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
                if   i == 0:
                    output += '| |S: '
                    if (self.data.row[Z][1])/10 < 1: output += ' '
                    output += str(self.data.row[Z][1]) + '|\n'
                elif i == 3:      output += '| | ~~~ |\n'
                elif i == 6:
                    output += '| |0:  '
                    output += str(self.data.row[Z][0]) + '|\n'

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
        self.maxscore = self.score = 1
        self.data.reset()
        for tile in self.T:
            tile.flip(False)
                            
    def start_game(self):
        self.reset()
        for tile in self.T:
            point = randint(0,3)
            if point != 0:
                self.maxscore *= point
            tile.contents = str(point)
        self.data.collect_data(self.T)
        print self
