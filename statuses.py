import colorama
from colorama import Fore, Back, Style
import sys

ERROR = "[ " + Fore.RED + "ERROR" + Fore.WHITE + " ] : "
SUCCESS = "[ " + Fore.GREEN + "SUCCESS" + Fore.WHITE + " ] : "
RUNNING = "[ " + Fore.GREEN + "RUNNING" + Fore.WHITE + " ] : "
WARNING = "[ " + Fore.YELLOW + "WARNING" + Fore.WHITE + " ] : "
FUNDWAR = "[ " + Fore.YELLOW + "LOW FUNDS" + Fore.WHITE + " ] : "
FUNDERR = "[ " + Fore.RED + "NO FUNDS" + Fore.WHITE + " ] : "
TRADE = Back.BLACK + "[ " + Fore.CYAN + "TRADE" + Fore.WHITE + " ] : "
TRADE_BUY = Back.BLACK + "[ " + Fore.GREEN + "BUY" + Fore.WHITE + " ] : "
TRADE_SELL = Back.BLACK + "[ " + Fore.RED + "SELL" + Fore.WHITE + " ] : "
TRADE_WITHDRAW = Back.BLACK + "[ " + Fore.MAGENTA + "TRANSFER" + Fore.WHITE + " ] : "
PROFIT = "[ " + Fore.GREEN + "PROFIT" + Fore.WHITE + " ] : "

def versioning():
    if('2.7.' in sys.version):
        print(SUCCESS + 'Python ' + sys.version)
    else:
        print(ERROR + 'Python version 2.7.xx required')
        return False

    if('0.3.' in colorama.__version__):
        print(SUCCESS + 'colorama ' + colorama.__version__)
    else:
        print(WARNING + 'install/upgrade colorama for aesthetic appeal')

    return True

print("crypto-data package made by Patrick Grady")

if(not versioning()):
    quit()

colorama.init()