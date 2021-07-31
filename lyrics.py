import lyricsgenius
geniustoken = "Akf1AHXpbqaKHSQ06hesk8q1urZkHWJ334bzLr1SwZ1BBPSMGUm3NcbcbDR8ye7Z"
genius = lyricsgenius.Genius(geniustoken)
songname = input("")
def lysearch(songname):
    import lyricsgenius
    geniustoken = "Akf1AHXpbqaKHSQ06hesk8q1urZkHWJ334bzLr1SwZ1BBPSMGUm3NcbcbDR8ye7Z"
    genius = lyricsgenius.Genius(geniustoken)
    songname = songname.split("/")
    if len(songname) == 1:
        song = genius.search_song(songname[0])  
    elif len(songname) > 1:
        song = genius.search_song(songname[0], songname[1])
    ly = song.lyrics
    return ly

#print(song.lyrics)