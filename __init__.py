from aqt.reviewer import Reviewer

_old_answer_button_list = Reviewer._answerButtonList
_old_answer_card = Reviewer._answerCard


def answer_button_list(self):
    buttons = _old_answer_button_list(self)

    if self.card and self.card.queue == 1:
        buttons = tuple(button for button in buttons if button[0] != 4)

    return buttons


def answer_card(self, ease):
    if self.card and self.card.queue == 1 and ease == 4:
        return

    return _old_answer_card(self, ease)


Reviewer._answerButtonList = answer_button_list
Reviewer._answerCard = answer_card