from argparse import ArgumentParser
from pprint import pprint
from sys import argv

from ... import get_features, get_headers, get_row_count, load_dataset


def parse_args(*args):
    args = ArgumentParser(
        prog=argv[0],
        description=f"{argv[0]} will load a hugging face dataset and then print info on it",
    )
    args.add_argument("name", help="The name of the dataset")
    args.add_argument(
        "-e",
        "--headers",
        action="store_true",
        default=False,
        help="Print datasets column names",
    )
    args.add_argument(
        "-f",
        "--features",
        action="store_true",
        default=False,
        help="Print datasets features",
    )
    args.add_argument(
        "-l",
        "--len",
        action="store_true",
        default=False,
        help="Print the number of rows",
    )
    return args


def hfinfo(*args):
    a = parse_args(*args)
    hf = load_dataset(args.name)
    if a.headers:
        pprint(get_headers(hf))
    if a.features:
        pprint(get_features(hf))
    if a.len:
        pprint(get_row_count(hf))
    return 0


def main():
    hfinfo(*argv)
