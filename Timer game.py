# Timer Game
import time


input("3s test. Hit enter to start: ")
start = time.time()

input("Hit enter to stop: ")
end = time.time()

target_time = 3
difference = target_time - (end - start)
print(f" {round(end - start, 3)} seconds")

print(f'you were {difference} seconds off)')







