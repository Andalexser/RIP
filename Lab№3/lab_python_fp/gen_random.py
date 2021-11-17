import random as rand

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield rand.randint(begin, end)

if __name__ == "__main__":
    gen_random(10, 0, 100)
    wait = input("PRESS ENTER TO CONTINUE.")
