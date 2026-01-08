from book import book_info
def test_book_info(bookID,bookTitle,authorName,yearOfPublication):
    expected_output = (
        "bookID=101\n"
        "bookTitle=Geetaanjali\n"
        "authorName=Rabindranath Tagore\n"
        "yearofPublication=1986"
    )
    assert (101,"Geetaanajali","Rabindranath Tagore",1986) == expected_output
     
