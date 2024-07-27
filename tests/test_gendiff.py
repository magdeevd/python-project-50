import os

from gendiff import generate_diff


def test_generate_diff():
    output = generate_diff(
        os.getcwd() + '/tests/fixtures/files/file1.json',
        os.getcwd() + '/tests/fixtures/files/file2.json'
    )

    expected_output = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""

    assert output == expected_output
