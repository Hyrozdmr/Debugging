class GrammarStats:
    def __init__(self):
        self.total_texts_checked = 0
        self.texts_passed_check = 0

    def check(self, text):
        self.text = text
        start_with_capital = self.text[0].isupper()
        ends_with_punctuation = self.text[-1] in [".", ",", "!", "?"]
        passed_check = start_with_capital and ends_with_punctuation
        self.total_texts_checked =+ 1
        if passed_check:
            self.texts_passed_check += 1

        return passed_check    
    
    def percentage_good(self):
        percentage = (self.texts_passed_check / self.total_texts_checked) * 100
        return int(percentage)
    

        
