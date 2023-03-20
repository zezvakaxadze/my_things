""" The number of bacteria doubles every hour.
The program shows how many bacteria we
will have at the end of the experiment."""

bacteria = int(input("write the initial number of bacteria: "))

time_of_experiment = int(input("write Duration of the experiment in hours: "))

for i in range(time_of_experiment):
    bacteria *= 2

print(f"the end of the experiment: {bacteria} bacteria")
