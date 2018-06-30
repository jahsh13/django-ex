from django.db import models


class Words(models.Model):
    hashed_word = models.TextField('Hashed version of the word')
    word = models.TextField('The actual word')
    word_length = models.IntegerField('The length of the word')

    def __str__(self):
        return self.word

    def get_word_list(self, letters):
        pass



