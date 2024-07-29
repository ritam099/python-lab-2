class LibraryManager:
    def __init__(self):
        #Initialize the library with an empty collection.
        self.books = {}

    def add_book(self, title, author, publisher, volume, year, isbn):
       
        if isbn in self.books:
            raise ValueError(f"Book with ISBN {isbn} already exists.")
        
        self.books[isbn] = {
            'title': title,
            'author': author,
            'publisher': publisher,
            'volume': volume,
            'year': year,
            'isbn': isbn
        }

    def remove_book(self, isbn):
       
        if isbn not in self.books:
            raise ValueError(f"Book with ISBN {isbn} not found.")
        
        del self.books[isbn]

    def retrieve_book(self, isbn):
       
        return self.books.get(isbn, None)

    def search_books(self, title=None, author=None):
        
        results = []
        for book in self.books.values():
            if (title and title.lower() in book['title'].lower()) or \
               (author and author.lower() in book['author'].lower()):
                results.append(book)
        return results

    def list_books(self):
       
        return self.books

    def update_book(self, isbn, title=None, author=None, publisher=None, volume=None, year=None):
        
        if isbn not in self.books:
            raise ValueError(f"Book with ISBN {isbn} not found.")
        
        book = self.books[isbn]
        
        if title is not None:
            book['title'] = title
        if author is not None:
            book['author'] = author
        if publisher is not None:
            book['publisher'] = publisher
        if volume is not None:
            book['volume'] = volume
        if year is not None:
            book['year'] = year

    def check_availability(self, isbn):
        
        return isbn in self.books

# Example usage
if __name__ == "__main__":
    library = LibraryManager()
    
    # Sample data for 25 books
    books_data = [
        {"title": "Modern Operating Systems", "author": "Andrew S. Tanenbaum", "publisher": "Prentice Hall", "volume": "3rd Edition", "year": 2021, "isbn": "9780133591620"},
        {"title": "Introduction to Machine Learning", "author": "Ethem Alpaydin", "publisher": "MIT Press", "volume": "4th Edition", "year": 2022, "isbn": "9780262043791"},
        {"title": "Data Structures and Algorithms in Python", "author": "Michael T. Goodrich", "publisher": "Wiley", "volume": "2nd Edition", "year": 2020, "isbn": "9781118290279"},
        {"title": "Artificial Intelligence: A Modern Approach", "author": "Stuart Russell", "publisher": "Prentice Hall", "volume": "4th Edition", "year": 2023, "isbn": "9780137903955"},
        {"title": "Operating System Concepts", "author": "Silberschatz Henry", "publisher": "Wiley", "volume": "10th Edition", "year": 2021, "isbn": "9781119456339"},
        {"title": "Deep Learning", "author": "Ian Goodfellow", "publisher": "MIT Press", "volume": "1st Edition", "year": 2021, "isbn": "9780262035611"},
        {"title": "Computer Vision: Algorithms and Applications", "author": "Richard Szeliski", "publisher": "Springer", "volume": "1st Edition", "year": 2021, "isbn": "9781848829346"},
        {"title": "Introduction to the Theory of Computation", "author": "Michael Sipser", "publisher": "Cengage Learning", "volume": "3rd Edition", "year": 2022, "isbn": "9781133187790"},
        {"title": "Pattern Recognition and Machine Learning", "author": "Christopher M. Bishop", "publisher": "Springer", "volume": "1st Edition", "year": 2021, "isbn": "9780387310732"},
        {"title": "Data Science from Scratch", "author": "Joel Grus", "publisher": "O'Reilly Media", "volume": "2nd Edition", "year": 2022, "isbn": "9781492041139"},
        {"title": "Fundamentals of Database Systems", "author": "Ramez Elmasri", "publisher": "Pearson", "volume": "7th Edition", "year": 2022, "isbn": "9780133970777"},
        {"title": "Introduction to Algorithms", "author": "Thomas H. Cormen", "publisher": "MIT Press", "volume": "4th Edition", "year": 2022, "isbn": "9780262033846"},
        {"title": "Computer Networks", "author": "Andrew S. Tanenbaum", "publisher": "Prentice Hall", "volume": "6th Edition", "year": 2022, "isbn": "9780132126953"},
        {"title": "Database Management Systems", "author": "Raghu Ramakrishnan", "publisher": "McGraw-Hill", "volume": "3rd Edition", "year": 2023, "isbn": "9780073523323"},
        {"title": "Introduction to Quantum Computing", "author": "Michael A. Nielsen", "publisher": "Cambridge University Press", "volume": "1st Edition", "year": 2023, "isbn": "9780521635035"},
        {"title": "Python Machine Learning", "author": "Sebastian Raschka", "publisher": "Packt Publishing", "volume": "3rd Edition", "year": 2023, "isbn": "9781804633571"},
        {"title": "Principles of Compiler Design", "author": "Aho, Sethi, Ullman", "publisher": "Addison-Wesley", "volume": "1st Edition", "year": 2022, "isbn": "9780321486813"},
        {"title": "Introduction to Data Mining", "author": "Pang-Ning Tan", "publisher": "Pearson", "volume": "2nd Edition", "year": 2021, "isbn": "9780133128901"},
        {"title": "Computer Architecture: A Quantitative Approach", "author": "John L. Hennessy", "publisher": "Morgan Kaufmann", "volume": "6th Edition", "year": 2022, "isbn": "9780128182519"},
        {"title": "Algorithms Unlocked", "author": "Thomas H. Cormen", "publisher": "MIT Press", "volume": "1st Edition", "year": 2022, "isbn": "9780262518818"},
        {"title": "Deep Reinforcement Learning Hands-On", "author": "Maxim Lapan", "publisher": "Packt Publishing", "volume": "2nd Edition", "year": 2023, "isbn": "9781801074954"},
        {"title": "Computer Vision: A Modern Approach", "author": "David L. Poole", "publisher": "Cambridge University Press", "volume": "2nd Edition", "year": 2021, "isbn": "9780521515511"},
        {"title": "Python Data Science Handbook", "author": "Jake VanderPlas", "publisher": "O'Reilly Media", "volume": "1st Edition", "year": 2022, "isbn": "9781491912058"},
        {"title": "Natural Language Processing with Python", "author": "Steven Bird", "publisher": "O'Reilly Media", "volume": "1st Edition", "year": 2022, "isbn": "9780596516499"},
        {"title": "Machine Learning Yearning", "author": "Andrew Ng", "publisher": "Self-Published", "volume": "1st Edition", "year": 2023, "isbn": "9780999664468"},
        {"title": "Programming Collective Intelligence", "author": "Toby Segaran", "publisher": "O'Reilly Media", "volume": "1st Edition", "year": 2022, "isbn": "9780596529321"},
        {"title": "Introduction to Neural Networks for Java", "author": "Jeff Heaton", "publisher": "Heaton Research", "volume": "1st Edition", "year": 2023, "isbn": "9780975569328"},
        {"title": "Practical Statistics for Data Scientists", "author": "Peter Bruce", "publisher": "O'Reilly Media", "volume": "2nd Edition", "year": 2022, "isbn": "9781492072934"},
        {"title": "Data Structures and Algorithms in Java", "author": "Robert Lafore", "publisher": "Sams Publishing", "volume": "2nd Edition", "year": 2022, "isbn": "9780672324530"}
    ]
    
    # Adding sample books to the library
    for book in books_data:
        library.add_book(
            title=book['title'],
            author=book['author'],
            publisher=book['publisher'],
            volume=book['volume'],
            year=book['year'],
            isbn=book['isbn']
        )