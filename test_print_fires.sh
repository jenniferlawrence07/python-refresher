#!/bin/bash

test -e ssshtest || curl -s -o ssshtest https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run raw_values python3 print_fires.py "Testland" 0 3 test_data.csv
assert_in_stdout "[2, 4, 6]"
assert_exit_code 0

run mean_test python3 print_fires.py "Testland" 0 3 test_data.csv \
    --operation mean
assert_in_stdout "4"
assert_exit_code 0

run median_test python3 print_fires.py "Testland" 0 3 test_data.csv \
    --operation median
assert_in_stdout "4"
assert_exit_code 0

run std_test python3 print_fires.py "Testland" 0 3 test_data.csv \
    --operation std
assert_in_stdout "1.632"
assert_exit_code 0

run bad_operation python3 print_fires.py "Testland" 0 3 test_data.csv \
    --operation bad
assert_exit_code 2
