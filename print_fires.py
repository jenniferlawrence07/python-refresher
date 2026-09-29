import argparse
from my_utils import find_mean
from my_utils import find_median
from my_utils import find_std
from my_utils import get_column

parser = argparse.ArgumentParser()

parser.add_argument("country")
parser.add_argument("country_column", type=int)
parser.add_argument("fires_column", type=int)
parser.add_argument("file_name")
parser.add_argument(
    "--operation",
    choices=["mean", "median", "std"]
)

args = parser.parse_args()

fires = get_column(
    args.file_name,
    args.country_column,
    args.country,
    result_column=args.fires_column)

if args.operation == "mean":
    print(find_mean(fires))
elif args.operation == "median":
    print(find_median(fires))
elif args.operation == "std":
    print(find_std(fires))
else:
    print(fires)
