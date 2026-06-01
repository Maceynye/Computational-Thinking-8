from utils import *

# Section 1 - setup
# TODO - set a background using set_background()
set_background("sun")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
starfish = 0
bird = 0 
# OPTIONAL: use this invisible alien to say a message
m1 = create_sprite("alien", -200,200)
m1.hideturtle()



# Section 2 - controls
# TODO - define an action. ex: def my_control()
def get_starfish():
    global starfish 
    starfish += 1
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    create_sprite("star2" ,x,y) 
# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(get_starfish,"space")
# TODO - make a second control
def get_bird(): 
   global bird 
   bird += 1 
   x = random.randint(-200,200)
   y = random.randint(-200,200)
   create_sprite("bird" ,x,y)
window.onkeypress(get_bird,"B")





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here


    # OPTIONAL - use the message sprite to say a message
    # goul is to get as meant starfish as posible 
  m1.clear()
  m1.write("Hello")

  time.sleep(0.01)
  window.update( )