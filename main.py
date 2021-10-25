from lab_python_op.Square import Square
from lab_python_op.Circle import Circle
from lab_python_op.Rectangle import Rectangle

def main():
    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()
wait = input("PRESS ENTER TO CONTINUE.")