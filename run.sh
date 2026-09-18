#!/bin/bash

python3 print_fires.py "United States of America" 0 3 Agrofood_co2_emission.csv

python3 print_fires.py "United States of America" 0 3 wrong_file.csv

python3 print_fires.py "United States of America" 0 0 Agrofood_co2_emission.csv
