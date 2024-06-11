<h2 class="c-project-heading--task">Make the player follow the mouse</h2>

--- task ---
➡️ Make the player follow the mouse to move across the screen
--- /task --- 

Add a variable called `player_y` and use it to record the player's position on the y (horizontal) axis.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 7
line_highlights: 9
---
# Draw player function goes here
def draw_player():   
    player_y = 320
    fill(255, 0, 0) # Red
  
--- /code ---
</div>

Set the player's y position to `player_y` and set the player's x position to `mouse_x`.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 11-12
---
ellipse(
        mouse_x, # x
        player_y, # y
        70,  # width
        70   # height
    ) 
  
--- /code ---
</div>


**Test:** Run your code and check that the player circle moves left and right when you move the mouse. 

<div class="c-project-callout c-project-callout--tip">

### Tip

The variable `mouse_x` was defined automatically by p5 by the code `from p5 import *`.  

</div>
