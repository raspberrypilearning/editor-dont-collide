<h2 class="c-project-heading--task">Move the obstacle</h2>

➡️ Move the obstacle down the screen

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

Add two variables to keep track of the obstacle's x and y coordinates. Update the code to draw the emoji so that it uses these variables.  

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

## Now run your code

The cactus emoji should move down the screen until it reaches the bottom.

### Tip

<div class="c-project-callout c-project-callout--tip">

The variable `frame_count` automatically starts counting the frames when you click run. This is another useful variable provided by the p5 library, from the code `from p5 import *`. 

</div>

Confirm the observable result.
