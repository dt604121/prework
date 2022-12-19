import random
# comment
import os
import sys
keep_chatting = True
while keep_chatting == True:
  print("Hello! I'm  chatbot.")
  chatting = input("\nWould you like chat with me? If not, just tell me 'goodbye'! ")
  if chatting.lower() == "goodbye":
    break
  user_name = input("\nGreat. What is your name? ")
  if user_name == "goodbye":
    break
  print(f"\nNice to meet you {user_name.capitalize()}.")
  
  user_status = input(f"\n...This is awkward..so..well {user_name.capitalize()}, how are you doing? ")
  status = user_status.lower()
  if user_status.lower() == "goodybe" or status == "goodbye":
    break
  elif status == "great" or status == "good" or status == "fine" or status == "ok" or status == "okay":
    print("\nThat's great. I'm also doing well.")
  else:
    status_response = input("\nI'm sorry to hear that. Why is that? ")
    if status_response == "goodbye":
      break
    print(f"\n'{status_response.capitalize()}' How interesting. Hmmm.. Okay.")
  favorite_color = input("\nI'd like to get to know you better. Why don't we start will some simple things..What is your favorite color? ")
  if favorite_color.lower() == "goodbye":
    break
  elif favorite_color.lower() == "green":
    print("\nGuess what?! That's my favorite color as well. At least we have something in common ;)")
  else:
    print(f"\nWell green is a better color..don't you think? ;). Haha I guess {favorite_color.upper()} is okay too.")
  favorite_hobby = input("\nOkay so now I want to know your favorite hobby! What is it? ")
  lower_hobby = favorite_hobby.lower()
  if lower_hobby == "goodbye":
    break 
  print(f"\nNo way! {favorite_hobby.capitalize()} is my favorite as well. Such a great way to pass the time!")
  if lower_hobby == "piano" or lower_hobby == "cooking" or lower_hobby == "reading":
    print("\nI like you already!")
  else:
    print(f"\nJust kidding. I don't like {favorite_hobby}. You totally fell for it though. :)")
  favorite_tv = ""
  guess_show = input("\nWell enough about you. Let's see if you can guess my favorite tv show! Well, what do you think? ")
  if guess_show.lower() == "goodbye":
    break
  while favorite_tv != "chuck":
    favorite_tv = input("\nGuess my favorite show: ")
    if favorite_tv.lower() == "goodbye":
      break
    elif favorite_tv.lower() == "chuck":
      print(f"\nYou got it! {favorite_tv.capitalize()} is the BEST! ")
      break
    else:
      ('\nNope. Try again! That show sounds terrible. ')
  if favorite_tv.lower() == "goodbye":
    break
  else:
    more_talk = input("\nOkay I'm getting tired of talking. How about you tell me about yourself?! I need a break because this is exhausting. When you are done chatting just tell be 'goodbye'! Sound good? ")
  if more_talk.lower() == "goodbye":
    break
  def generate_response(user_input):
    responses = [
      "How interesting!",
      "You don't say!",
      "Very cool!",
      "Hmm..",
      "Nice!",
      "Ah. Okay",
      "Wow."
        ] 
    return random.choice(responses)
  
  def init_chat():
    quit_word = "goodbye"
      
    user_input = input("\nTell me something about you: ")
  
    
    while user_input != quit_word:
      user_input = input("\n" + generate_response(user_input) + "\n" + "\n")
        
  if __name__ == "__main__":
    init_chat()

print("\nIt was nice chatting with you. Talk to you next time! :)")
