class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
    def __str__(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0

watch = Stopwatch()
for i in range(3600):
    pass
    #print(watch)
    #watch.tick()
