<h2 class="c-project-heading--task">Lots of obstacles</h2>

➡️ Use a loop to generate multiple obstacles.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

Add a loop and indent the code to draw an obstacle. The loop will run this code multiple times. Change the number inside `range()` to control how many obstacles are created.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 13
line_highlights: 15-19
---
 
def draw_obstacles():
    seed(1234)
    for i in range(8):
        obstacle_x = randint(0, screen_size)
        obstacle_y = randint(0, screen_size) + frame_count
        obstacle_y = obstacle_y % screen_size
        text('🌵', obstacle_x, obstacle_y)
  
--- /code ---
</div>

## Now run your code

You should see several obstacles.

### Debugging

<div class="c-project-callout c-project-callout--debug">

Make sure that the code for the seed is outside of the loop, otherwise all of your obstacles will be generated on top of each other!

</div>

Confirm the observable result.
