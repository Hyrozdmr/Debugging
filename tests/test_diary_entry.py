from lib.diary_entry import *

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My Title" , "Some contents")
    result = diary_entry.format()
    assert result == "My Title: Some contents"
    
def test_counts_words_in_both_title_and_contents():
    diary_entry = DiaryEntry("My Title" , "Some contents")
    result = diary_entry.count_words()
    assert result == 2

def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry("Galatasaray" , "we are the best")
    result = diary_entry.reading_time(2)
    assert result == 2


def test_reading_chunck_with_wpm_and_minutes():
    diary_entry = DiaryEntry("Galatasaray" , "we are the best")
    assert diary_entry.reading_chunk(2,1) == "we are"
