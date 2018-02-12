import os
import argparse


class Teleop(object):

    def __init__(self):
        pass


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='Input', required=True)
    parser.add_argument('-o', '--output_dir', help='Output', required=True)
    parser.add_argument('-F', '--flag', help='Flag', action='store_true')
    args = parser.parse_args()

    return args.input, args.output_dir, args.flag


if __name__ == '__main__':
    input, output_dir, flag = parse_arguments()
