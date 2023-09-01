from lib.album import Album
"""
Constructs with id, title, release_year and artist_id
"""

def test_construct_with_fields():
    album = Album(1, "Dark Side", 1995, 2)
    assert album.id == 1
    assert album.title == "Dark Side"
    assert album.release_year == 1995 
    assert album.artist_id == 2