class word_buffer():

    def __init__(self):
        self._word = ''

    def get_word(self):
        return self._word

    def set_word(self, n_word:str):
        self._word = n_word