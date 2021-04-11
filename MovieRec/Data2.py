import sys
import os
import tkinter as tk
from imdb import IMDb
from tkinter import *
from PIL import ImageTk



x = IMDb()

top = x.get_top250_movies()

for i in range(10):
    topMovie = x.get_movie(top[i].movieID)
    genres = topMovie.data['genres']
    for g in genres:
        print(type(g))