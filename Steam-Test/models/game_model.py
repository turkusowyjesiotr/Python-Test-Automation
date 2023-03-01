class GameModel:
    def __init__(self, title, platforms, release_date, reviews, price):
        self.title = title
        self.platforms = platforms
        self.release_date = release_date
        self.reviews = reviews
        self.price = price

    def __repr__(self):
        return str([self.title, self.platforms, self.release_date, self.reviews, self.price])

    def __eq__(self, other):
        if not isinstance(other, GameModel):
            return False

        return [self.title, self.platforms, self.release_date, self.reviews, self.price] == \
               [other.title, other.platforms, other.release_date, other.reviews, other.price]
