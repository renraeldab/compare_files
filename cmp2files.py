import difflib
import sys
import argparse


def read_file(file):
    try:
        with open(file, 'r') as f:
            return f.read().splitlines()
    except IOError:
        print('cannot read {}'.format(file))
        sys.exit()


def compare_files(file1, file2, result_path=None):
    if result_path is None:
        result_path = './'
    text1 = read_file(file1)
    text2 = read_file(file2)
    diff = difflib.HtmlDiff()
    result = diff.make_file(text1, text2, file1, file2)
    result_file = result_path + 'result.html'
    try:
        with open(result_file, 'w') as f:
            f.write(result)
            print('result:'+result_file)
    except IOError:
        print('failed to save result')


if __name__ == "__main__":
    # -f1 file1 -f2 file2
    parser = argparse.ArgumentParser(description="input two files to compare")
    parser.add_argument('-f1', action='store', type=str, help='file1', required=True)
    parser.add_argument('-f2', action='store', type=str, help='file2', required=True)
    parser.add_argument('-p', action='store', type=str, help='result path', required=False)
    # retrieve all input arguments
    given_args = parser.parse_args()
    file1 = given_args.f1
    file2 = given_args.f2
    result_path = given_args.p
    compare_files(file1, file2, result_path)
