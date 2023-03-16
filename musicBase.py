import sqlite3
from time import sleep
con = sqlite3.connect("musicbase.db") 

cursor = con.cursor() 

def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Songs (Artist TEXT, Name TEXT, Time FLOAT)")
    con.commit()
create_table()

# def add_data():
#     cursor.execute("INSERT INTO Songs Values('Metallica','Master of Puppets',8.36)")
#     con.commit()
# add_data()


information = """
----------------------------------------------------------------------------
Welcome to MusicBase project. Enjoy your song the way you wish...
----------------------------------------------------------------------------

1. IF YOU WANT TO CALCULATE THE PLAYLIST DURATION PRESS 1
2. ADD NEW SONG WITH 2
3. REMOVE A SONG WITH 3
4. PRESS 4 TO SEE THE CURRENT PLAYLIST
"""

def playlist():
    cursor.execute("SELECT * FROM Songs")
    playlist = cursor.fetchall()
    for i in playlist:
        a,b,c = i
        print(str(a),"-",str(b),"-",str(c))


def playlist_duration():
    total = 0
    cursor.execute("SELECT Time FROM Songs")
    duration = cursor.fetchall()
    for i in duration:
        total += i[0]
    print(f"\nPlaylist total duration = {total} minute\n")



def add_song(artist,name,time):
    cursor.execute("INSERT INTO Songs VALUES(?,?,?)",(artist,name,time))
    con.commit()



def remove_song(song_name):
    
    cursor.execute("DELETE FROM Songs where Name = ?",(song_name,))
    con.commit()
    
    
print(information)
while (True):
    choosen = int(input("SELECT A NUMBER BETWEEN 1-4(IF YOU CHOOSE SOMETHING DIFFERENT FROM THE BOUNDS, YOU CAN EXIT THE PROGRAM"))
    if choosen == 1:
        playlist_duration()
    elif choosen == 2:
        print()
        artist = input('Artist: ')
        print()
        name = input("Name: ")
        print()
        time = float(input("Time: "))
        print()
        add_song(artist,name,time)
        sleep(0.5)
        print("New song added smoothly.")
        print("Current Playlist:\n")
        playlist()

    elif choosen == 3:
        print()
        song_name = input("Name: ")
        remove_song(song_name)
        sleep(0.3)
        print("Successfully deleted.")
        print("Current Playlist:\n")
        playlist()
    elif choosen == 4:
        print()
        playlist()
        print()
        

    else:
        print("YOU LEAVING THE PROGRAM, TAKE CARE YOURSELF...")
        sleep(1)
        break



