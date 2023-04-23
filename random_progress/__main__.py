from random_progress.services import progress
from random_progress.sleep import item, random_numbers

if __name__ == "__main__":
    print(progress(time=item.sleep_time, number=random_numbers))
