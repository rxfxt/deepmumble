from lyricsgenius import Genius
import config

# Function to initialize lyrics file 
def write_lyrics(file_name):
    while True:
        try:
            file = open(f"./Lyrics/{file_name}.txt", "x", encoding="utf-8")
            return file, file_name
        except:
            print("Could not save to the requested file name, please try again...")
            file_name = input("Specify filename to write lyrics: ")

# Set API key and setup parameters for Genius Search
api_key = config.api_key
genius = Genius(api_key, skip_non_songs=True, excluded_terms=["(Remix)"], remove_section_headers=True)

# Prompt user on which artist, number of songs they want to grab lyrics
artist_input = input("Enter artist name to retreive song lyrics: ")
all_music = input("Do you want to pull all the aritsts lyrics (y/n): ")
file_name = input("Specify filename to write lyrics: ")

# Initialize lyrics file
file, file_name = write_lyrics(file_name)

# Fetch song lyrics using Genius API and assign them to the variable songs 
if all_music == "y":
    artist = genius.search_artist(artist_input)

elif all_music == "n":
    max_songs = int(input("Number of songs: "))
    artist = genius.search_artist(artist_input, max_songs = max_songs, sort = "popularity")

songs = artist.songs

# Create list of song lyrics    
lyrics_list = [song.lyrics for song in songs]
num_songs = len(lyrics_list)

# Write lyrics to file, write the lyrics and seperate them using the seperator below
file.write("\n \n".join(lyrics_list))      

# Print summary of the lyrics fetched and filename
if all_music == "y":
    print(f"All song lyrics ({num_songs} songs) for {artist_input} have been written to {file_name}.txt") 
elif all_music == "n":
    print(f"{num_songs} song lyrics for {artist_input} have been written to {file_name}.txt") 
