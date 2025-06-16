from app.utils.file_parser import parse_file


def test_parse_txt():
    filename = "sample.txt"
    content = b"Hello, this is a test."
    result = parse_file(filename, content)
    assert result == [(1, "Hello, this is a test.")]


def test_parse_invalid_extension():
    filename = "sample.docx"
    content = b"Some content"
    result = parse_file(filename, content)
    assert result == []
