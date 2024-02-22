def make_album(artist_name, album_title, number_of_songs=None):
    """Dictionary about a music album"""
    album = {'name': artist_name, 'title': album_title, 'song': number_of_songs}
    return album

while True:
    print("Create an album:")
    print("(enter 'q' at any time to exit.)")
    artist_name = input("Enter your favorite artist: ")
    if artist_name == 'q':
        break
    album_title = input("Enter you favortie album: ")
    if album_title == 'q':
        break
    number_of_songs = input("How many songs are on the album?: ")

    artist = make_album(artist_name, album_title, number_of_songs)
    print(artist)