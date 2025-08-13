# playing with apis

from museam.myfunctions import get_artworks, get_artists

def main():
    artist = input("Artist: ")
    artists = get_artists(query=artist, limit=3) 

    if not artists:
        print("No artists found.")
    else:
        print("Artists:")
        for a in artists:
            print(f" - {a}")  

if __name__ == "__main__":
    main()