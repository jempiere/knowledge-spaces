"""
This will actually run the quiz
and serialize the output into
something saveable into the graph
"""
import re


def Answer(correct:bool, order:list, delta:float):
  # correct is True if the quesiton was entirely correct.
  # order will be the exact response of the question in the form of a list.
  # delta will be a score from -1 to 0 where -1 is entirely incorrect and 0 is entirely correct.
  return (correct,order,delta)

class Question:
  SORT  = 0 # input strings in a list in the correct ordering.
  CHOICE= 1 # input a list of tuples. each tuple is of the format ("choice", return_value)
  BLANK = 2 # input a list of typles. each tuple contains (prompt,(possible solutions)). possible solutions can be in tuples to indicate alternates. Regex will be used based on the flag.
  FREE  = 3 # input a list containing at least one prompt. Each prompt will have a free resonse question asked.
  def __init__(self,*,name,type,message,choices,random=False,regex=False):
    """ name:str || type:SORT|CHOICE|BLANK|FREE || message:str || choices:list || random:bool || regex:bool"""
    self.name:str = str(name)
    self.type:int = self.assert_enum(type)
    self.message:str  = str(message)
    self.choices:list = choices
    self.random :bool = bool(random)
    self.regex  :bool = bool(regex)

  def ask(self,pprinter):
    # if pprinter is enabled, relay the name and choices in correct order to self.pprint(*).
    # if pprinter is None, print them out and use the default command line interface. See Textualize.
    # this should return a tuple of (boolean, list, float). View the documentation for the Answer function.
    ...

  def shuffle(self):
    # determined by self.type and self.random.
    # for SORT   : this will randomly shuffle self.choices if self.random is True
    # for CHOICE : this will randomly shuffle self.choices if self.random is True
    # for BLANK  : this will randomly shuffle the order of possible responses if self.random is True
    # for FREE   : this will do nothing.
    ...

def test():
  question_1_choices = ["Traverse underground or in tall grass.","Use a pokéball on Diglett.","Return to Celadon.","Buy Lemonade.","Use lemonade on Diglett."]
  question_1 = Question(name="1", type=Question.SORT, msg="Locate, Capture, and heal a diglett.", random=True, choices=question_1_choices)

  ok, order, delta = question_1.ask()

