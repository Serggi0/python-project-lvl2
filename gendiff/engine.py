import argparse
import json


def create_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser


def get_diff(first_file, second_file):
    with open(first_file, 'r') as file1:
        with open(second_file, 'r') as file2:
            txt1 = json.load(file1)
            txt2 = json.load(file2)
            set_key_txt1 = set(txt1)
            set_key_txt2 = set(txt2)
            set_key_all = set_key_txt1 | set_key_txt2
            sort_key_all = list(set_key_all)
            sort_key_all.sort()
            result = []
            print(set_key_txt1)

            for i in sort_key_all:
                if i in set_key_txt1 and i in set_key_txt2:
                    if txt1[i] == txt2[i]:
                        result.append('  {}: {}'.format(i, txt1[i]))
                    else:
                        result.append('- {}: {}'.format(i, txt1[i]))
                        result.append('+ {}: {}'.format(i, txt2[i]))
                elif i in (set_key_txt1 - set_key_txt2):
                    result.append('- {}: {}'.format(i, txt1[i]))
                elif i in (set_key_txt2 - set_key_txt1):
                    result.append('+ {}: {}'.format(i, txt2[i]))
    return '{}\n{}\n{}'.format('{', '\n'.join(result), '}')


def gendiff():
    parser = create_parser()
    args = parser.parse_args()
    print(get_diff(args.first_file, args.second_file))
