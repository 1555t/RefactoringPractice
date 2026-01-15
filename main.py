from helpers import *
from utils import thing
import stuff
import temp

students = {}

def run():
    print("STARTING PROGRAM")

    data = open("data.txt", "r").read().split("\n")

    for line in data:
        if line != "":
            parts = line.split(",")
            name = parts[0]
            subject = parts[1]
            score = int(parts[2])

            if name not in students:
                students[name] = []

            students[name].append(score)

    for s in students:
        avg = sum(students[s]) / len(students[s])
        students[s] = avg

    thing(students)

    if temp.doThing(students):
        stuff.print_students(students)

    print("DONE")

run()
