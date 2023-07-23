#!/usr/bin/python3
"""Log parsing."""
from contextlib import suppress
from sys import stdin


StatusCodes = dict[int, int]
FileSize = list[int]


def _print_stats(file_size: FileSize, status_codes: StatusCodes) -> None:
    """Print stats."""
    print('File size: {}'.format(file_size[0]))
    for key in sorted(status_codes.keys()):
        if key in status_codes:
            print('{}: {}'.format(key, status_codes[key]))


def _parse_line(
    line: str,
    status_codes: StatusCodes,
    file_size: FileSize
        ) -> tuple[StatusCodes, FileSize]:
    """Parse line."""
    with suppress(BaseException):
        line = line[:-1]
        word = line.split(' ')
        file_size[0] += int(word[-1])
        status_code = int(word[-2])
        if status_code in status_codes:
            status_codes[status_code] += 1
    return status_codes, file_size


def main() -> None:
    """Main function."""

    file_size = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}
    line_number = 1
    try:
        for line in stdin:
            status_codes, file_size = _parse_line(
                line, status_codes, file_size
                )
            if line_number % 10 == 0:
                _print_stats(file_size, status_codes)
            line_number += 1
    except KeyboardInterrupt:
        _print_stats(file_size, status_codes)
        raise
    _print_stats(file_size, status_codes)


if __name__ == '__main__':
    main()
