<h2 class="c-project-heading--task">Wrap around</h2>

--- task ---
➡️ When the obstacle goes off the bottom of the screen, make it reappear at the top
--- /task --- 
 
Currently, the obstacle disappears off the bottom of the screen, because its `obstacle_y` position becomes larger than the screen size.

Use the modulo (%) operator to divide the y position by the screen size and give you the **remainder**. This make the obstacle wrap around!

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 13
line_highlights: 16
---
 
def draw_obstacles():
    obstacle_x = 200
    obstacle_y = 200 + frame_count
    obstacle_y = obstacle_y % screen_size
    text('🌵', obstacle_x, obstacle_y) 
  
--- /code ---
</div>

**Test:** Run your code and you should see the obstacle reach the bottom of the screen and then restart from the top.

<div class="c-project-callout c-project-callout--tip">

### Tip

The modulo operator gives you the **remainder** of a whole number division. So, if the y position of the cactus becomes 401, and the screen size is 400, the calculation is `401 % 400`. The number 400 goes into 401 once, and the remainder is `1`, so the cactus reappears at y coordinate 1 - neat!  

</div>
