#Import libraries
import random

from textblob import TextBlob

#1. Opening & Greeting
print('Welcome to Amadeus Tourism Agency! \n')
print('Hello! How can I help you today? \n')
issue = input()
blob = TextBlob(issue)
if blob.polarity > 0:
  print('Glad to hear this, we are always here to serve you better! \n ')

  # goodbyes = [
  # 'We are always here to help you!',
  # 'I am glad to you help you, goodbye!'
  # ]
  # print(random.choice(goodbyes))

else:
  print('\n Sorry to hear that, let me check my solutions: \n ')
  if 'hotel' in issue.lower():
    print('I can suggest you different hotel in your area, would you like me to change your reservation? \n')
    answer=input()

    if 'yes' in answer.lower():

      print('Here are the suggestions: \n Ritz-Carlton \n Sheraton \n Divan Hotel \n\n Would you like to select one of these options?')
      answer=input()

      match answer:
        case "Ritz-Carlton":
          print("Now we updated your reservation for Ritz-Carlton! \n")
        case "Sheraton":
          print("Now we updated your reservation for Sheraton! \n")
        case "Divan Hotel":
          print("Now we updated your reservation for Divan Hotel! \n")
    else:
      print ('You can call our Customer Service for more information... +1-555-55-55 \n')

    print('Is this solved your problem? \n')
    answer=input()
    blob=TextBlob(answer)
    if blob.polarity > 0:
      print('Glad to hear this! \n ')
      goodbyes = [
      'We are always here to help you!',
      'I am glad to you help you, goodbye!'
      ]
      print(random.choice(goodbyes))
  elif 'return' in issue.lower():
    print('For the overseas tours you will get your return in 7 work days \n \nFor local tours you will get your return in 5 work days \n\nFor more information you can call Customer Service from +1-555-55-55')
    quit()
  
  elif 'flight' in issue.lower():
    print('How can I help you about your flight? \n')
    answer=input()
    print ('Sure, we can change your flight date! Here are the new options: \n 15 Jan 2023 - 21:30 \n 20 Jan 2023 - 06:30 \n 15 Feb 2023 - 16:00')
    answer=input()
    blob=TextBlob(answer)
    print('Your flight is updated now \n')

    if blob.polarity > 0:
      print('Glad to hear this! \n ')
      goodbyes = [
        'We are always here to help you!',
        'I am glad to you help you, goodbye!'
      ]
      print(random.choice(goodbyes))
  print('How do you rate our service, please write your comments: ')
  answer=input()
  blob=TextBlob(answer)

  if blob.polarity > 0.5:
    print('Thank you for your comments, we are always here to help you!')
  elif blob.polarity > 0.1:
    print('Thank you for your comments, you can always write your questions!')
  elif blob.polarity < -0.5:
    print('We are sorry to hear this, you can leave your number and we can call you for solve your issue closely.')
  elif blob.polarity < -0.5:
    print("Sorry to hear this. ")
  else:
    print('That is a very neutral view on ')
  #print('If you are looking for a solution except your reservations, flights or returns you can call our Customer Service 24 x 7 from +1-555-55-55 \n Thank you for choosing us!')