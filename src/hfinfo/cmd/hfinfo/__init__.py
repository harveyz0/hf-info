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
    args.add_argument(
        "-a",
        "--all",
        action="store_true",
        default=False,
        help="Print all the info we can get",
    )
    args.add_argument(
        "-d",
        "--load-from-disk",
        action="store_true",
        default=False,
        help="Use Hugging Faces load_from_disk method",
    )
    return args.parse_args()


def hfinfo(*args):
    a = parse_args(*args)
    hf = load_dataset(a.name, a.load_from_disk)
    if a.headers or a.all:
        pprint(get_headers(hf))
    if a.features or a.all:
        pprint(get_features(hf))
    if a.len or a.all:
        pprint(get_row_count(hf))
    return 0


def main():
    hfinfo(*argv)
