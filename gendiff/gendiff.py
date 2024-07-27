import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument(
        'first_file',
        type=str,
        help='The path to the first configuration file.'
    )
    parser.add_argument(
        'second_file',
        type=str,
        help='The path to the second configuration file.'
    )
    args = parser.parse_args()


if __name__ == '__main__':
    main()
