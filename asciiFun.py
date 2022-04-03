'''
Create ascii art text banners from a text 
By: Sologeek, 2022
python 3.8.3
'''
import sys
import random
import requests
import time
import os

# Handling of missing important modules
try:
    import pyfiglet
    from bs4 import BeautifulSoup
    import pyperclip as pc
    from urllib.error import URLError
except ModuleNotFoundError as err:
    print("\n[•] You need to have these Modules installed to use this program:\n'pyperclip', 'beautifulsoup4', 'pyfiglet'")
    time.sleep(.5)
    print("\n[!] You can install them by running 'pip install pyperclip beautifulsoup4 pyfiglet' in terminal (A Virtual Environment  is Higly Recommended). \n[!] You can also install them by running 'pip install -r requirements.txt'")
    time.sleep(.5)
    print("\nNow Exiting...")
    time.sleep(1)
    sys.exit()

    
# Function to generate the actuall Ascii art
def generateAscii(userfont=None):
    os.system('cls')
    global font
    global usertext

    try:
        local_fonts = pyfiglet.FigletFont.getFonts()
        local_fonts_noExtension = [s.replace('.flf', '') for s in local_fonts]
        font = random.choice(local_fonts_noExtension)

        # Get the user's input (inline or input)
        if sys.argv[1:]:
            try:
                if sys.argv[2:]:
                    raise IndexError  # If the user enters more than one argument, raise an error
                ascii_banner = pyfiglet.figlet_format(sys.argv[1], font)               
                print(ascii_banner)
            except IndexError:
                print("\n[!] TOO_MANY_ARGUMENTS: Please put your String in Quotes. Sample Code: \npython3.exe asciiFun.py 'What The Hell'\n")
        else:
            user_input = input('[♦] Enter a string: ')
            usertext = user_input
            if userfont: # in case user wants to a certain font
                print('\n[!] Using font: ' + userfont)
                custom_fig = pyfiglet.Figlet(userfont)
                print('\n', custom_fig.renderText(user_input))
            else:
                print('\n', pyfiglet.figlet_format(user_input, font))

            # Check if the user's input is a number
            if user_input.isdigit():
                # Convert the user's input to an integer
                user_input = int(user_input)
    except KeyboardInterrupt:
        bye()
    except Exception as e:
        print(e)
        bye()

    backtomenu = input('\n[♠] Generate New Ascii Art (y/n): ')
    if backtomenu == 'y':
        generateAscii()
    elif backtomenu == 'n':
        menu()

# Function to copy the ascii art text to clipboard
def copy_to_clipboard():
    # copying stdout to clipboard
    copyfont = font
    text = usertext
    ascii_banner = pyfiglet.figlet_format(text, copyfont)
    pc.copy(ascii_banner)
    print("\n[•] Ascii art copied to clipboard!")

    backtomenu = input('\n[♠] Show Menu? (y/n): ')
    if backtomenu == 'y':
        os.system('cls')
        menu()
    elif backtomenu == 'n':
        bye()

# Function to compare Local fonts and Remote Updated Fonts and Downloading the new ones
def compare_upadte():
    os.system('cls')
    try:
        # Fetching new fonts from the repo/pyfiglet/fonts
        url = 'https://github.com/pwaller/pyfiglet/tree/master/pyfiglet/fonts-contrib'
        print('\n[•] Getting all the font titles for: ' + url)
        time.sleep(1.5)
        print('[•] Pls wait ...')
        time.sleep(1.5)
        print('[•] Done!\n')
        time.sleep(0.5)

        titles_list = []
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('a', attrs={
                            'data-pjax': '#repo-content-pjax-container', 'class': 'js-navigation-open Link--primary'})
        for title in titles:
            titles_list.append(title.get_text())


        # Compare the local fonts and the remote fonts
        fonts_to_be_downloaded = []
        web_fonts = titles_list
        local_fonts = pyfiglet.FigletFont.getFonts()
        local_fonts_with_extension = [lf + '.flf' for lf in local_fonts]
    except URLError:
        print('Check yo Internet! Connection!')
    except Exception as err:
        print('Something went wrong!')
        print(err)


    for font in web_fonts:
        if font not in local_fonts_with_extension:
            fonts_to_be_downloaded.append(font)


    # Download fonts
    print("\n[•] Missing Fonts:")
    print(', '.join(fonts_to_be_downloaded))
    downornot = input(
        "\n[♠] Do you Want to download the the Missing Fonts? (y/n)\n")

    if downornot == 'y':
        pass
    elif downornot == 'n':
        print('\n☻ No fucks given :)')

    backtomenu = input('\n[♠] Show Menu? (y/n): ')
    if backtomenu == 'y':
        os.system('cls')
        menu()
    elif backtomenu == 'n':
        bye()
    

# Function to exit
def bye():
    print("\n[•] Thank you for using the ASCII Generator!")
    time.sleep(0.5)
    print("Goodbye!")
    exit()


# Menu Function to let user run the program again or exit
def menu():
    print("""
++++++++++ MENU ++++++++++
1. Credits 
2. Generate New Ascii Art 
3. Upate Local Fonts
4. Copy this Ascii Art to the clipboard
5. Show current Font name
6. Choose a Font to use for the next run
7. Exit
+++++++++++++++++++++++++++\n
    """)

    # Get the user's choice
    choice = input("[♦] Enter your choice (Just the Number): ")

    try:
        # If the user wants to run the program again
        if choice == '1':
            os.system('cls')
            print("\n~~ Ascii Art Text Banner Generator ~~\nMain Credit goes to: https://github.com/pwaller/pyfiglet, \nI made some Overall changes And customized it by adding some new features, Enjoy :)    \nSpring 2022\n~SoloGeek~\n")
            backtomenu = input('\n[♠] Show Menu? (y/n): ')
            if backtomenu == 'y':
                os.system('cls')
                menu()
            elif backtomenu == 'n':
                bye()
        elif choice == '2':
            generateAscii()
        elif choice == '3':
            compare_upadte()
        elif choice == '4':
            copy_to_clipboard()
        elif choice == '5':
            print('\n[•] The current Font Name is: ' + font)
            backtomenu = input('\n[♠] Show Menu (y/n): ')
            if backtomenu == 'y':
                os.system('cls')
                menu()
            elif backtomenu == 'n':
                bye()
        elif choice == '6':
            userfont = input("[♦] Enter the Font name (Without .flf): ")
            generateAscii(userfont)
        elif choice == '7':
            bye()
        elif choice < '1' or choice > '7':
            raise ValueError(
                '\n[!] Invalid input, choose a number between 1 and 7')
    except KeyboardInterrupt:
        bye()
    except Exception as e:
        print(e)
        menu()


# Main function
def main():
    
    generateAscii()

# Initialize the Main function
if __name__=='__main__':
    main()