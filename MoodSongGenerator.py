# the library we're using doesn't work on Ed, please use any other IDE to run our code
import lyricsgenius

# finds statistics of given song
class SongStats:

    # initialize different mood dictionaries
    def __init__(self):
        self.sad_songs = {}
        self.happy_songs = {}
        self.unorganized_songs = {}

    # if debugging code, prints number of sad/happy lyrics, otherwise
    # adds given song into appropriate mood dictionary
    def add(self, song_name, artist_name, num_happy, num_sad):
        debug = False
        if debug:
            print (" number of sad lyrics: " + str(num_sad))
            print (" number of happy lyrics: " + str(num_happy))
        
        if (num_happy > num_sad): # more happy words
            self.happy_songs[song_name] = artist_name
        if (num_sad > num_happy):
            self.sad_songs[song_name] = artist_name
        if (num_sad == num_happy):
            self.unorganized_songs[song_name] = artist_name
            
    # prints given song name and artist under the mood it belongs to 
    # printed text is properly formatted
    def print(self):
        print("\nAnalysis of songs by mood ...")
        print ("\n sad songs: ")
        for i, (song, artist) in enumerate(self.sad_songs.items()):
            print("\t%2s. %-40s by %s" % (i+1, song, artist))
            
        print ("\n happy songs: ")
        for i, (song, artist) in enumerate(self.happy_songs.items()):
            print("\t%2s. %-40s by %s" % (i+1, song, artist))

        print ("\n unorganized songs: ")
        for i, (song, artist) in enumerate(self.unorganized_songs.items()):
            print("\t%2s. %-40s by %s" % (i+1, song, artist))

# finds mood of song based on number of mood-specific lyrics
class WordClassifier:
    # creates pairs of mood/mood-specific lyric 
    def __init__(self):
        word_bank = {
            "sad": "sad cry hurt hurts scared lies fear pain lonely die dead hate goodbye heartbreak bye alone misery miss",
            "happy": "happy smile cheer laugh party good great fun funny celebrate excited excite ecstatic adore"
        }
        self.word_class = {}
        for mood, words in word_bank.items():
            for word in words.split():
                self.word_class[word] = mood

    # returns mood
    def get_mood(self, word):
        return self.word_class.get(word, None)

# pre-determined collection of songs for auto function
song_and_artist = {
  "Adore You": "Harry Styles",
  "iT's YoU": "Zayn",
  "Circles": "EDEN",
  "scared": "Jeremy Zucker",
  "Party in the USA": "Miley Cyrus",
  "So Lonely": "Jorja Smith",
  "Nobody Compares": "One Direction",
  "What Makes You Beautiful": "One Direction"
  "Happy": "Pharrell Williams"
}

word_classifier = WordClassifier()
song_stats = SongStats()

# gets actual lyrics from Genius, determines mood, and adds song to appropriate mood dictionary
def analyze(song_name, artist_name):
    song = genius.search_song(song_name, artist_name)
    num_sad = 0
    num_happy = 0
    for word in song.lyrics.split():
        mood = word_classifier.get_mood(word)
        if mood == "sad":
            num_sad += 1
        elif mood == "happy":
            num_happy += 1
    song_stats.add(song_name, artist_name, num_happy, num_sad)

# lyricsgenius library and Genius access token allow access to Genius database
genius = lyricsgenius.Genius("Dkv4TkcUPKXbawsoKcwosPHqK8qiz9B-UPwruoLESzB0Ipm4LpEWLtooD4dZbCrl")   

# initial message to user that provides context on function of program
print("""Welcome to the Mood Song Generator! Please enter the name of a song 
and its artist in the following format: 'song name, artist name'. If you would 
like the computer to use a predetermined set of songs, type 'auto'. If you are 
done entering songs, type 'done' to see the mood analysis.""")

# takes user input until user types 'done'
while True:
    artist_song = input(">> ")  
    if artist_song == "auto":
        for song_name, artist_name in song_and_artist.items():
            analyze(song_name, artist_name)
        break
        
    elif artist_song == "done":
        break
    
    song_name, artist_name = artist_song.split(",")
    artist_name = artist_name.strip()
    song_name = song_name.strip()
    analyze(song_name, artist_name)    
    
song_stats.print()

