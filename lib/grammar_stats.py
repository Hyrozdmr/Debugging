class GrammarStats:
    def __init__(self):
        self.total_texts_checked = 0
        self.texts_passed_check = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise

        self.text = text
        if text[0].isupper() and text[-1] in [".","!","?"]:
            self.total_texts_checked += 1
            self.texts_passed_check += 1
            return True 
        else:
            self.total_texts_checked += 1
            return False
    
    
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.total_texts_checked == 0:
            return 0
        percentage = (self.texts_passed_check / self.total_texts_checked) * 100
        return int(percentage)
