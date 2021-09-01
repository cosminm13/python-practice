import csv


def get_scores():
    """Print a list of scores from the CSV file."""
    with open('scores.csv', 'r') as file:
        reader = csv.reader(file)
        r = 0
        for row in reader:
            if r > 0:
                print(f'The word \'{row[0]}\' had {row[1]} wrong guesses. The game was {row[2]}.')
            r += 1


def add_score(word, wrong_guesses, outcome):
    """Add a score to the CSV file."""
    with open('scores.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([word, wrong_guesses, outcome])

# if __name__ == '__main__':
#     get_scores()
#     add_score('testword', 2, 'won')
#     get_scores()
