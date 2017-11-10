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
  print("k")
  
  
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
