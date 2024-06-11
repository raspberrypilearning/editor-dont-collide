<h2 class="c-project-heading--task">Random obstacle position</h2>

--- task ---
➡️ Generate a random position for the obstacle 
--- /task --- 
 
Generate a pair of random x, y coordinates for the obstacle to start at. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 14-16
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
