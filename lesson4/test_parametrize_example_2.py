

@pytest.mark.parametrize(
    "number", [
        "One",
        "Two",
        "Three",
        "Four",
        "Five"
    ]
)
def test_numbers(number):
    print(number)
