def song_decoder(song):
    song = song.split('WUB') # returns ["a", ",", "b", ","]
    output_song = ""
    for i in song:
         if len(i) > 0:
            output_song +=(i) + " "
    return(output_song.strip())


print (song_decoder("AWUBBWUBC")) #"A B C","WUB should be replaced by 1 space")
print (song_decoder("AWUBWUBWUBBWUBWUBWUBC")) # "A B C" multiples WUB should be replaced by only 1 space #
print (song_decoder("WUBAWUBBWUBCWUB")) #"A B C","WUB should be replaced by 1 space")
