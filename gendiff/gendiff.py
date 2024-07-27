import argparse
import json


def _compare_jsons(json1, json2):
    all_keys = sorted(set(json1.keys()).union(set(json2.keys())))

    diff = []

    for key in all_keys:
        match (key in json1, key in json2):
            case (True, True) if json1[key] != json2[key]:
                diff.append({
                    'type': 'changed',
                    'key': key,
                    'old_value': json1[key],
                    'new_value': json2[key]
                })
            case (True, True) if json1[key] == json2[key]:
                diff.append({
                    'type': 'not changed',
                    'key': key,
                    'value': json1[key]
                })
            case (True, False):
                diff.append({
                    'type': 'removed',
                    'key': key,
                    'value': json1[key]
                })
            case (False, True):
                diff.append({
                    'type': 'added',
                    'key': key,
                    'value': json2[key]
                })

    return diff


def _format_diff(diffs):
    lines = []

    for diff in diffs:
        match diff['type']:
            case 'changed':
                lines.append(f"  - {diff['key']}: {diff['old_value']}")
                lines.append(f"  + {diff['key']}: {diff['new_value']}")
            case 'removed':
                lines.append(f"  - {diff['key']}: {diff['value']}")
            case 'added':
                lines.append(f"  + {diff['key']}: {diff['value']}")
            case 'not changed':
                lines.append(f"    {diff['key']}: {diff['value']}")

    return "\n".join(["{", *lines, "}"])


def generate_diff(file_path1: str, file_path2: str) -> str:
    with open(file_path1, 'r') as f1, open(file_path2, 'r') as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    diff = _compare_jsons(data1, data2)
    formated_diff = _format_diff(diff)

    return formated_diff


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
    parser.add_argument(
        '-f', '--format',
        type=str,
        help='set format of output'
    )

    args = parser.parse_args()

    diff_output = generate_diff(args.first_file, args.second_file)

    print(diff_output)


if __name__ == '__main__':
    main()

__all__ = ['generate_diff']
