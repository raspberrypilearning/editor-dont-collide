## Create an obstacle

➡️ Create and call a function to draw one obstacle.

## Step 1

Define a `draw_obstacles` function to draw a cactus emoji 🌵.

```python filename="main.py" line_numbers="true" line_number_start="12" line_highlights="13-14"
 
# Draw obstacles function goes here
def draw_obstacles():
    text('🌵', 200, 200)
  
```

## Step 2

Call the `draw_obstacles` function so that the cactus is drawn on the screen. 

```python filename="main.py" line_numbers="true" line_number_start="22" line_highlights="27"

def draw():   
    # Put code to run every frame here
    global safe
    safe = Color(200, 100, 0) 
    background(safe)
    draw_obstacles()
    draw_player()
  
```

## Now run your code

You should see a cactus as well as your player.