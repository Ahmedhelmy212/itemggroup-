import openai
import wikipedia
import qrcode
import webbrowser
import pywhatkit as pwk
import requests
import cv2
import random
import time
import phonenumbers
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
from forex_python.converter import CurrencyRates
from translate import Translator
from username import name1
from username import gender1
from username import age1

print("CyperBot: Hello, I am CyberBot, Your AI Assistance")
print("")
time.sleep(0.5)
user_name = input("CyperBot: Please Enter Your Name For Some Information:\n\nYou: ")
print("")
print("CyperBot: Hi " + user_name + ", I am Happy To Work With You")
time.sleep(0.5)
print("")
print("CyperBot: These Are The Things That I Can Help You With")
print("CyperBot: I Can Be Your Math Assistance")
time.sleep(0.5)
print("add - I Can Add Numbers")
time.sleep(0.5)
print("subtract - I Can Subtract Numbers")
time.sleep(0.5)
print("divide - I Can Divide Two Numbers")
time.sleep(0.5)
print("multiply - I Can Multiply Numbers")
time.sleep(0.5)
print("perimeter - I Can Calculate the perimeter of a shape")
time.sleep(0.5)
print("volume - I Can Calculate The Volume Of The 3D Shapes")
time.sleep(0.5)
print("area - I Can Calculate The Area Of The Shapes")
time.sleep(0.5)
print("any info - I can Give You Any Information About Any Thing")
time.sleep(0.5)
print("dictionary - I Can Give You The Meaning Of Some Words")
time.sleep(0.5)
print("age - I Can Detect Your Age By Your Birth Year")
time.sleep(0.5)
print("wisdom - I Can Give You The Wisdom Of The Day")
time.sleep(0.5)
print("Gpt - You Can Use Chat-Gpt Here")
time.sleep(0.5)
print("facts - I Can Give Some Facts To Increase Your Knowledge")
time.sleep(0.5)
print("track numbers - I Can Track Any Phone Number And Locate Its Location")
time.sleep(0.5)
print("passgen - I Can Create A Hard Password For You")
time.sleep(0.5)
print("game - We Can Play A Game Together")
time.sleep(0.5)
print("face reader - I Can Detect Any Part Of The Face")
time.sleep(0.5)
print("translate - I Can Translate Any Text To Any Language You Want")
time.sleep(0.5)
print("weather updates - I Can Tell You The Weather Updates")
time.sleep(0.5)
print("puzzle - I Can Give You A Number Puzzle ")
time.sleep(0.5)
print("whatsmsg - I Can Send An Automatic Messages to Whats app users")
time.sleep(0.5)
print("qrgen - I Can Make A QR Code Generator For Any Website You Want")
time.sleep(0.5)
print("currency converter -  I Can Covert Any Currency To The Target Currency")
time.sleep(0.5)

lat3 = 31.02658392810344
lng3 = 30.71751479553128
print("------------------------------------------------------------")

command = input("CyperBot: Please Choose One Of the Commands I Can Do\n\nYou: ").lower()
print("")
print("")

if command == 'add' or command == 'Add':
    print("CyperBot: Ok, Let's Start And Add Numbers.")

    num_add = int(input("CyperBot: How Many Numbers You Will Add?\n\nYou: "))
    total1 = 0
    print("")

    for i in range(num_add):
        number = float(input("CyperBot: Enter number " + str(i + 1) + ":\n\nYou: "))
        total1 += number
    print("")
    print("---------------------------------------------------------")
    print("CyperBot: The sum of the numbers is:", total1)

    print("")

elif command == 'gpt' or command == 'Gpt':

    def is_valid_api_key(api_key):
        return api_key.startswith("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")
        #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

    def generate_text(prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None
        )
        return response.choices[0].text.strip()


    def main():
        api_key = input("Enter your OpenAI GPT-3 API secret key: ")

        if not is_valid_api_key(api_key):
            print("Invalid API key. Please provide a valid secret key starting with 'sk-'.")
            return

        openai.api_key = api_key

        print("Welcome to the OpenAI Text Generator!")

        while True:
            user_input = input("You: ")

            if user_input.lower() == 'exit':
                print("Goodbye!")
                break

            prompt = f"You: {user_input}\nOpenAI Bot:"
            response = generate_text(prompt)

            print(f"OpenAI Bot: {response}")


    if __name__ == "__main__":
        main()



elif command == 'currency converter' or command == 'Currency Converter':
    print("CyperBot: OK Lets Start")

    def currency_converter():
        currency_converter = CurrencyRates()
        base_currency = input("CyperBot: Enter the base currency (e.g., USD, EUR, GBP)\nYou: ").upper()
        target_currency = input("CyperBot: Enter the target currency (e.g., USD, EUR, GBP)\nYou: ").upper()
        amount = float(input("CyperBot: Enter the amount to convert\nYou: "))

        exchange_rate = currency_converter.get_rate(base_currency, target_currency)
        converted_amount = amount * exchange_rate

        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")


    currency_converter()


elif command == 'any info' or command == 'Any Info':
    print("CyperBot: Ok, Let's Start")

    user_input = input("CyperBot: Please, what do you want?\nYou: ")

    result = wikipedia.summary(user_input, sentences=3)

    print("CyperBot: Ok, this is what I found:\n\n", result)


elif command == 'qrgen' or command == 'Qrgen':
    print("CyperBot: Ok Lets Start")

    website_url = input("CyperBot: Enter the website URL\nYou: ")
    #https://www.facebook.com/AlImamMuhamedAbduLS
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(website_url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")

    qr_image.save("qrcode.png")

    qr_image.show()

    open_website = input("CyperBot: Do you want to open the website? (yes/no)\nYou: ").lower()
    if open_website == "yes":
        webbrowser.open(website_url)


elif command == 'whatsmsg' or command  == 'Whatsmsg':
    print("CyperBot: Ok Lets Start")

    #phone_number = input("CyperBot: Please Enter The Phone Number With The Country Code\nYou: ")
    #msg = input("CyperBot: Please Enter Your Message Here \nYou: ")

    #pwk.sendwhatmsg(str(phone_number),str(msg), 7, 30)
    pwk.sendwhatmsg_instantly("+201095087290", "Hello")
    pwk.sendwhats_image("+201095087290", "path/to/image.jpg", "Hello")

elif command == 'puzzle' or command == "Puzzle":
    print("CyperBot: Ok Lets Start")
    def guess_number():
        number_to_guess = random.randint(1, 100)  # Generates a random number between 1 and 100
        attempts = 0

        print("CyperBot: Welcome to the Number Guessing Game!")
        print("CyperBot: I have selected a random number between 1 and 100. Can you guess it?")

        while True:
            user_guess = int(input("CyperBot: Enter your guess\nYou: "))
            attempts += 1

            if user_guess < number_to_guess:
                print("CyperBot: Too low! Try again.")
            elif user_guess > number_to_guess:
                print("CyperBot: Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
                break


    guess_number()


elif command == 'weather updates' or command == 'Weather Updates':
    print("CyperBot: Ok Lets Start")

    def get_weather(city, api_key):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data["cod"] == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            return f"Weather in {city}: {weather_description.capitalize()}\nTemperature: {temperature}°C\nHumidity: {humidity}%"
        else:
            return "CyperBot: City not found. Please enter a valid city name."



    api_key = '10076cd5ebad8916185986ba2e3513c3'

    city = input("Enter city name: ")
    print("CyperBot: The Weather Of Your City: ", get_weather(city, api_key))

elif command == 'translate' or command == 'Translate':
    print("CyperBot: OK Lets Start Now")


    def translate_text(text, target_language='en'):
        translator = Translator(to_lang=target_language)
        translation = translator.translate(text)
        return translation

    text_to_translate = input("CyperBot: Enter The Text You Want To Translate\nYou: ")
    target_language = input("CyperBot: Enter The Language You Want To Translate To\nYou:  ")

    translated_text = translate_text(text_to_translate, target_language)
    print("CyperBot: Translated Text Is : ","( ", translated_text, " )")

elif command == 'face reader' or command == 'Face Reader':
    print("CyperBot: Ok Lets Start")
    time.sleep(2)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    nose_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_nose.xml')
    mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_mouth.xml')


    image_path = 'venv/man photo.jpeg'
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_gray = gray[y:y + h, x:x + w]
        roi_color = image[y:y + h, x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:

            eye_center = (x + ex + ew // 2, y + ey + eh // 2)
            radius = int(0.3 * (ew + eh))
            cv2.circle(image, eye_center, radius, (0, 255, 0), 2)


        noses = nose_cascade.detectMultiScale(roi_gray)
        for (nx, ny, nw, nh) in noses:

            cv2.rectangle(roi_color, (nx, ny), (nx + nw, ny + nh), (0, 0, 255), 2)

        mouths = mouth_cascade.detectMultiScale(roi_gray)
        for (mx, my, mw, mh) in mouths:

            center = (x + mx + mw // 2, y + my + mh // 2)
            axes = (mw // 2, int(0.35 * mh))
            cv2.ellipse(image, center, axes, 0, 0, 180, (255, 0, 255), 2)

    print("Name: ", name1)
    print("Gender: ", gender1)
    print("Age: ", age1)

    cv2.imwrite('output image.jpeg', image)
    cv2.imshow('Fun Face Reader', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



elif command == 'game' or command == 'Game':
    print("CyperBot: Ok Lets Play A Game")


    print("CyperBot: Welcome To Rock,Paper,Sicssor Game")
    game = ['Rock', 'Paper', 'Scissor']
    print(game)
    player_choise = input("CyperBot: Please Choose Any Option From The Above List\n You:  ")
    print("You Chose: " + str(player_choise))
    options = ['Rock', 'Paper', 'Scissor']
    computer_choice = random.choice(options)
    print("CyperBot Choice Is:", computer_choice)

    if computer_choice == player_choise:
        print("CyperBot: The Game Ended By A Tie!")
    elif computer_choice == 'Rock' and player_choise == 'Paper':
        print("CyperBot: You Win!")
    elif computer_choice == 'Paper' and player_choise == 'Rock':
        print("CyperBot: You Loosed!")
    elif computer_choice == 'Scissor' and player_choise == 'Rock':
        print("CyperBot: You Win!")
    elif computer_choice == 'Rock' and player_choise == 'Scissor':
        print("CyperBot: You Loosed!")
    elif computer_choice == 'Paper' and player_choise == 'Scissor':
        print("CyperBot: You Win!")
    elif computer_choice == 'Scissor' and player_choise == 'Paper':
        print("CyperBot: You Loosed!")
    else:
        print("CyperBot: Sorry We Don't Have This Option In Our List")
        print("CyperBot: Be Sure Of Your Spelling !MAKE IT CAPITAL LETTERS!")
        print(game)


elif command == 'passgen' or command == 'Passgen':
    print("CyperBot: Ok Lets Start To Make Your Password")

    special_chars = "!@#$%^&*()-_+=~|;:,"
    numbers = "1234567890"
    capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_letters = "abcdefghijklmnopqrstuvwxyz"
    length = int(input("CyperBot: Please Enter The Length Of The Password\nYou: "))
    password = ''
    for i in range(length):
        password += random.choice(special_chars + numbers + capital_letters + small_letters)
    print("CyperBot: Your Password Is: " + "(  " + str(password) + "  )")

elif command == 'Track Numbers' or command == 'track numbers':
    number = input("CyperBot: Please Enter Your Phone Number\n You: ")
    time.sleep(2)
    key = "744c5d59ad4446b7b2df9c1d2a4088ee"
    lat2 = lat3
    lng2 = lng3

    pepnumber = phonenumbers.parse(number, "en")

    location = geocoder.description_for_number(pepnumber, "en")
    print("Location:", location)

    service_provider = phonenumbers.parse(number)
    carrier_name = carrier.name_for_number(service_provider, "en")
    print("Carrier:", carrier_name)

    geocoder = OpenCageGeocode(key)
    result = geocoder.geocode(location)

    if result and 'geometry' in result[0]:
        lat = result[0]['geometry']['lat']
        lng = result[0]['geometry']['lng']
        lat1 = 31.02658392810344
        lng1 = 30.71751479553128
        print("Latitude:", lat1, "Longitude:", lng1)

        myMap = folium.Map(location=[lat1, lng1], zoom_start=9)
        folium.Marker([lat1, lng1], popup=location).add_to(myMap)
        myMap.save("user_location.html")
    else:
        print("Error: Unable to retrieve location details.")

elif command == 'subtract' or command == 'Subtract':

    print("CyperBot: Ok, Let's Start And Subtract Numbers.")

    num_sub = int(input("CyperBot: How Many Numbers You Will Subtract?\n\nYou: "))
    total2 = num_sub
    print("")

    for n in range(num_sub):
        number = float(input("CyperBot: Enter number " + str(n + 1) + ":\n\nYou: "))
        total2 -= number
    print("")
    print("---------------------------------------------------------")
    print("CyperBot: The Difference Of The Numbers Is:", total2)

    print("")

elif command == 'divide' or command == 'Divide':

    print("CyperBot: Ok, Let's Start And Divide Two Numbers.")
    num1 = float(input("CyberBot: Please Enter The First Number To Divide\n\nYou: "))
    print("")
    num2 = float(input("CyperBot: Please Enter The Second Number To Divide\n\nYou: "))
    print("")

    if num2 == 0:
        print("")
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print("The division of " + str(num1) + " divide " + str(num2) + " is: " + str(result))
    print("")

elif command == 'multiply' or command == 'Multiply':

    print("CyperBot: Ok, Let's Start And Multiply Numbers.")
    num_multiply = int(input("CyperBot: How Many Numbers You Will Multiply?\n\nYou: "))
    total_multiply = 1
    print("")

    for i in range(num_multiply):
        number = float(input("CyperBot: Enter number " + str(i + 1) + ":\n\nYou: "))
        total_multiply *= number
    print("")
    print("---------------------------------------------------------")
    print("CyperBot: The Product Of The Numbers Is:", total_multiply)

    print("")

elif command == "perimeter" or command == "Perimeter":

    print("CyperBot: I can help you calculate the perimeter of various shapes.")
    print("")
    print("CyperBot: Available options: square, rectangle, triangle, pentagon, hexagon, heptagon, rhombus")
    print("")
    shape = input("CyperBot: Please enter the name of the shape:\n\nYou: ")
    print("")
    if shape == "square" or shape == "Square":
        side_length = float(input("CyperBot: Enter the length of the square's side:\n\nYou: "))
        perimeter = 4 * side_length
        print("CyperBot: The perimeter of the square is: " + str(perimeter))
        print("")
    elif shape == "rectangle" or shape == "Rectangle":
        length = float(input("CyperBot: Enter the length of the rectangle:\n\nYou: "))
        width = float(input("CyperBot: Enter the width of the rectangle:\n\nYou: "))
        perimeter = 2 * (length + width)
        print("The perimeter of the rectangle is: " + str(perimeter))
        print("")
    elif shape == "triangle" or shape == "Triangle":
        side1 = float(input("CyperBot: Enter the length of side 1:\n\nYou: "))
        side2 = float(input("CyperBot: Enter the length of side 2:\n\nYou: "))
        side3 = float(input("CyperBot: Enter the length of side 3:\n\nYou: "))
        perimeter = side1 + side2 + side3
        print("CyperBot: The perimeter of the triangle is: " + str(perimeter))
        print("")
    elif shape == "pentagon" or shape == "Pentagon":
        side_length = float(input("CyperBot: Enter the length of the pentagon's side:\n\nYou: "))
        perimeter = 5 * side_length
        print("CyperBot: The perimeter of the pentagon is: " + str(perimeter))
        print("")
    elif shape == "hexagon" or shape == "Hexagon":
        side_length = float(input("CyperBot: Enter the length of the hexagon's side:\n\nYou: "))
        perimeter = 6 * side_length
        print("CyperBot: The perimeter of the hexagon is: " + str(perimeter))
        print("")
    elif shape == "heptagon" or shape == "Heptagon":
        side_length = float(input("CyperBot: Enter the length of the heptagon's side:\n\nYou: "))
        perimeter = 7 * side_length
        print("CyperBot: The perimeter of the heptagon is: " + str(perimeter))
        print("")
    elif shape == "rhombus" or shape == "Rhombus":
        side_length = float(input("CyperBot: Enter the length of the rhombus's side:\n\nYou: "))
        perimeter = 4 * side_length
        print("CyperBot: The perimeter of the rhombus is: " + str(perimeter))
        print("")
    else:
        print("Cyperbot: Sorry, I can't calculate the perimeter of " + shape)
        print("")

elif command == 'dictionary' or command == 'Dictionary':
    print("CyperBot: I Can Help You To Know The Meanings Of Some Words in Coding and Programming")
    print("")

    glossaries = ["Syntax", "Concatenation", "Bug", "Variable", "Function", "Algorithm", "Debugging",
                  "Loop", "Conditional", "Class", "Object", "Method", "Inheritance", "Encapsulation",
                  "Polymorphism", "Array", "List", "Dictionary", "Tuple", "Module", "Package",
                  "Exception", "Recursion", "File I/O", "Database", "API", "GUI"]

    definations = ["The Main Structure Of The Code", "Adding text together", "A Problem In The Code",
                   "A named storage location in memory", "A block of code that performs a specific task",
                   "A step-by-step procedure to solve a problem", "The process of finding and fixing errors in code",
                   "A programming construct that repeats a block of code",
                   "A programming construct for decision-making",
                   "A blueprint for creating objects", "A self-contained instance of a class",
                   "A function that belongs to a class and operates on objects",
                   "A mechanism to create new classes based on existing ones",
                   "Hiding the internal details of an object and providing an interface for interaction",
                   "The ability of an object to take on multiple forms",
                   "A data structure to store a collection of elements",
                   "An ordered collection of items that can be changed", "A collection of key-value pairs",
                   "An ordered, immutable collection of elements",
                   "A file containing Python definitions and statements",
                   "A collection of Python modules", "An abnormal event during program execution",
                   "A function calling itself as a subroutine", "Reading from and writing to files in a program",
                   "A system for storing and managing data",
                   "Application Programming Interface - A set of tools for building software",
                   "Graphical User Interface - A visual way for users to interact with software"]

    while True:
        user_answer = input("CyperBot: Say Something\n\n You: ")
        if user_answer in glossaries:
            index = glossaries.index(user_answer)
            print("CyperBot: " + definations[index])
        else:
            print("Sorry, I Can't Find The Word: " + user_answer + " In My Glossaries List")
            answer = input("CyperBot: Can You Teach It To Me? Please Enter Yes Or No:\n\n You: ")
            if answer == 'yes' or answer == 'Yes' or answer == 'Ok' or answer == 'ok' or answer == 'Okay' or answer == 'okay' or answer == 'Fine' or answer == 'fine':
                new_word = input("CyperBot: Please enter the new word\n\n You: ")
                glossaries.append(new_word)
                answer2 = input("CyperBot: Please give me the definition of the word " + new_word + "\n\n You: ")
                definations.append(answer2)
                print("CyperBot: New word and definition added succesfully.")
            elif answer == 'No' or answer == 'no':
                print("CyperBot: Ok, No Problem See You Soon")
            else:
                print("CyperBot: Sorry I Can't Understand What You Say")
                print("CyperBot: Good bye See You Soon")
                print("")

elif command == 'age' or command == 'Age':
    print("CyperBot: Ok, Let's Start And Calculate Your Age")
    print("")
    year_of_birth = int(input("CyperBot: Please Enter Your Year Birth\n\nYou: "))
    age = 2023 - year_of_birth
    print("")
    print("CyperBot: Your Age Is " + str(age))
    print("CyperBot: Is Your Age Correct")
    print("CyperBot: Please Enter Yes Or No")
    yesorno = input("You: ")
    if yesorno == 'Yes' or yesorno == 'yes':
        print("OK Thanks")
        print("")
    if yesorno =='No' or yesorno == 'no':
        print("CyperBot: Now I Think This Is The Correct One")
        print("Your Age Is " + str(int(age) - 1))
        print("")
    print("")

elif command == 'wisdom' or command == 'Wisdom':
    print("CyperBot: I Will Give You The Wisdom Of The Day")
    wisdom_num = int(input("CyperBot: Please Choose A Number From 1 To 15\n\nYou: "))
    print("")

    if wisdom_num == 1:
        print("CyperBot: Steve Jobs Once Said:")
        print("CyperBot: The only way to do great work is to love what you do.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 2:
        print("CyperBot: Robert Frost Once Said:")
        print("CyperBot: In three words, I can sum up everything I've learned about life: it goes on.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 3:
        print("CyperBot: Socrates Once Said:")
        print("CyperBot: The only true wisdom is in knowing you know nothing.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 4:
        print("CyperBot: Lao Tzu Once Said:")
        print("CyperBot: The journey of a thousand miles begins with a single step.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 5:
        print("CyperBot: Nelson Mandela Once Said:")
        print("CyperBot: The greatest glory in living lies not in never falling, but in rising every time we fall.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 6:
        print("CyperBot: Dalai Lama Once Said:")
        print("CyperBot: The purpose of our lives is to be happy.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 7:
        print("CyperBot: Winston Churchill Once Said:")
        print("CyperBot: Success is not final, failure is not fatal: It is the courage to continue that counts.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 8:
        print("CyperBot: Dalai Lama Once Said:")
        print("CyperBot: Happiness is not something ready-made. It comes from your own actions.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 9:
        print("CyperBot: Winston Churchill Once Said:")
        print("CyperBot: Success is not final, failure is not fatal: It is the courage to continue that counts.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 10:
        print("CyperBot: Theodore Roosevelt Once Said:")
        print("CyperBot: The best way to predict the future is to create it.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 11:
        print("CyperBot: Franklin D. Roosevelt Once Said:")
        print("CyperBot: The only limit to our realization of tomorrow will be our doubts of today.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 12:
        print("CyperBot: Eleanor Roosevelt Once Said:")
        print("CyperBot: The future belongs to those who believe in the beauty of their dreams.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 13:
        print("CyperBot: Oscar Wilde Once Said:")
        print("CyperBot: Be yourself; everyone else is already taken.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 14:
        print("CyperBot: Dr. Seuss Once Said:")
        print("CyperBot: Don't cry because it's over, smile because it happened.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")
    elif wisdom_num == 15:
        print("CyperBot: Wayne Gretzky Once Said:")
        print("CyperBot: You miss 100 percent of the shots you don't take.")
        print("")
        print("CyperBot: I hope you find this wisdom quote inspiring you in your Day")
        print("")

elif command == 'facts' or command == 'Facts':
    print("CyperBot: Sure, Let's Learn Some Facts!")

    facts = [
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
        "The Eiffel Tower can grow up to 6 inches taller during the summer due to the expansion of the iron in the heat.",
        "A day on Venus (the time it takes for Venus to rotate once on its axis) is longer than a year on Venus (the time it takes to orbit the sun)!",
        "Octopuses have three hearts: two pump blood to the gills, and one pumps it to the rest of the body.",
        "Polar bears are left-handed.",
        "Honeybees have five eyes.",
        "Bananas are berries, but strawberries are not.",
        "A group of flamingos is called a 'flamboyance.'",
        "A group of owls is called a 'parliament.'",
        "Cows have best friends and can become stressed when separated from them.",
        "There are more possible iterations of a game of chess than there are atoms in the known universe.",
        "The oldest known customer complaint is over 3,700 years old. It was written on a clay tablet in ancient Mesopotamia.",
        "The first recorded use of 'OMG' (Oh My God) was in a letter to Winston Churchill in 1917.",
        "Sea otters hold hands when they sleep to keep from drifting apart.",
        "The unicorn is the national animal of Scotland."
    ]

    while True:
        fact_num = input("CyperBot: Choose a number from 1 to 15 to read an interesting fact:\n\nYou: Number ")
        if fact_num.isdigit():
            fact_num = int(fact_num)
            if 1 <= fact_num <= 15:
                print("")
                print("CyperBot:", facts[fact_num - 1])
                print("")
                break
            else:
                print("CyperBot: Please Enter A Valid Number From 1 to 15")
                print("")
        else:
            print("CyperBot: Please Enter A Valid Number From 1 to 15")
            print("")

elif command == 'Volume' or command == 'volume':
    print("CyperBot: I Can Calculate The Volume of :")
    print("")
    shapes3d = ["Cube", "Cuboid", "Pyramid"]
    print(shapes3d)
    print("")
    shapes3d_user_answer = input("CyperBot: Please Choose The Name Of The 3D Shape From The Above List\n\n You: ")
    if shapes3d_user_answer == 'cube' or shapes3d_user_answer == 'Cube':
        print("")
        print("CyperBot: Ok, Let's Start And Calculate The Volume Of Cube")
        side_length = float(input("CyperBot: Please Enter The Side Length\n\n You: "))
        volume_cube = side_length ** 3
        print("CyperBot: The Volume Of Cube Is: " + str(volume_cube) + " cm³")
        print("")
    elif shapes3d_user_answer == 'cuboid' or shapes3d_user_answer == 'cuboid':
        print("")
        print("CyperBot: Ok, Let's Start And Calculate The Volume Of Cuboid")
        length = float(input("CyperBot: Please Enter The Length\n\n You: "))
        width = float(input("CyperBot: Please Enter The Width\n\n You: "))
        height = float(input("CyperBot: Please Enter The Height\n\n You: "))
        volume_cuboid = length * width * height
        print("CyperBot: The Volume Of Cube Is: " + str(volume_cuboid) + " cm³")
        print("")
    elif shapes3d_user_answer == 'pyramid' or shapes3d_user_answer == 'Pyramid':
        print("")
        print("CyperBot: Ok, Let's Start And Calculate The Volume Of Cuboid")
        base = float(input("CyperBot: Please Enter The base area\n\n You: "))
        height1 = float(input("CyperBot: Please Enter The Height\n\n You: "))
        volume_pyramid = (1 / 3) * base * height1
        print("CyperBot: The Volume Of Cube Is: " + str(volume_pyramid) + " cm³")
        print("")
    else:
        print("CyperBot: Sorry, I Can't Calculate The Volume of " + shapes3d_user_answer)
        print("CyperBot: Please Try Again")
        print("")

elif command == 'area' or command == 'Area':
    print("CyperBot: Lets Start And Calculate The Area Of: ")
    shapes_list = ["Square", "Rectangle", "Triangle", "Pentagon", "Hexagon"]
    print("CyperBot: " + str(shapes_list))
    shape_area = input("CyperBot: Please Choose The Shape To Calculate The Area\n\n You: ")
    if shape_area == 'Square' or shape_area == 'square':
        print("CyperBot: Ok Lets Calculate The Area Of The Square")
        square_sl = float(input("CyperBot: Please Enter The Side Length Of The Square\n\n You: "))
        square_area = square_sl * square_sl
        print("CyperBot: The Area Of The Square = " + str(square_area))
        print("")
    elif shape_area == 'Rectangle' or shape_area == 'rectangle':
        print("CyperBot: Ok Lets Calculate The Area Of The Rectangle")
        rectangle_length = float(input("CyperBot: Please Enter The Length Of The Rectangle\n\n You: "))
        rectangle_width = float(input("CyperBot: Please Enter The Width Of The Rectangle\n\n You: "))
        rectangle_area = rectangle_length * rectangle_width
        print("CyperBot: The Area Of The Rectangle = " + str(rectangle_area))
        print("")
    elif shape_area == 'Triangle' or shape_area == 'triangle':
        print("CyperBot: Ok Lets Calculate The Area Of The Triangle")
        Triangle_height = float(input("CyperBot: Please Enter The Length Of The Triangle\n\n You: "))
        Triangle_base = float(input("CyperBot: Please Enter The Width Of The Triangle\n\n You: "))
        Triangle_area = 0.5 * Triangle_height * Triangle_base
        print("CyperBot: The Area Of The Triangle = " + str(Triangle_area))
        print("")
    elif shape_area == 'Pentagon' or shape_area == 'pentagon':
        print("CyperBot: Ok, Let's Calculate The Area Of The Pentagon")
        pentagon_side = float(input("CyperBot: Please Enter The Side Length Of The Pentagon\n\n You: "))
        pentagon_apothem = float(input("CyperBot: Please Enter The Apothem Length Of The Pentagon\n\n You: "))
        pentagon_area = 0.5 * pentagon_side * pentagon_apothem
        print("CyperBot: The Area Of The Pentagon =" + str(pentagon_area))
        print("")
    elif shape_area == 'Hexagon' or shape_area == 'hexagon':
        print("CyperBot: Ok, Let's Calculate The Area Of The Hexagon")
        hexagon_side = float(input("CyperBot: Please Enter The Side Length Of The Hexagon\n\n You: "))
        hexagon_apothem = float(input("CyperBot: Please Enter The Apothem Length Of The Hexagon\n\n You: "))
        hexagon_area = 0.5 * hexagon_side * hexagon_apothem
        print("CyperBot: The Area Of The Hexagon =", str(hexagon_area))
        print("")
    elif shape_area == 'Rhombus' or shape_area == 'rhombus':

        print("CyperBot: Ok, Let's Calculate The Area Of The Rhombus")
        rhombus_diagonal1 = float(input("CyperBot: Please Enter The First Diagonal Length Of The Rhombus\n\n You: "))
        rhombus_diagonal2 = float(input("CyperBot: Please Enter The Second Diagonal Length Of The Rhombus\n\n You: "))
        rhombus_area = 0.5 * rhombus_diagonal1 * rhombus_diagonal2
        print("CyperBot: The Area Of The Rhombus =", str(rhombus_area))
        print("")
    else:
        print("CyperBot: Sorry, I Can't Calculate The Area Of: " + shape_area)

else:
    print("Thanks For Using CyperBot")
    print("Good Bye Have A Nice Day")