from breaking_bad.lib import get_quote


def test_get_quote():
    response = get_quote()
    assert type(response) == str