<h2 class="c-project-heading--task">Moving the obstacle</h2>

--- task ---
➡️ Move the obstacle down the screen
➡️ Make the obstacle wrap around to the top once it goes off the bottom of the screen
--- /task --- 
 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 19
line_highlights: 21-23,25-26
---

def draw_obstacles():
    fill(0, 255, 0) # Green
    ob_x = 200
    ob_y = 200 + frame_count
    ob_y %= screen_size
    rect(
        ob_x, # x
        ob_y, # y
        40,  # width
        40   # height
    )  

--- /code ---
</div>

**Test:** Run your code and you should see a coloured square. 

<div class="c-project-callout c-project-callout--tip">

### Tip

For a white background, choose `background(255, 255, 255)`.

</div>
