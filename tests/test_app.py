from app import main


def test_main():
    expected = "done"
    actual = main()
    assert actual == expected
