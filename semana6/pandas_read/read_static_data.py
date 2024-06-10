from modules import PandasReader
import argparse

def main(path:str, delimiter:str):

    reader = PandasReader(path, delimiter)
    data = reader.get_data_from_file()

    print(data.head())



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Insert file to check or the url")

    parser.add_argument(
        "--path", type=str, help="path to run"
    )

    parser.add_argument(
        "--delimiter", type=str , nargs="?", const=",", help="delimiter , by default ',' "
    )

    args = parser.parse_args()

    main(args.path,args.delimiter)