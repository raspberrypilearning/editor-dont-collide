## Move the obstacle

➡️ Move the obstacle down the screen

## Step 1

Add two variables to keep track of the obstacle's x and y coordinates. Update the code to draw the emoji so that it uses these variables.  

```python filename="main.py" line_numbers="true" line_number_start="13" line_highlights="14-16"

def draw_obstacles():
    obstacle_x = 200
    obstacle_y = 200 
    text('🌵', obstacle_x, obstacle_y) 

```

## Step 2

Now, add `frame_count` to the obstacle's y (vertical) position. 

```python filename="main.py" line_numbers="true" line_number_start="13" line_highlights="15"

def draw_obstacles():
    obstacle_x = 200
    obstacle_y = 200 + frame_count
    text('🌵', obstacle_x, obstacle_y) 

```

## Now run your code

The cactus emoji should move down the screen until it reaches the bottom.

> [!TIP]
>
> The variable `frame_count` automatically starts counting the frames when you click run. This is another useful variable provided by the p5 library, from the code `from p5 import *`.