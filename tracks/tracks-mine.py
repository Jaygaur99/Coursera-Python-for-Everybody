import xml.etree.ElementTree as ET
import sqlite3 as S

conn = S.connect('sqltracks.sqlite')
con = conn.cursor()

con.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')
fname = input ('ENter file Name: ')
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Length of dict',len(all))
def lookup(d,key):
    found = False
    for child in d:
        if found:return child.text
        if child.tag == 'key' and child.text == key: found =True
    return None

for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue
    name = lookup(entry,'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    genre = lookup(entry , 'Genre')

    if name is None or artist is None or album is None or genre is None :
        continue
    print(name, artist, album, count, rating, length,genre)

    con.execute(''' INSERT OR IGNORE INTO Artist(name) VALUES(?)
    ''',(artist,))
    con.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
    artist_id = con.fetchone()[0]

    con.execute(''' INSERT OR IGNORE INTO Album(title, artist_id)
    VALUES(?,?)     ''',(album,artist_id))
    con.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = con.fetchone()[0]

    con.execute('''INSERT OR IGNORE INTO Genre(name) VALUES(?)''',(genre,))
    con.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
    genre_id = con.fetchone()[0]

    con.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count, genre_id)
        VALUES ( ?, ?, ?, ?, ? ,?)''',
        ( name, album_id, length, rating, count,genre_id ) )

    conn.commit()
