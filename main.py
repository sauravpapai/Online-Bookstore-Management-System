import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('bookstore.db')
c = conn.cursor()

# Function to display all books
def display_books():
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    for book in books:
        print(book)

# Function to add a new book
def add_book(title, author, price):
    c.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", (title, author, price))
    conn.commit()
    print("Book added successfully!")

# Function to place an order
def place_order(book_id, quantity):
    c.execute("SELECT * FROM books WHERE id=?", (book_id,))
    book = c.fetchone()
    if book:
        total_price = book[3] * quantity
        print(f"Order placed successfully! Total Price: {total_price}")
    else:
        print("Book not found!")

# Main function
if __name__ == "__main__":
    # Create books table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS books
                 (id INTEGER PRIMARY KEY, title TEXT, author TEXT, price REAL)''')

    # Sample data
    c.execute("INSERT INTO books (title, author, price) VALUES ('Book1', 'Author1', 10.99)")
    c.execute("INSERT INTO books (title, author, price) VALUES ('Book2', 'Author2', 15.99)")
    conn.commit()

    # Example usage
    display_books()
    add_book("Book3", "Author3", 20.99)
    place_order(1, 2)

    # Close the connection
    conn.close()
