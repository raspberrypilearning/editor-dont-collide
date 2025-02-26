<h2 class="c-project-heading--task">Collisions</h2>

--- task ---
➡️ Change the emoji if the player hits an obstacle.
--- /task --- 
 
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

**Test:** Run your code and move the player. You should see the explosion emoji if your player touches an obstacle.

<div class="c-project-callout c-project-callout--tip">

### Tip

The collision will be based on the colour at one specific coordinate - x=`mouse_x`, y=320. You can improve the collision detection by changing the coordinate (for example `mouse_x + 20` is closer to the centre of the emoji), or by testing multiple coordinates for potential collisions. 

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

Make sure that in `draw()`, the line of code to `draw_obstacles()` is before `draw_player()`. If you check for collisions before drawing the obstacles in a frame, then there won’t be any obstacles to collide with!

</div>
