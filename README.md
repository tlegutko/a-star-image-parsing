# a-star-tests

Tests for benchmarking a-star algorithm implementation in various languages. For testing there's problem where we want to drive several cars from destination to goal.

## Movement rules
At each moment each car has 4 numbers describing it's state: X, Y, V<sub>x</sub>, V<sub>y</sub>.  
So there are always 9 possible state changes:  

|               | Y, V<sub>y</sub>                      | Y, V<sub>y</sub> + 1                | Y, V<sub>y</sub> - 1           |
| ------------- | -------------              |:-------------            | -----              |
| **X, V<sub>x</sub>**     | X+V<sub>x</sub>, Y+V<sub>y</sub>, V<sub>x</sub>, V<sub>y</sub>            | X+V<sub>x</sub>, Y+V<sub>y</sub>+1, V<sub>x</sub>, V<sub>y</sub>+1        | X+V<sub>x</sub>, Y+V<sub>y</sub>-1, V<sub>x</sub>, V<sub>y</sub>-1   |
| **X, V<sub>x</sub> + 1** | X+V<sub>x</sub>+1, Y+V<sub>y</sub>, V<sub>x</sub>+1, V<sub>y</sub>        | X+V<sub>x</sub>+1, Y+V<sub>y</sub>+1, V<sub>x</sub>+1, V<sub>y</sub>+1    | X+V<sub>x</sub>+1, Y+V<sub>y</sub>-1, V<sub>x</sub>+1, V<sub>y</sub>-1   |
| **X, V<sub>x</sub> - 1** | X+V<sub>x</sub>-1, Y+V<sub>y</sub>, V<sub>x</sub>-1, V<sub>y</sub>        | X+V<sub>x</sub>-1, Y+V<sub>y</sub>+1, V<sub>x</sub>-1, V<sub>y</sub>+1    | X+V<sub>x</sub>-1, Y+V<sub>y</sub>-1, V<sub>x</sub>-1, V<sub>y</sub>-1 |
At each time step all vehicles must make one of moves above.  
Two cars cannot be in the same position on map at given time.  
Car can evade obstacle if it moves fast enough (it can 'jump' over it).  
Once car reaches destination, it's moved to position (-1, -1, -1, -1) to mark it's completed state and prevent collisions with other cars trying to reach te same goal.  
Game is solved when all vehicles park at end destination (cars need to have V<sub>x</sub> = V<sub>y</sub> = 0).  
Multiple cars cannot arrive at destination at the same time (that would be a collision).  
Upper left corner on map has  V<sub>x</sub>, V<sub>y</sub> = (0,0)

## Input format
In first line there are two integers: `number_of_columns` and `number_of_rows`, separated by space.  
In next `number_of_rows` lines there are `number_of_columns` integers separated by space, describing fields as follows:
  - `0` means regular field that can be traversed
  - `1` means map border / obstacle
  - `2` means starting field
  - `3` means ending field  
  
There can be multiple starting and ending points.

Example:  
4 5  
1 1 1 1  
1 2 0 1  
1 1 0 1  
1 0 3 1  
1 1 1 1  

## Output format
In first line there should two integers, separated by space: `number_of_steps`, `number_of_vehicles`.  
In next `(number_of_steps + 1) * number_of_vehicles` lines there should be four integers separated by space, describing X, Y, V<sub>x</sub>, V<sub>y</sub> in all moments in time.

Example:  
2 1  
1 1 0 0  
2 2 1 1  
2 3 0 0  

> FIXME: above example is wrong, create correct one.

## Checking output
`test_solution.py` script is meant to check correctness of the solution (in terms of state transitions legality) which should be provided in above format.
Usage:
```
test_solution.py [<input file>]
```
If `<input file>` is not provided, solution will be read from standard input.

## Adding new input files:
1. Create file in `.bmp` format, consisting of following RGB colors:
    - `#FFFFFF` for regular field that can be traversed
    - `#000000` for map border / obstacle
    - `#00FF00` for starting field
    - `#FF0000` for ending field
2. Put file in `/img_in` directory.
3. Run `python img_to_text.py`. This command converts all `.bmp` images in `/img_in` directory to text format in `/text_in` directory.
4. Resulting text in format specified above can be found in `/text_in` directory with `.in` extension instead of `.bmp`.  
   So file `/img_in/test100.bmp` will be converted to `/text_in/test100.in`.
5. Once test works, commit it so others can also use it!

