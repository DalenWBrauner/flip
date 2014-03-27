import flip as TileGame
import time
import webbrowser

YESNO =     ['y','n','Y','N','YES','NO','Yes','No','yes','no']
YES =       ['y','Y','YES','Yes','yes',]
NO =        ['n','N','NO','No','no']
ROWSCOLS =  ['1','2','3','4','5']
NOTES =     ['0','1','2','3','DONE','Done','done']
DONE =      ['DONE','Done','done']
BGM =       'http://www.listenonrepeat.com/watch/?v=nPSDHk_lyrc'
        
def ask_question(question, desired_inputs, error_msg=None):
    """Returns the user's input after assuring it's valid."""
    if error_msg == None: error_msg = question
    inp = raw_input(question)
    while inp not in desired_inputs:
        inp = raw_input(error_msg)
    return inp

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

def main():
    prep()
    playing = True
    B = TileGame.Board()
    while not (playing in NO):
        B.start_game()
        GAME = "READY!"
        while GAME != "OVER":
            
            # Asks the user if they want to flip a tile or write a note
            tile_or_note = ask_question("Flip a tile (F) or write a Note"+\
                                        " (N)? ",
                                        ['f','n','F','N'])

            # Asks the user which tile they want to play with
            print "Okay! Select a tile!"
            row = ask_question("Row: ",
                               ROWSCOLS,
                               "Sorry, what was that? We need a number" \
                               + " from 1 to 5. ")
            col = ask_question("Col: ",
                               ROWSCOLS,
                               "Sorry, what was that? We need a number" \
                               + " from 1 to 5. ")
            which_tile = (int(row) - 1)*5 + int(col)-1

            # If the user picked a tile that's already flipped
            if B.T[which_tile].up:
                print "Please pick a tile that isn't already flipped!"
            
            # If we're flipping the tile:
            elif tile_or_note in ['f','F']:
                B.score *= int(B.T[which_tile].flip())
                if B.score == 0:
                    GAME = "OVER"
                print B     # Show the user their changes

            # If we're making a note:
            else:
                newt = ask_question("Which numbers are you jotting down?"+\
                                    "\n(whenever you finish type: done) ",
                                    NOTES,
                                    "Err, please type in 0, 1, 2, 3,"+\
                                    " or done. ")
                while newt not in DONE:
                    B.T[which_tile].note(newt)
                    print B     # Show the user their changes
                    newt = ask_question("And? ", NOTES,
                                        "Err, please type in 0, 1, 2, 3,"+\
                                        " or done. ")

            # The user's made their change; let's loop!

        # GAME OVER!
        print "KABOOM! Better luck next time!"
        playing = ask_question("Ready to play again? (y/n)\n", YESNO)

    # The user chose to be done
    end = '\n'
    end *= 64
    end += "Thanks for playing!"
    print end
    time.sleep(4)
    # And the game is over!

if __name__ == "__main__": main()
