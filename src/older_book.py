from book import Book

def older_book(book1: Book, book2: Book):
    if book1.year == book2.year:
        print(f"{book1.name} and {book2.name} were published in {book1.year}")
    else:
        a = book1 if book1.year < book2.year else book2
        print(f"{a.name} is older, it was published in {a.year}")

if __name__ == '__main__':
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    older_book(python, everest)
    older_book(python, norma)
