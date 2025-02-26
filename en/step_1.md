<h2 class="c-project-heading--task">Choose a background colour</h2>

--- task ---
➡️ Create a variable to store a background colour.

➡️ Set the background to this colour.
--- /task --- 
 
Create a variable called `safe` to store the background colour.

In the game, the player is safe if they are touching the background colour. 

<div class="c-project-code">
--- code ---
---
language: python
line_numbers: true
line_number_start: 20
line_highlights: 22-24
---
 
def draw():   
    # Put code to run every frame here
    global safe
    safe = Color(200, 100, 0) 
    background(safe) 
  
--- /code ---
</div>

**Test:** Run your code and you should see a coloured square. 

<div class="c-project-callout c-project-callout--tip">

### Tip

The colour is three numbers - the amount of red, green and blue. You can use a [colour picker](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} to help you find the values for a colour you want to use. 

</div>
