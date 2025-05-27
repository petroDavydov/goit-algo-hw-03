import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_curve(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 3) # Додано size / 3
    t.pendown()
#  додано код використовуючи базовий сценарій конспекту 
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.exitonclick()  # use hint
# JОбираємо рівень рекурсії
order = int(input("Рівень рекурсії (не ставте більше 5): "))
draw_koch_curve(order)