# futval4.py
# upgraded version

from graphics import *

def createLabeledWindow():
   
    window = GraphWin("Investment Growth Chart", 500, 500)
    window.setBackground("white")
    window.setCoords(-1.75,-2000, 11.5, 10400)
    Text(Point(5, 8000), 'Investment Growth Chart').draw(window)
    Text(Point(-1, 0), '0.0K').draw(window)
    Text(Point(-1, 2500), '2.5K').draw(window)
    Text(Point(-1, 5000), '5.0K').draw(window)
    Text(Point(-1, 7500), '7.5K').draw(window)
    Text(Point(-1, 10000), '10.0K').draw(window)
    Text(Point(0.5, -500), 'y0').draw(window)
    Text(Point(2.5, -500), 'y2').draw(window)
    Text(Point(4.5, -500), 'y4').draw(window)
    Text(Point(6.5, -500), 'y6').draw(window)
    Text(Point(8.5, -500), 'y8').draw(window)
    Text(Point(10.5, -500), 'y10').draw(window)
    return window

def drawBar(window, year, height):
    # draw a bar in window starting at year with given height
    bar = Rectangle(Point(year, 0), Point(year+1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)

def main():
    print("This program plots the growth of a 10-year investment.")

    principal = eval(input("Please enter the initial principal: "))
    apr = eval(input("Please enter the annualized interest rate: "))

    win = createLabeledWindow()
    drawBar(win, 0, principal)
    for year in range(1, 11):
        principal *= (1 + apr)
        drawBar(win, year, principal)

    input("Press <Enter> to quit.")
    win.close()
    
main()


