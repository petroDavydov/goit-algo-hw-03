import turtle


def koch_curve(t, order, size):
    if order == 0:
        try:
            t.forward(size)
        except turtle.Terminator:
            print("Was closed before drawing completed.")
            return
    else:
        for angle in [60, -120, 60, 0]:
            try:
                koch_curve(t, order - 1, size / 3)
                t.left(angle)
            except turtle.Terminator:
                print("Window was closed before drawing completed.")
                return


def draw_koch_curve(order, size=300):
    try:
        window = turtle.Screen()
        window.bgcolor("white")

        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(-size / 2, size / 3)
        t.pendown()

        for _ in range(3):
            koch_curve(t, order, size)
            t.right(120)

        window.exitonclick()  # Закриває вікно по кліку
    except turtle.Terminator:
        print("Window was closed before drawing completed.")
    except Exception as error:
        print(f"Eroror occured: {error}")

# Рекурсія і помилки


def main():
    while True:
        try:
            user_level = int(input("Enter level of recursion (0 or higher): "))
            if user_level >= 0:
                break
            else:
                print("Enter a non-negative integer.")
        except ValueError:
            print("Enter a valid integer.")

    try:
        draw_koch_curve(order=user_level)
    except turtle.Terminator:
        print("!!! Window was closed before drawing completed !!!")


if __name__ == "__main__":
    main()


# використовував знання інших розробників для розуміння помилок, та старався трохи розібратися в їх причинах.
# Не знаю чи вийшло зробити все правильно, але намагався.