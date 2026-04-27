<h2 class="c-project-heading--task">Collisions</h2>

➡️ Change the emoji if the player hits an obstacle.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

Create a variable to store the colour the player emoji is currently touching. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 8
line_highlights: 9
---
 
def draw_player():
    player_on = get(mouse_x, 320).hex
    text('🤠', mouse_x, 320)
  
--- /code ---
</div>

If that colour is the safe colour, draw the player emoji. If it is not, draw an explosion emoji to show they have crashed. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 8
line_highlights: 10, 12-13
---
 
def draw_player():
    player_on = get(mouse_x, 320).hex
    if player_on == safe.hex: 
        text('🤠', mouse_x, 320)
    else:  
        text('💥', mouse_x, 320)
  
--- /code ---
</div>

## Now run your code

### Tip

<div class="c-project-callout c-project-callout--tip">

The collision will be based on the colour at one specific coordinate - x=`mouse_x`, y=320. You can improve the collision detection by changing the coordinate (for example `mouse_x + 20` is closer to the centre of the emoji), or by testing multiple coordinates for potential collisions. 

</div>

### Debugging

<div class="c-project-callout c-project-callout--debug">

Make sure that in `draw()`, the line of code to `draw_obstacles()` is before `draw_player()`. If you check for collisions before drawing the obstacles in a frame, then there won’t be any obstacles to collide with!

</div>

Move the player and check that an explosion emoji appears if your player touches an obstacle.
