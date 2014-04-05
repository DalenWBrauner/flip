import flip as TileGame
import time
import webbrowser

YESNO =     ['Y','N','YES','NO']
YES =       ['Y','YES']
NO =        ['N','NO']
ROWSCOLS =  ['1','2','3','4','5']
NOTES =     ['0','1','2','3','D','DONE']
DONE =      ['D','DONE']
OPTIONS =   ['F','FLIP','N','NOTE','Q','QUIT']
BGM =       'http://www.listenonrepeat.com/watch/?v=nPSDHk_lyrc'
LETTERS =   'ABCDEFGHIJKLMNOPQRSTUVWXY'
# Given a string letter L, ALPH_NUM[L] outputs L's position in the string.
ALPH_NUM =  {}
for position in xrange(25):
    ALPH_NUM[LETTERS[position]] = position

        
def ask_question(question, desired_inputs, error_msg=None):
    """Returns the user's input after assuring it's valid."""
    if error_msg == None: error_msg = question
    inp = raw_input(question).upper()
    while inp not in desired_inputs:
        inp = raw_input(error_msg)
    return inp

def all_up(board):
    for t in board.T:
        t.up = False
        t.flip()
    print board

def prep():
    # Asks the user if they want to hear BGM
    mu = ask_question("(Did you want music? y/n) ",
                      YESNO,
                      "(Sorry, what was that?) ")
    if mu in YES:
        webbrowser.open(BGM)

    # Gives the user a moment
    print "ALL RIGHT",
    for z in xrange(3):
        time.sleep(.4)
        print ".",
    print "\nShow me how you play and make my heart pound with excitement!"
    time.sleep(2)

    # Planned Feature:
    #print "Press Ctrl+C at any time to cancel what you're doing."

def pick_a_tile(board):
    """ Asks the user to pick a tile! """
    theysaid = ask_question("Okay! Select a tile! ",
                            LETTERS,
                            "Sorry, what was that? We need a letter from A to Y. ")
    translation = ALPH_NUM[theysaid]
    if board.T[translation].up:
        print "Please pick a tile that isn't already flipped!"
        return None
    
    return translation
        
def notetaking(board):
    pass

def main():
    prep()
    Total_Score = 0
    playing = True
    B = TileGame.Board()
    while not (playing in NO):
        print "Total Score:",Total_Score
        B.start_game()
        GAME = "READY!"
        while GAME == "READY!":
            
            # Asks the user to make a play
            tile_or_note = ask_question(
                "Flip a tile (F), write a Note (N) or Quit (Q)? ",
                OPTIONS)

            if tile_or_note in ['Q','QUIT']:
                GAME = "QUIT"
            
            # If we're flipping the tile:
            elif tile_or_note in ['F','FLIP']:
                which_tile = pick_a_tile(B)
                if not (which_tile is None):
                    B.flip(which_tile)
                    if   B.score == 0:
                        GAME = "OVER"
                    elif B.score == B.maxscore:
                        GAME = "WON"
                    print B     # Show the user their changes

            # If we're making a note:
            elif tile_or_note in ['N','NOTE']:
                which_tile = pick_a_tile(B)
                if not (which_tile is None):
                    newt = ask_question(
                        "Which numbers are you jotting down?"+\
                        "\n(whenever you finish type: done) ",
                        NOTES,
                        "Err, please type in 0, 1, 2, 3, or done. ")
                    while newt not in DONE:
                        B.T[which_tile].note(newt)
                        print B     # Show the user their changes
                        newt = ask_question(
                            "And? ",
                            NOTES,
                            "Err, please type in 0, 1, 2, 3, or done. ")
            else:
                print "Wait, how did you get HERE?"
                time.sleep(.5)
                print "Definitely contact the developers."
                time.sleep(1)
                print "Tell them",tile_or_note,"sent ya!"

            # The user has taken their turn!


        # This round has ended:
        Total_Score += B.score
        if   GAME == "OVER":
            print "KABOOM! Better luck next time!"
            all_up(B)
        elif GAME == "WON":
            print "Amazing job!"
            all_up(B)
        elif GAME == "QUIT":
            print "Can't fault you for that!"
            all_up(B)
        playing = ask_question("Ready to play again? (y/n) ", YESNO)

    # The user is done playing:
    end = '\n'
    end *= 64
    end += "Thanks for playing!"
    print end
    time.sleep(4)
    # And the game is over!

if __name__ == "__main__": main()
