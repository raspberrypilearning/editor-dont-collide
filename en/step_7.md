<h2 class="c-project-heading--task">Random obstacle position</h2>

--- task ---
➡️ Generate a random position for the obstacle 
--- /task --- 
 
Add a line of code for a random **seed**. A seed lets you generate the same random numbers in each frame.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 14
---
 
# Draw obstacles function goes here
def draw_obstacles():
    seed(1234)
    obstacle_x = 200
    obstacle_y = 200 + frame_count

--- /code ---
</div>

Update the code so that the x, y coordinates for the obstacle are generated randomly.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 15-16
---
 
# Draw obstacles function goes here
def draw_obstacles():
    seed(1234)
    obstacle_x = randint(0, screen_size)
    obstacle_y = randint(0, screen_size) + frame_count

--- /code ---
</div>

**Test:** Run your code and you should see the cactus appear at a random position. Change the `1234` value inside the seed to another number and it will appear somewhere else. 

<div class="c-project-callout c-project-callout--tip">

### Tip
This code uses `randint()` to choose a random obstacle position. Calling the random `seed()` function first means that you will always get the same random numbers. This means that the obstacles won't jump around every frame.

</div>
