class Book:
    def __init__(self, author, title, price, book_id):
        self.author = author
        self.title = title
        self.price = price
        self.book_id = book_id

    # define the necessary method here
    def __repr__(self):
        return "{} by {}. ${}. [{}]".format(self.title, self.author, self.price, self.book_id)
    def __str__(self):
        return "{} by {}. ${}. [{}]".format(self.title, self.author, self.price, self.book_id)
