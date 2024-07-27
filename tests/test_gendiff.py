import os

from gendiff import generate_diff


def test_generate_diff_json():
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


def test_generate_diff_yaml():
    output = generate_diff(
        os.getcwd() + '/tests/fixtures/files/file1.yml',
        os.getcwd() + '/tests/fixtures/files/file2.yml',
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
