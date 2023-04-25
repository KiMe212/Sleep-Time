from random_progress.services import progress
from random_progress.sleep import app_config, random_numbers

if __name__ == "__main__":
    print(progress(time=app_config.sleep_time, number=random_numbers))
