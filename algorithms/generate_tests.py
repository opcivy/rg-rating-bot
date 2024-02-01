import csv
import string

class Ratings:
    title = ""
    score = 0
    chartLevel = 0.0
    rating = 0.0
    lamp = 0

    def __init__(self, title,  chartLevel,score, rating, lamp):
        self.title = title
        self.score = score
        self.chartLevel = chartLevel
        self.rating = rating
        self.lamp = lamp


def generate_test(games: [str]):
    f = open("tests.py", "w")
    f.write(f"import unittest\nimport ratings\n")
    for game_name in games:
        list = []        

        with open(f'{game_name}.csv', mode='r') as infile:
            reader = csv.reader(infile)
            for row in reader:
                print(game_name)
                print(row[0])
                print(row[1])
                print(row[2])
                print(row[3])
                print(row[4])
                list.append(Ratings(row[0],row[1],row[2], row[3], row[4]))

        f.write(f"\nclass Test{game_name}(unittest.TestCase):\n\n")
        for song in list:
            title = song.title.translate(str.maketrans('', '', string.punctuation)).replace(' ', '_')
            f.write("    def test"+f"_{title}"+f"(self):\n        self.assertEqual(ratings.{game_name}({song.score},{song.chartLevel},{song.lamp}),{song.rating})\n\n")

        list.clear()
        
    f.write("if __name__ == '__main__':\n    unittest.main()")
    


generate_test(["chunithm", "gitadora"])