import lyricsgenius
token = "Akf1AHXpbqaKHSQ06hesk8q1urZkHWJ334bzLr1SwZ1BBPSMGUm3NcbcbDR8ye7Z"
genius = lyricsgenius.Genius(token)
song = genius.search_song("born this way")
string = song.lyrics
#print(string)
#string = input()
split_string = []
split_string = string.split("\n")
split_string = list(filter(None, split_string))
melded_string = (split_string[0])
x = 1
while True:
    try:
        nxtln = int(x + 1)
        a = melded_string
        b = split_string[x]
        stringmeldlength = int(len(a)) + int(len(b))
        print(stringmeldlength)
        #input()
        if int(stringmeldlength) > 2048:
            print("=== STRING SPLIT 2048 ===")
            pt1 = melded_string
            melded_string = (b)
            x = x + 1
        else:
            melded_string = (f"{melded_string}\n{b}")
            x = x + 1
    except:
        pt2 = melded_string
        break
input("Done")
print(melded_string)

openfile = open(f"part1.txt", "w")
openfile.write(pt1)
openfile.close()
openfile = open(f"part2.txt", "w")
openfile.write(pt2)
openfile.close()