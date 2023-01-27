import webbrowser
import os

filename = 'file:///'+os.getcwd()+'/' + 'book/index.html'
webbrowser.open_new_tab(filename)