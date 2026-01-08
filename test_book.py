from book import book_info
def test_book_info():
    bookID = 101
    bookTitle = "Geetaanjali"
    authorName = "Rabindranath Tagore"
    yearOfPublication = 1986

    assert bookID == 101
    assert bookTitle == "Geetaanjali"
    assert authorName == "Rabindranath Tagore"
    assert yearOfPublication == 1986

     
