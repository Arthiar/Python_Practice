from datetime import datetime
import time

def task():
    with open("datetime.txt", "a") as file:   # better use .txt extension
        file.write(f"Script ran at: {datetime.now()}\n")

while True:   # run forever
    task()
    time.sleep(10)
