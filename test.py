import requests
from colorama import init, Fore, Style
import logging
import os
import platform
import time

# Initialize colorama
init(autoreset=True)

# Replace with your ngrok URL
ngrok_url = 'https://6f16-2402-800-620f-c3e0-c03e-da38-a53a-b85f.ngrok-free.app'

# Sample API key (Replace with a valid one if needed)
api_key = 'main'

# Setup logging
logging.basicConfig(filename='api_client.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def clear_console_and_show_banner():
    # Clear the console
    os.system('cls' if platform.system().lower() == 'windows' else 'clear')
    # Display the banner
    print(Fore.YELLOW + Style.BRIGHT + """
  _______ _________ _______  _______  _______  _______  _______ 
 (  ____ \\__   __/(  ___  )(  ____ \\(  ___  )(  ____ \\(  ____ \\
 | (    \/   ) (  | (   ) || (    \/| (   ) || (    \/| (    \/
 | |         | |  | |   | || (____  | (___) || (__    | (_____ 
 | |         | |  | |   | |(_____ \\ |  ___  ||  __)   (_____  )
 | |         | |  | |   | |      ) )| (   ) || (            ) )
 | (____/\\___) (  | (___) |/\\____) )| )   ( || (____/\\ /\\____) )
 (_______/\\_______) (_______)\\______/ |/     \\|(_______/(_______/ 
                                                                 
    """)

def log_and_print_response(response):
    if response.status_code == 200:
        print(Fore.GREEN + Style.BRIGHT + "Success:")
        logging.info(f'Success: {response.json()}')
    else:
        print(Fore.RED + Style.BRIGHT + "Error:")
        logging.error(f'Error: {response.json()}')
    print(response.json())

def create_order():
    clear_console_and_show_banner()
    print(Fore.CYAN + "Creating an order...")
    type = input("Enter order type (AD/BF): ")
    tk = input("Enter tk: ")
    mk = input("Enter mk: ")
    url = f'{ngrok_url}/stock/{type}'
    headers = {'X-API-Key': api_key}
    params = {'tk': tk, 'mk': mk}
    response = requests.get(url, headers=headers, params=params)
    log_and_print_response(response)

def retrieve_account():
    clear_console_and_show_banner()
    print(Fore.CYAN + "Retrieving account...")
    orderID = input("Enter orderID: ")
    url = f'{ngrok_url}/account'
    params = {'orderID': orderID}
    response = requests.get(url, params=params)
    log_and_print_response(response)

def clear_data():
    clear_console_and_show_banner()
    print(Fore.CYAN + "Clearing data...")
    url = f'{ngrok_url}/clear'
    headers = {'X-API-Key': api_key}
    response = requests.get(url, headers=headers)
    log_and_print_response(response)

def check_orders():
    clear_console_and_show_banner()
    print(Fore.CYAN + "Checking orders...")
    url = f'{ngrok_url}/check'
    headers = {'X-API-Key': api_key}
    response = requests.get(url, headers=headers)
    log_and_print_response(response)

def create_custom_api_key():
    clear_console_and_show_banner()
    print(Fore.CYAN + "Creating a custom API key...")
    key = input("Enter custom API key: ")
    url = f'{ngrok_url}/createApiKey/custom'
    params = {'key': key}
    response = requests.get(url, params=params)
    log_and_print_response(response)

def get_stats():
    clear_console_and_show_banner()
    print(Fore.CYAN + "Getting stats...")
    url = f'{ngrok_url}/stats'
    response = requests.get(url)
    log_and_print_response(response)

def get_pricing():
    clear_console_and_show_banner()
    print(Fore.CYAN + "Getting pricing data...")
    url = f'{ngrok_url}/pricing'
    response = requests.get(url)
    log_and_print_response(response)

def update_pricing():
    clear_console_and_show_banner()
    print(Fore.CYAN + "Updating pricing data...")
    item = input("Enter item (spotify/netflix/discord_nitro/robux): ")
    price = float(input("Enter new price: "))
    duration = None
    if item in ['netflix', 'discord_nitro', 'robux']:
        duration = input("Enter duration (1m/3m): ")
    url = f'{ngrok_url}/pricing/{item}'
    data = {'price': price}
    if duration:
        data['duration'] = duration
    response = requests.put(url, json=data)
    log_and_print_response(response)

def menu():
    clear_console_and_show_banner()
    print(Fore.YELLOW + Style.BRIGHT + "\nSelect an action:")
    print("1. Create Order")
    print("2. Retrieve Account")
    print("3. Clear Data")
    print("4. Check Orders")
    print("5. Create Custom API Key")
    print("6. Get Stats")
    print("7. Get Pricing Data")
    print("8. Update Pricing Data")
    print("9. Exit")

if __name__ == '__main__':
    while True:
        menu()
        choice = input("Enter your choice (1-9): ")
        if choice == '1':
            create_order()
        elif choice == '2':
            retrieve_account()
        elif choice == '3':
            clear_data()
        elif choice == '4':
            check_orders()
        elif choice == '5':
            create_custom_api_key()
        elif choice == '6':
            get_stats()
        elif choice == '7':
            get_pricing()
        elif choice == '8':
            update_pricing()
        elif choice == '9':
            print(Fore.YELLOW + "Exiting...")
            logging.info("Exiting the application")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")
            logging.warning(f'Invalid choice: {choice}')
