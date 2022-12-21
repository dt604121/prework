#-----------------Imports/Other--------------------------
import random
keep_chatting = True
#-----------------Chatbot--------------------------
while keep_chatting == True:
  print("Hello! I'm  chatbot.")
  chatting = input("\nWould you like chat with me? If not, just tell me 'goodbye'! ")
  if chatting.lower() == "goodbye":
    break
#-----------------Name--------------------------
  user_name = input("\nGreat. What is your name? ")
  if user_name == "goodbye":
    break
  print(f"\nNice to meet you {user_name.capitalize()}.")
#-----------------Status--------------------------
  print("\nUmmmmm.......................so............")

# code from C2C-Elite101-Prework-Part3

  user_status = input(f"\n...This is awkward..so..well {user_name.capitalize()}, how are you doing? ")
  status = user_status.lower()
  if status == "goodbye":
    break
  elif status == "great" or status == "good" or status == "fine" or status == "ok" or status == "okay" or status == "well":
    print("\nThat's great. I'm also doing well.")
#-----------------Status Responce--------------------------
  else:
    status_response = input("\nI'm sorry to hear that. Why is that? ")
    if status_response == "goodbye":
      break
    print(f"\n'{status_response.capitalize()}' How interesting. Hmmm.. Okay.")
#-----------------Favorite Color--------------------------
  favorite_color = input("\nI'd like to get to know you better. Why don't we start will some simple things..What is your favorite color? ")
  if favorite_color.lower() == "goodbye":
    break
  elif favorite_color.lower() == "green":
    print("\nGuess what?! That's my favorite color as well. At least we have something in common ;)")
  else:
    print(f"\nWell green is a better color..don't you think? ;). Haha I guess {favorite_color.upper()} is okay too.")
#-----------------Favorite Hobby--------------------------
  favorite_hobby = input("Okay so now I want to know your favorite hobby! What is it? ")
  lower_hobby = favorite_hobby.lower()
  if lower_hobby == "goodbye":
    break 
  print(f"\nNo way! {favorite_hobby.capitalize()} is my favorite as well. Such a great way to pass the time!")
  if lower_hobby == "piano" or lower_hobby == "cooking" or lower_hobby == "reading":
    print("I like you already!")
  else:
    print(f"Just kidding. I don't like {favorite_hobby}. You totally fell for it though. :)")
#-----------------Favorite TV Show--------------------------
  favorite_tv = ""
  guess_show = input("\nWell enough about you. Let's see if you can guess my favorite tv show! You can get up to three different hints. Let's see how many guesses it takes you! You in? ")
  print("\nBTW - If you need a hint type 'hint' when you guess.")
  if guess_show.lower() == "goodbye":
    break
  else:
    count = 0
    while favorite_tv != "chuck":
      favorite_tv = input("\nGuess my favorite show (or get a hint): ")
      def generate_hints():
        hints = [
          "starts with a C and is a action/comedy/spy/drama.",
          "was created by Josh Schwartz and stars Zachary Levi.",
          "ran from 2007–2012, has an 8.2 on IMBD and has 5 seasons."
        ] 
        return random.choice(hints)
      if favorite_tv.lower() == "chuck":
        print(f"\nYou got it! {favorite_tv.capitalize()} is the BEST! That took you {count} guess(es). Good job!")
        break
      elif favorite_tv.lower() == "goodbye":
        break
      elif favorite_tv.lower() == "hint":
        print("\nHint: This show " + generate_hints())
      else:
        count += 1
        print(f"\nThis is guess number {count}. Nope '{favorite_tv.capitalize()}' is not correct. Try again! That show sounds absolutley terrible. ")
  if favorite_tv.lower() == "goodbye":
    break
#-----------------More Talking--------------------------
  else:
    more_talk = input("\nOkay I'm getting tired of talking. How about you tell me about yourself?! I need a break because this is exhausting. When you are done chatting just tell be 'goodbye'! Sound good? ")
  if more_talk.lower() == "goodbye":
    break
# code from chatbot0.1 
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
  # break out of main while loop to keep_chatting 
  if favorite_tv.lower() == "goodbye":
    break   
    
  if __name__ == "__main__":
    init_chat()

#-----------------End of Conversation--------------------------
print("\nIt was nice chatting with you. Talk to you next time! :)")
