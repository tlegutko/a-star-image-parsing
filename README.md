# a-star-tests

Tests for benchmarking a-star algorithm implementation in various languages.

## Input format
In first line there are two integers: `number_of_columns` and `number_of_rows`, separated by space.  
In next `number_of_rows` there are `number_of_columns` integers describing fields as follows:
  - `0` means regular field that can be traversed
  - `1` means map border / obstacle
  - `2` means starting field
  - `3` means ending field

Example:  
4 4  
1 1 1 1  
1 2 0 1  
1 1 0 1  
1 0 3 1  
1 1 1 1  

## Adding new input files:
1. Create file in `.bmp` format, consisting of following RGB colors:
    - `#FFFFFF` for regular field that can be traversed
    - `#000000` for map border / obstacle
    - `#00FF00` for starting field
    - `#FF0000` for ending field
2. Put file in `/img_in` directory.
3. Run `python img_to_text.py`
4. Resulting text in format specified above can be found in `/text_in` directory with `.in` extension instead of `.bmp`.  
   So file `/img_in/test100.bmp` will be converted to `/text_in/test100.in`.
5. Once test works, commit it so others can use it!

## Output format
TODO

