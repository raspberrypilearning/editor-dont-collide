<h2 class="c-project-heading--task">Move the obstacle</h2>

--- task ---
➡️ Move the obstacle down the screen
--- /task --- 

Add two variables to keep track of the obstacle's x and y coordinates. Change the code to draw the emoji so that it uses these variables.  

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 13
line_highlights: 14-16
---

def draw_obstacles():
    obstacle_x = 200
    obstacle_y = 200 
    text('🌵', obstacle_x, obstacle_y) 

--- /code ---
</div>

Now, add `frame_count` to the obstacle's y (vertical) position. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 13
line_highlights: 15
---

def draw_obstacles():
    obstacle_x = 200
    obstacle_y = 200 + frame_count
    text('🌵', obstacle_x, obstacle_y) 

--- /code ---
</div>

**Test:** Run your code and the cactus emoji should move down the screen until it reaches the bottom.  

<div class="c-project-callout c-project-callout--tip">

### Tip

The variable `frame_count` automatically starts counting the frames when you click run. This is another useful variable provided by the p5 library, from the code `from p5 import *`. 

</div>
