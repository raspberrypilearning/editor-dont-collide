## Collisions

➡️ Change the emoji if the player hits an obstacle.

## Step 1

Create a variable to store the colour the player emoji is currently touching. 

```python filename="main.py" line_numbers="true" line_number_start="8" line_highlights="9"
 
def draw_player():
    player_on = get(mouse_x, 320).hex
    text('🤠', mouse_x, 320)
  
```

## Step 2

If that colour is the safe colour, draw the player emoji. If it is not, draw an explosion emoji to show they have crashed. 

```python filename="main.py" line_numbers="true" line_number_start="8" line_highlights="10,12-13"
 
def draw_player():
    player_on = get(mouse_x, 320).hex
    if player_on == safe.hex: 
        text('🤠', mouse_x, 320)
    else:  
        text('💥', mouse_x, 320)
  
```

## Now run your code

> [!TIP]
>
> The collision will be based on the colour at one specific coordinate - x=`mouse_x`, y=320. You can improve the collision detection by changing the coordinate (for example `mouse_x + 20` is closer to the centre of the emoji), or by testing multiple coordinates for potential collisions.

> [!DEBUG]
>
> Make sure that in `draw()`, the line of code to `draw_obstacles()` is before `draw_player()`. If you check for collisions before drawing the obstacles in a frame, then there won’t be any obstacles to collide with!

Move the player and check that an explosion emoji appears if your player touches an obstacle.
