<h2 class="c-project-heading--task">Create an obstacle</h2>

--- task ---
➡️ Create and call a function to draw one obstacle.
--- /task --- 

Define a `draw_obstacles` function to draw a cactus emoji 🌵.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 12
line_highlights: 13-14
---
 
# Draw obstacles function goes here
def draw_obstacles():
    text('🌵', 200, 200)
  
--- /code ---
</div>


Call the `draw_obstacles` function so that the cactus is drawn on the screen. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 22
line_highlights: 27
---

def draw():   
    # Put code to run every frame here
    global safe
    safe = Color(200, 100, 0) 
    background(safe)
    draw_obstacles()
    draw_player()
  
--- /code ---
</div>

**Test:** Run your code and you should see a cactus as well as your player. 


