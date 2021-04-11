import sys
import os
import tkinter as tk
from imdb import IMDb
from tkinter import *
from PIL import ImageTk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 1500, height = 900)
canvas1.config(bg = 'black')

image = ImageTk.PhotoImage(file = "Images/Moviex.png")
canvas1.create_image(10, 10, image = image, anchor = NW)

canvas1.pack(padx = 10, pady = 10)

root.attributes("-fullscreen", True)



promptL = tk.Label(text = "Input favorite movie")
promptL.config(font = (5))
canvas1.create_window(680, 400, window = promptL)
entry1 = tk.Entry (root, width = 40)
entry1.config(font = (3))
canvas1.create_window(690, 430, window = entry1)

def quit():
    root.destroy()

button2 = tk.Button(text = 'Exit', command = quit, bg = 'white', fg = 'black')
button2.config(font = (10))
canvas1.create_window(1400, 40, window=button2)

x = IMDb()

def reStart ():
    python = sys.executable
    os.execl(python, python, * sys.argv)
 

def byGenre(movName):
    top = x.get_top250_movies()
    movie = x.get_movie(movName.movieID)
    mg = movie.data['genres']
    pr = []
    index = 0
    for i in range(30):
        topMovie = x.get_movie(top[i].movieID)
        g = topMovie.data['genres']
        for j in mg:
            if index == 10:    
                break
            for k in g:
                if j == k and index < 10:
                    pr.append(topMovie['title'])
                    index = index + 1
                    break
    canvas1.delete("all")
    button2 = tk.Button(text = 'Start Over', command = reStart, bg = 'light blue', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1140, 40, window=button2)
    button2 = tk.Button(text = 'Exit', command = quit, bg = 'light blue', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1000, 40, window=button2)
    ind = 1
    xCoord = 400
    yCoord = 100
    for i in pr:
        desButton = tk.Button(text = 'Recommendation {0}: {1}'.format(ind, i), command = lambda: getDetails(i), bg = 'white', fg = 'black')
        canvas1.create_window(xCoord, yCoord, window = desButton)
        yCoord = yCoord+75
        ind = ind+1
    

def byRating(mName):
    top = x.get_top250_movies()
    movie = x.get_movie(mName.movieID)
    mg = movie.data['rating']
    pr = []
    index = 0
    for i in range(30):
        topMovie = x.get_movie(top[i].movieID)
        g = topMovie.data['rating']
        if index == 10:
            break
        if mg <=g+1 and mg >= g-1 and index < 10:
            pr.append(topMovie['title'])
            index = index + 1
            break         
    canvas1.delete("all")
    button2 = tk.Button(text = 'Start Over', command = reStart, bg = 'light blue', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1140, 40, window=button2)
    button2 = tk.Button(text = 'Exit', command = quit, bg = 'light blue', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1000, 40, window=button2)
    

def byDir(mName):
    top = x.get_top250_movies()
    movie = x.get_movie(mName.movieID)
    mg = movie.data['director']
    pr = []
    index = 0
    for i in range(30):
        topMovie = x.get_movie(top[i].movieID)
        g = topMovie.data['director']
        for j in mg:
            if index == 10:    
                break
            for k in g:
                if j == k and index < 10:
                    pr.append(topMovie['title'])
                    index = index + 1
                    break         
    canvas1.delete("all")
    button2 = tk.Button(text = 'Start Over', command = reStart, bg = 'light blue', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1140, 40, window=button2)
    button2 = tk.Button(text = 'Exit', command = quit, bg = 'light blue', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1000, 40, window=button2)

def getRec(Namem):
    canvas1.delete("all")
    button2 = tk.Button(text = 'Start Over', command = reStart, bg = 'light blue', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1140, 40, window=button2)
    button2 = tk.Button(text = 'Exit', command = quit, bg = 'light blue', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1000, 40, window=button2)
    
    bGenre = tk.Button(text = 'Recommendations by Genre', command = lambda: byGenre(Namem), bg = 'white', fg = 'black')
    bGenre.config(font = (10))
    canvas1.create_window(200, 100, window = bGenre)
    
    bRate = tk.Button(text = 'Recommendations by Rating', command = lambda: byRating(Namem), bg = 'white', fg = 'black')
    bRate.config(font = (10))
    canvas1.create_window(200, 300, window = bRate)
    
    bDir = tk.Button(text = 'Recommendations by Director', command = lambda: byDir(Namem), bg = 'white', fg = 'black')
    bDir.config(font = (10))
    canvas1.create_window(200, 500, window = bDir)
    
    
   
def getDetails(mName):
    canvas1.delete("all")
    button2 = tk.Button(text = 'Start Over', command = reStart, bg = 'light blue', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1140, 40, window=button2)
    button2 = tk.Button(text = 'Exit', command = quit, bg = 'light blue', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1000, 40, window=button2)
    label1 = tk.Label(text="Details for '{}'".format(mName), bg = 'light blue', fg = 'black')
    label1.config(font = ("Courier", 15, 'bold'))   
    canvas1.create_window(400, 20, window=label1)
    name = mName
    id = name.movieID
    movie = x.get_movie(id)
    genre = movie.data['genres']
    year = movie.data['year']
    rating = movie.data['rating']
    directors = movie.data['director']
    
    label2 = tk.Label(text="Movie ID: {0}                        Movie Genres: {1}".format(id, genre), bg = 'light blue', fg = 'black')
    label2.config(font = ("Courier", 15, 'bold'))
    canvas1.create_window(600, 300, window=label2)
    label4 = tk.Label(text="Movie Year: {0}                         Movie Rating: {1}".format(year, rating), bg = 'light blue', fg = 'black')
    label4.config(font = ("Courier", 15, 'bold'))
    canvas1.create_window(450, 400, window=label4)
    label5 = tk.Label(text="Directors: {0}".format([director['name'] for director in directors[:1]]), bg = 'light blue', fg = 'black')
    label5.config(font = ("Courier", 15, 'bold'))
    canvas1.create_window(450, 500, window=label5)
    
    recButton = tk.Button(text = 'Get Recommendations', command = lambda: getRec(mName), bg = 'white', fg = 'black')
    recButton.config(font = (10))
    canvas1.create_window(500, 700, window = recButton)
def getEntry ():  
    canvas1.delete("all")
    canvas1.config(bg = 'light blue')

    button2 = tk.Button(text = 'Exit', command = quit, bg = 'white', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1000, 40, window=button2)
    button2 = tk.Button(text = 'Start Over', command = reStart, bg = 'white', fg = 'black')
    button2.config(font = (10))
    canvas1.create_window(1140, 40, window=button2)
    x1 = entry1.get()
    x2 = x.search_movie(x1) 
    y = 200
    z = 150
    index = 0
    for i in x2:
        index = index+1
    b = [0 for x in range(index)]
    tempI = 0
    for i in x2:
        b[tempI] = tk.Button(text=i, command = lambda i=i: getDetails(i), bg = 'white', fg = 'black')
        b[tempI].pack()
        tempI = tempI + 1
    for i in range(index):
        if z > 800:
            y = y+200
            z = 150
        if y > 1300:
            break
        canvas1.create_window(y, z, window = b[i])
        z = z+50
button1 = tk.Button(text='Enter', command=getEntry, bg = 'white', fg = 'black')
button1.config(font = (1))
canvas1.create_window(950, 430, window=button1)


root.mainloop()