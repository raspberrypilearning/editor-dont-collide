<h2 class="c-project-heading--task">Create an obstacle</h2>

--- task ---
➡️ Create and call a function to draw one obstacle.
--- /task --- 

Define a `draw_obstacles` function. Inside, create a rectangle to represent **one** obstacle. 


<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 18
line_highlights: 19-26
---
 
# Draw obstacles function goes here
def draw_obstacles():   
    fill(0, 255, 0) # Green
    rect(
        100, # x
        100, # y
        40,  # width
        40   # height
    ) 
  
--- /code ---
</div>


Call the `draw_obstacles` function so that the obstacle is drawn on the screen. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 34
line_highlights: 39
---

def draw():   
    global safe
    safe = Color(200, 100, 0) 
    background(safe)
    draw_obstacles()
    draw_player()
  
--- /code ---
</div>

**Test:** Run your code and you should see a coloured square as well as your player circle. 

<div class="c-project-callout c-project-callout--tip">

### Tip

Make sure you put the call to `draw_obstacles` before the call to `draw_player` so that the obstacles are drawn before the player.

</div>
