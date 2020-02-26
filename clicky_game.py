import arcade
import math
WIDTH = 800
HEIGHT = 600

# Screen width and height

window = arcade.Window(WIDTH, HEIGHT, "My Arcade Game")
arcade.set_background_color(arcade.color.BLACK)

# Initialize your variables here
circle_x = 400
circle_y = 300
circle_radius = 50
count = 0
count1 = 0


@window.event("on_draw")
def game_loop():
    # import global variables here.
    global circle_x
    global circle_y
    global circle_radius
    global count
    global count1
    # update your variables here.
    text = 20
    # Draw things here.
    arcade.start_render()
    arcade.draw_circle_filled(circle_x, circle_y, circle_radius, arcade.color.RED)
    arcade.draw_text(('$' + str(count)), 25, 400, arcade.color.GREEN)
    arcade.draw_text('x  x', 640, 400, arcade.color.WHITE)
    arcade.draw_circle_outline(650, 400, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(650, 390, 5, arcade.color.WHITE,)
    arcade.draw_text(str(count1), 680, 400, arcade.color.WHITE)
    if(count == 0):
        arcade.draw_text("If you press this button, you will get $5000, but one person dies", 100, 400, arcade.color.WHITE)
    elif(count > 0 and count < 35000):
        arcade.draw_text("You're Terrible", 110, 400, arcade.color.WHITE, text)
    elif(count >= 35000):
        arcade.draw_parabola_filled(45, 100, 80, 40, arcade.color.CRIMSON)
        arcade.draw_parabola_filled(25, 120, 45, 20, arcade.color.CRIMSON)
        arcade.draw_parabola_filled(80, 120, 105, 20, arcade.color.CRIMSON)
        arcade.draw_circle_filled(100, 135, 10, arcade.color.GRAY)
        arcade.draw_circle_filled(35, 135, 10, arcade.color.GRAY)
        arcade.draw_text("Hey look, you have a little car now, hope you're proud of yourself", 110, 400, arcade.color.WHITE )
 

@window.event
def on_mouse_press(x, y, button, modifiers):
    global circle_radius
    global circle_x
    global circle_y
    global count
    global count1
    diameter = circle_radius * 2
    b = circle_y - y
    a = circle_x - x
    d = math.pow(a, 2) + math.pow(b, 2)
    c = math.sqrt(d)
    e = 0
    if(c <= circle_radius):
        count += 5000
        count1 += 1
        print(f"CLICKED AT {x}, {y}!")
  
            


arcade.run()