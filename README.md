##python-refresher

This project reads agricultural CO2 emissions data from a CSV file and
returns emissions values for a selected country.

##installation**

This project uses a mamba environment with Python and `pycodestyle`.

Create the environment with:

```bash
mamba env create -f environment.yml

## activate it 
mamba activate best_practice

##use

The program uses the `Agrofood_co2_emission.csv` file as input.

The command takes four arguments:

1. country
2. country column
3. fires column
4. file name

#example run script

```bash
python3 print_fires.py "United States of America" 0 3 Agrofood_co2_emission.csv

### running it 
Run ./run.sh and it'll print out the forest fire emissions numbers for the US. Agrofood_co2_emission.csv in the folder for this to work.
 
##examples with errors

./run.sh

This runs three examples:

- one working example
- one example with a missing file
- one example that cannot convert the selected values to integers

# testing updates

Added functions to calculate mean, median, and standard deviation.

Added unit tests for the utility functions using Python `unittest`.

Added functional tests for `print_fires.py` using `ssshtest`, including
tests for the different operations and exit codes

##Continuous Integration

Added a GitHub Actions workflow for continuous integration.

The workflow automatically runs:
- pycodestyle style checks
- unit tests
- functional tests

The workflow runs when any branch is pushed and when a pull request is made to master