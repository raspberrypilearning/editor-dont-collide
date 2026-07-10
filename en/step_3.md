## Make the player follow the mouse

➡️ Make the player follow the mouse to move across the screen

To make the player follow the mouse as it moves from side to side, change the player's x position to `mouse_x`.

```python filename="main.py" line_numbers="true" line_number_start="7" line_highlights="9"
# Draw player function goes here
def draw_player():
    text('🤠', mouse_x, 320)
  
```

## Now run your code

> [!TIP]
>
> The position of the mouse is automatically stored in `mouse_x` by the p5 library, which is imported with code `from p5 import *`.

Run your code and check that the player moves left and right when you move the mouse.
