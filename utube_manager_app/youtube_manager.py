import sqlite3 

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEy,
        name TEXT NOT NULL
        time TEXT NOT NULL
    )               
''')

def list_videos():
    pass

def add_video(name, time):
    pass

def main():
    while True:
        print("\n Youtube Manager App")
        print("1. List all videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("Enter your choice: ")
        
        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video duration: ")
                add_video(name, time)
            case '3':

if __name__ == '__main__':
    main()