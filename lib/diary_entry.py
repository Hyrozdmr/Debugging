class DiaryEntry:
    # Parameters:
    #   title: string
    #   contents: string
    def __init__(self, title, contents):
        if title == "" or contents == "":
            return Exception("Diary entries must have a title or contents")
        self._title = title
        self._contents = contents
    

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self._title}: {self._contents}"
         
    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        return  len(self._title.split(" "))

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        return round(len(self._contents.split(" ")) / wpm)
    
    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning
        words_can_read = wpm * minutes
        words = self._contents.split(" ")
        chunk_words = words[:words_can_read]
        return " ".join(chunk_words)