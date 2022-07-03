from lyricsgenius import Genius #https://github.com/johnwmillr/LyricsGenius

#Passing API key and setup parameters for Genius Search
api_key = "***REMOVED***"
genius = Genius(api_key, skip_non_songs=True, excluded_terms=["(Remix)"], remove_section_headers=True)

#Prompt user on which artist and number of songs they want to grab lyrics for
artist_input = input("Enter artist name to retreive song lyrics: ")
all_music = input("Do you want to pull all the aritsts lyrics (y/n): ")
#Fetch song lyrics using Genius API and assign them to Variable songs 
if all_music == "y":
    artist = genius.search_artist(artist_input)
elif all_music == "n":
    num_songs = int(input("Number of songs: "))
    artist = genius.search_artist(artist_input, max_songs = num_songs, sort = "popularity")

songs = artist.songs

#Prompt user if they want to write the requested lyrics to file, if yes prompt user to input filename
write_input = input("Write lyrics to file (y/n): ")
if write_input == "y":
    file_name = input("Specify filename: ")
    try:
        file = open(f"C:/rafatDev/deepMumble/Lyrics/{file_name}.txt", "x", encoding="utf-8")
    except:
        print(f"Could not save the following file: {file_name}.txt")
else:
    pass

#Create list of song lyrics    
lyrics_list = [song.lyrics for song in songs]

#If user requested to write lyrics to file, write the lyrics and seperate them using the seperator below. Else, print the song lyrics for each song
if write_input == "y":
    file.write("\n \n".join(lyrics_list))      
else:
    for song in lyrics_list:
        print(song)

if write_input == "y" and all_music == "y":
    print(f"All song lyrics for {artist_input} have been written to {file_name}.txt") 
elif write_input == "y" and all_music == "n":
    print(f"{num_songs} song lyrics for {artist_input} have been written to {file_name}.txt") 

