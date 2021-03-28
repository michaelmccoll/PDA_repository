### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):    
    if card.value = 1:                      # There should be a double == rather than single
      return True
    else                                    # Missing a colon (:)
      return False
   

  dif highest_card(self, card1 card2):      # 'dif' should be 'def' and missing a comma between card1 & card2
  if card1.value > card2.value:             # 'if statement should be indented right
    return card                             # 'card' should be 'card1'
  else:
    return card2                        
                                            # Function should be a third outcome using 'elif', for when the cards are the same value


def cards_total(self, cards):               # Alignment of function should all be tabbed once
  total                                     # 'total' needs to be assigned with a zero value
  for card in cards:                        # 'for' needs to be same indentation as return
    total += card.value
    return "You have a total of" + total    # This needs to be formatted correctly with an 'f' at start
  
```
