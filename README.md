# python-refresher

## Assignment 1: Git and Python

For this assignment I finished writing get_column() in my_utils.py. It reads
through a CSV file line by line, and for any row where a certain column matches
a value I'm searching for, it grabs the value from another column I want and
adds it to a list. At the end it returns that list.

### What I did
- Wrote the get_column() function so it actually works instead of just
  returning None.
- Gave result_column a default value of 1, so you don't have to pass it every
  time if you just want that column.
- Fixed print_fires.py so it actually calls get_column() correctly and prints
  out forest fire emissions for the United States using the data in
  Agrofood_co2_emission.csv.
- Added run.sh so you can just run ./run.sh instead of typing out the python
  command every time.

### Running it 
Run ./run.sh and it'll print out the forest fire emissions numbers for the US. Agrofood_co2_emission.csv in the folder for this to work.
