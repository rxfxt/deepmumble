from lyricsgenius import Genius

# Set API key and setup parameters for Genius Search
api_key = "***REMOVED***"
genius = Genius(api_key, skip_non_songs=True, excluded_terms=["(Remix)"], remove_section_headers=True)

# Prompt user on which artist and number of songs they want to grab lyrics for
artist_input = input("Enter artist name to retreive song lyrics: ")
all_music = input("Do you want to pull all the aritsts lyrics (y/n): ")

# Fetch song lyrics using Genius API and assign them to the variable songs 
if all_music == "y":
    artist = genius.search_artist(artist_input)

elif all_music == "n":
    max_songs = int(input("Number of songs: "))
    artist = genius.search_artist(artist_input, max_songs = max_songs, sort = "popularity")

songs = artist.songs

# Prompt user to set filename to write the requested lyrics to file
file_name = input("Specify filename: ")
try:
    file = open(f"./Lyrics/{file_name}.txt", "x", encoding="utf-8")
except:
    print(f"Could not save the following file: {file_name}.txt")
else:
    pass

# Create list of song lyrics    
lyrics_list = [song.lyrics for song in songs]
num_songs = len(lyrics_list)

# If user requested to write lyrics to file, write the lyrics and seperate them using the seperator below. Else, print the song lyrics for each song
file.write("\n \n".join(lyrics_list))      

# Print summary of the lyrics fetched and filename
if all_music == "y":
    print(f"All song lyrics ({num_songs} songs) for {artist_input} have been written to {file_name}.txt") 
elif all_music == "n":
    print(f"{num_songs} song lyrics for {artist_input} have been written to {file_name}.txt") 

