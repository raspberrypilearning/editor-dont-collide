<h2 class="c-project-heading--task">Add a player</h2>

--- task ---
➡️ Create and call a function to draw the player.
--- /task --- 
 
Define a `draw_player` function. Inside, create a circle to represent the player. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 7
line_highlights: 8-15
---
# Draw player function goes here
def draw_player():   
    fill(255, 0, 0) # Red
    ellipse(
        200, # x
        320, # y
        70,  # width
        70   # height
    ) 
  
--- /code ---
</div>


Call the `draw_player` function so that the player is drawn on the screen. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 16
line_highlights: 20
---

def draw():   
    global safe
    safe = Color(200, 100, 0) 
    background(safe)
    draw_player()
  
--- /code ---
</div>

**Test:** Run your code and you should see a coloured circle appear near the bottom of the screen. 

<div class="c-project-callout c-project-callout--tip">

### Tip

You may not want your player to look like a circle, but you can make the code work with just a circle for now, and then update the way the player looks later. This is called **iterating**.

</div>
