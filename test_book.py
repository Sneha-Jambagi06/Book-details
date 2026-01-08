from book import book_info

def test_book_case1():
    result = book_info(101, "Geetanjali", "Rabindranath Tagore", 1986)
    expected = (
        "Book ID=101\n"
        "Book Title=Geetanjali\n"
        "Author Name=Rabindranath Tagore\n"
        "Year of Publication=1986"
    )
    assert result == expected






