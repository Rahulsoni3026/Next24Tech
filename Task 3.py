
"""
Creating GUI to Extract Lyrics from Songs Using Python

(This GUI works for some songs only. 
For example it provides the lyrics for english songs like: 
lauv - I like me better ,
justin bieber - intentions , 
selena gomez - who says ,
Artist: "Ed Sheeran", Song: "Shape of You"
Artist: "Ariana Grande", Song: "7 rings"
Artist: "Billie Eilish", Song: "bad guy"
Artist: "The Weeknd", Song: "Blinding Lights"
Artist: "Dua Lipa", Song: "Don't Start Now"..)

"""
import tkinter as tk
from tkinter import messagebox
import requests

def get_lyrics():
    artist = artist_entry.get()
    song = song_entry.get()
    if artist and song:
        try:
            url = f"https://api.lyrics.ovh/v1/{artist}/{song}"
            response = requests.get(url)
            data = response.json()
            lyrics = data.get("lyrics", "Lyrics not found.")
            lyrics_text.delete(1.0, tk.END)
            lyrics_text.insert(tk.END, lyrics)
        except Exception as e:
            messagebox.showerror("Error", f"Could not fetch lyrics: {str(e)}")
    else:
        messagebox.showwarning("Input Error", "Please enter both artist and song name.")

# Create the main window
root = tk.Tk()
root.title("Lyrics Extractor")

# Set background color
root.configure(bg='green')

# Artist label and entry
tk.Label(root, text="Artist", bg='green', font=('Times New Roman', 14)).grid(row=0, column=0, padx=10, pady=10)
artist_entry = tk.Entry(root, font=('Times New Roman', 12))
artist_entry.grid(row=0, column=1, padx=10, pady=10)

# Song label and entry
tk.Label(root, text="Song", bg='green', font=('Times New Roman', 14)).grid(row=1, column=0, padx=10, pady=10)
song_entry = tk.Entry(root, font=('Times New Roman', 12))
song_entry.grid(row=1, column=1, padx=10, pady=10)

get_lyrics_button = tk.Button(root, text="Get Lyrics", command=get_lyrics, bg='#C1FFC1', fg='black', font=('Times New Roman', 12, 'bold'))
get_lyrics_button.grid(row=2, column=0, columnspan=2, pady=10)

# Lyrics text box
lyrics_text = tk.Text(root, wrap='word', height=15, width=50, bg='#FFB6C1')
lyrics_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()