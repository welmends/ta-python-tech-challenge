from app.src.data_capture import DataCapture
from timeit import default_timer as timer
from datetime import timedelta
import random

NUMBER_OF_SAMPLES = 100000000

capture = DataCapture()

print("Random samples: ", end="")
start = timer()
for i in range(NUMBER_OF_SAMPLES):
    capture.add(int(random.uniform(0, 999)))
end = timer()
print(timedelta(seconds=end - start))

print("Build Stats:    ", end="")
start = timer()
stats = capture.build_stats()
end = timer()
print(timedelta(seconds=end - start))

print("Less stat:      ", end="")
start = timer()
stats.less(4)
end = timer()
print(timedelta(seconds=end - start))

print("Between stat:   ", end="")
start = timer()
stats.between(3, 100)
end = timer()
print(timedelta(seconds=end - start))

print("Greater stat:   ", end="")
start = timer()
stats.greater(677)
end = timer()
print(timedelta(seconds=end - start))
