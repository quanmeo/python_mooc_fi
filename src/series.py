class Series:
    def __init__(self, title: str, num_of_seasons: int, genres: list):
        self.title = title
        self.num_of_seasons = num_of_seasons
        self.genres = genres
        self.rates = []

    def rates_num(self):
        return len(self.rates)

    def average(self):
        size = self.rates_num()
        if size == 0:
            return 0
        else:
            return sum(self.rates) / size

    def get_rating(self):
        size = self.rates_num()
        if size == 0:
            return "no ratings"
        else:
            total = sum(self.rates)
            return f"{num} ratings, average {self.average():.1f} points"

    def __str__(self):
        return (
            f"{self.title} ({self.num_of_seasons} seasons)\n"
            f"genres: {', '.join(self.genres)}\n"
            f"{self.get_rating()}\n"
        )

    def rate(self, rating: int):
        if rating < 0 or rating > 5:
            raise ValueError('The rating value must between 0 and 5')
        self.rates.append(rating)

def minimum_grade(rating: float, series_list: list):
    series = [seri for seri in series_list if seri.average() >= rating]

    return series

def includes_genre(genre: str, series_list: list):
    series = [seri for seri in series_list if genre in seri.genres]

    return series

s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

print("a minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)

print("genre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.title)
