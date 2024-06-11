<h2 class="c-project-heading--task">Make the player follow the mouse</h2>

--- task ---
➡️ Make the player follow the mouse to move across the screen
--- /task --- 

The player will stay at the same y (vertical) position, but the player's x position will follow the mouse using `mouse_x`.

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
        320, # y
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
