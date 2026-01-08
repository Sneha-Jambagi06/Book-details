def book_info(bookID,bookTitle,authorName,yearOfPublication):
  return(f"Book Id:{bookID}\n"
         f"Book Title:{bookTitle}\n"
         f"Author Name:{authorName}\n"
         f"Year of Publication:{yearOfPublication}\n"
)
  
if __name__=="__main__":
      bookID=101
      bookTitle="Geetaanjali"
      authorName="Rabindranath Tagore"
      yearOfPublication=1986
      print("Book Details:")
      print(book_info(bookID,bookTitle,authorName,yearOfPublication))
      