from book import book_info
def test_book_info():
    expected_output = (
        "Book ID=101\n"
        "Book Title=Geetaanjali\n"
        "Author Name=Rabindranath Tagore\n"
        "Year of Publication=1986"
    )
    result = book_info(
        101,
        "Geetaanjali",
        "Rabindranath Tagore",
        1986
    )
    assert result == expected_output
