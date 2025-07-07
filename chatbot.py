import random
name = input("what's your name?😊")
print("Hi" + name + ", you're doing amazing!!!💖")
mood = input("How are you feeling today?😇")
if mood.lower() == "happy":
  print("Yay!! I am so glad you're feeling happy today! keep smiling!!😊✨")
elif mood.lower() == "sad/not good":
  print("awww I'm sorry to hear that,I hope you feel better soon 💖")
elif mood.lower() == "confused":
  print("It's okay to feel confused sometimes," + name +
        ".Everything will make sense soon!💖. you're doing great!👍🥰")
else:
  print(
      "Hmm I may not understand that mood, but I hope you'll feel alright soon!!💖😊"
  )
  color = input("what'syour favourite color?")
  print("WOW!!" + color + " is such a lovely color!!!!!")
  age = int(input("how old are you??🎂"))
  birth_year = 2025 - age
  print("you were probably born in" + str(birth_year) +
        "             yayyy !!! that's awesawesome 🎂")
  hobby = input("What do you like to do for fun ??")
  print("oohhh!! " + hobby +
        "sounds so much fun and relaxing! you're really cool!!😎🫡")
  food = input("what's your favourite food ??")
  print("yummm!! I love " + food + "too!! it's soo delicious 😋")
  print("you're amazing, " + name + " 💗 don't forget thaat okayy???")
  print("Thanks for chatting with me! see you soon !!!🥰💖✨")
  print("Byeeee!!!")
print("\nLet's play a quick math game! 😁🧠")
num1 = int(input("pick any number:"))
num2 = int(input("Now pick another numbr: "))
sum = num1 + num2 
print("Guess what?! " + str(num1) + " + " + str(num2) + " = " + str(sum) + " 🎉 smart choice!!")
print("\nWanna hear a joke ?😄")
print("Why did the computer go to therapy? 💻")
input("...") # wait for Enter 
print("beacause it had too many bytes of emotional data! 😭😂")
print("\n✨ here's something for you:")
print("Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.💖")
print("You are capable of doing anything you set your mind to. Don't let anyone or anything hold you back from achieving your dreams.🥰")
print("You are strong, you are brave, and you are worthy of all the good things in life. Keep going,keep fighting,and never give up on yourself.💖💖🌟🥰")
# Surprise compliment
print("\nYou are amazing, " +name + "! Keep spreading that vibe and shining bright as the star you are")
# Fun Quiz ahead LET'S GOOOOOOOOOOOOOOOO !!!!!!!
print("Let's play a little game before you go!!")
print("\nLet's warm up with few riddles!!\n")
score = 0
print("Riddle 1 : what has keys but can't open locks?") 
ans1 = input("your answer: ")
if "piano" in ans1.lower():
      print("correct!!!!🎉🌟")
      score += 1
else: 
      print("Oops! it's a piano 🎹")
      print("\nRiddle 2 : what come once in a minute, twice in moment,but never in a thousand years??")
      ans2 = input("your answer:")
      if "M" in ans2.lower():
            print("you are right!!!!🎉🌟")
            score += 1
      else:
            print("ohhh noo the answer is letter 'M'")
            print("\nRiddle 3 : I speak without a mouth and hear without ears. I have no body, but i come alive with the wind. What am I??")
            ans3 = input("your answer:")
            if "echo" in ans3.lower():
                  print("woohooo!! you're really smart 🧠 🎉🌟")
                  score += 1
            else:
             print("Oops! the answer is echo")
print("\nyou got {score}/3 riddles right!!🥳🥂")
print("\nLet's play a quick game - guess the number!!\n")
number_to_guess = random.randint(1, 10)
guess = int(input("I'm thinking of a number between 1 and 10. can you guess what it is? 🤔💭\n"))
if guess == number_to_guess:
      print("WOW!! you're a mind reader you guessed it right🎉🌟")
else:
      print("Oops! Not quite. The number I was thinking of", number_to_guess) 
      print("But what a great try!!😄 Keep practicing!")
      play_again = input("\nWanna try guessing again? (yes/no):🥰\n")
      if play_again.lower() == "yes" :
            print("Just hit the run button again and let's play!! I'm ready")
      else:
            print("Okayyyy!! Let's continue chatting then!!")
print("\nReady for a challange? Let's decode a secret word!!")
print("I'll give you a scrambled word. You have to guess the original word.")
word_list ={
      "mopucetr": "coumputer",
      "yptnoh": "python",
      "rgmproanimg": "programing",
      "odcieng": "coding",
      "lpaep": "apple"}
for scrambled, correct in word_list.items():
      answer = input(f"\nUnscramble this word: {scrambled}\nYour guess: ")
      if answer.lower() == correct:
            print("You got it right!! yeahhh!!!!🥳🥂")
      else:
            print(f"❌Oops! The correct word was: {correct}")
            print("🎉Great job decoding! you're a mini detective!!🕵🏻") 
            print("\nLet me predict your vibe for the today.....")
            predictions = [
                  "Today's your lucky day! "
                  "You're going to smile unexpectedly😄"
                  "A small surprise awaits you today🎁"
                  "you might meet someone interesting 👀"
                  "You'll learn something new and exciting today"
                  "The universe is cherring for you!!!💫"
                  "Time to manifest your dreams!!🌌"]
            print("🔮 your fortune: " + random.choice(predictions))
            print("\nLet's play 'This or That'")
            print("Answer with '1' or '2'")
            print("1. coffee or tea?")
            choice1 = input("your pick: ")
            print("Nice choice! we respect all caffine preferences 🙂‍↕️")
            print("1.beaches🌊 or mountains🗻?") 
            choice2 = input("your pick: ")
            print("Ohh that's a vibe!")
            print("1.books or movies?")
            choice3 = input("your pick: ")
            print("Cool cool cool....noted")
            print("\n🔥Rapid Fire Round! Answer fast,okay? Type the first thing that comes to your mind!")
            q1 = input("what's your favourite season?")
            q2 = input("If you had 1 superpower what would it be?💫") 
            q3 = input("Describe yourself in one word👀💫.")
            q4 = input("What's one food you could eat forever😋?")
            q5 = input("If you were an animal, which one would you be??🫏")
            print("\nWoohoo that was fast!!🔥")
            print("so you're a {q3}-person who loves {q1},dreams of being a {q5},and can eat {q4} all day while flying around with {q2} powers!!")
            compliments = [
                  
                  "you're doing amazing my friend !!!"
                  "you have a heart of gold💖"
                  "your energy is unmatched😎"
                  "you're lowkey the main charecter"
                  "you make everything better"
                  "you're a total vibe"
                  "you radiate good energy"]
            personality_traits = [
                  "creative"
                  "kind"
                  "curious"
                  "ambitious"
                  "funny"
                  "chill"
                  "bold"]
            print("\nHere's a little something for you:")
            print(random.choice(compliments))
            print(f"Also, I think you're super {random.choice(personality_traits)}!")
            print("\nIt was soo much fun chatting with you today!!")
            print("Remember, you're always welcome here")
            print("If you feel like talking again... just restart me again")
            print("\nThank you for spending your time with me !!")
            print("until next time..... Byeeee!!!💖🥰💌")
            
            
            
            
                  
            
            

            



