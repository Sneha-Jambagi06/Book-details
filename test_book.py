from book import book_info
def test_book_info(bookID,bookTitle,authorName,yearOfPublication):
    expected_output = (
        "Book ID=101\n"
        "Book Title=Geetaanjali\n"
        "Author Name=Rabindranath Tagore\n"
        "Year of Publication=1986"
    )
    assert (101,"Geetaanajali","Rabindranath Tagore",1986) == expected_output







