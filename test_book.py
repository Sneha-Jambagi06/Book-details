def test_book_case1():
    result = book_info(101, "Geetanjali", "Rabindranath Tagore", 1986)
    expected = (
        "Book ID=101\n"
        "Book Title=Geetanjali\n"
        "Author Name=Rabindranath Tagore\n"
        "Year of Publication=1986"
    )
    assert result == expected


def test_book_case2():
    result = book_info(102, "Wings of Fire", "A. P. J. Abdul Kalam", 1999)
    expected = (
        "Book ID=102\n"
        "Book Title=Wings of Fire\n"
        "Author Name=A. P. J. Abdul Kalam\n"
        "Year of Publication=1999"
    )
    assert result == expected


def test_book_case3():
    result = book_info(103, "The Alchemist", "Paulo Coelho", 1988)
    expected = (
        "Book ID=103\n"
        "Book Title=The Alchemist\n"
        "Author Name=Paulo Coelho\n"
        "Year of Publication=1988"
    )
    assert result == expected
