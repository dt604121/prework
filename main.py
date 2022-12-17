chatting = ""
print("Hello! I'm  chatbot.")
while chatting.lower() != "bye":
  chatting = input("\nWould you like chat with me? If not, just tell me 'bye'! ")
  if chatting.lower() == "bye":
    break
  user_name = input("\nGreat. What is your name? ")
  print(f"\nNice to meet you {user_name.capitalize()}.")
  user_status = input(f"\n...This is awkward..so..well {user_name.capitalize()}, how are you doing? ")
  status = user_status.lower()
  if status == "great" or status == "good" or status == "fine" or status == "ok" or status == "okay":
    print("\nThat's great. I'm also doing well.")
  else:
    status_response = input("\nI'm sorry to hear that. Why is that? ")
    print(f"\n'{status_response}' How interesting. Hmmm.. Okay.")
print("\nIt was nice chatting with you. Talk to you next time! :)")