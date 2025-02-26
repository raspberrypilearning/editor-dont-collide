<h2 class="c-project-heading--task">Add a player</h2>

--- task ---
➡️ Create and call a function to draw the player.
--- /task --- 
 
Define a `draw_player` function. Inside, add an emoji and a pair of x, y coordinates to represent the player. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 7
line_highlights: 8-9
---
# Draw player function goes here
def draw_player():
    text('🤠', 200, 320)
  
--- /code ---
</div>


Call the `draw_player` function so that the player is drawn on the screen. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 21
line_highlights: 26
---

def draw():  
    # Put code to run every frame here 
    global safe
    safe = Color(200, 100, 0) 
    background(safe)
    draw_player()
  
--- /code ---
</div>

**Test:** Run your code and you should see the emoji appear near the bottom of the screen. 

<div class="c-project-callout c-project-callout--tip">

### Tip

You can choose any emoji to represent your player.

</div>
