<h2 class="c-project-heading--task">Make the player follow the mouse</h2>

➡️ Make the player follow the mouse to move across the screen

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

To make the player follow the mouse as it moves from side to side, change the player's x position to `mouse_x`.

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 7
line_highlights: 9
---
# Draw player function goes here
def draw_player():
    text('🤠', mouse_x, 320)
  
--- /code ---
</div>

## Now run your code

Check that the player moves left and right when you move the mouse.

### Tip

<div class="c-project-callout c-project-callout--tip">

The position of the mouse is automatically stored in `mouse_x` by the p5 library, which is imported with code `from p5 import *`.  

</div>

Confirm the observable result.
