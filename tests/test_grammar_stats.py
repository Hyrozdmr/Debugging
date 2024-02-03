from lib.grammar_stats import *
def test_text_begins_with_capital_and_ends_with_punctuation():
    grammar_stats = GrammarStats()
    result = grammar_stats.check("Galatasaray!")
    assert result == True

def test_percentage_good():
    grammar_stats = GrammarStats()    
    grammar_stats.check("Galatasaray!")
    grammar_stats.check("world!")
    grammar_stats.check("Testing.")
    grammar_stats.check("check")
    grammar_stats.check("Hello?")
    result = grammar_stats.percentage_good()
    assert result == (3 / 5) * 100