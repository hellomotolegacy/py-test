'''       Working with Python, once again..            '''

#Used for line breaks, makes things a LOT more optimized..
def endl(a):
  print("\n" * a)
  
#'Press enter to continue' prompt..
def pause():
  enter = input("Press ENTER to continue")
  
#Clear the screen
def cls():
  print("\n" * 100)

#Enter your name and such..
def introduction():
  cls()
  print("You awaken in a room, a dark room. There is a monitor")
  print("sitting on the edge of a black desk.")
  endl(1)
  print("You approach the desk, you now notice that alongside")
  print("the monitor there is a QWERTY keyboard.")
  endl(1)
  print("The monitor reads \"What is your name?\"")
  endl(1)
  name = input("Answer the machine: ")
  cls()
  print("There is a loud buzzing as a sheet of paper is printed")
  print("out, black like the room. You wonder what else is there.")
  pause()
  cls()
  print("The paper finishes.")
  endl(1)
  print("It reads, \"Hello,",name,"!\"")
  pause()
  
  
#First thing called, this is the beginning.
def warning():
  print("Warning!")
  endl(1)
  print("This game does not have save points! You can NOT")
  print("go back, at ALL. Made a mistake? Too bad..")
  endl(1)
  pause()


#I'll admit, it's nice to not have to create a main function, I can 
#just place everything here.
warning()
introduction()
