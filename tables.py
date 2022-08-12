#scriptedbysincrytaayush
#sincryptionop

from colorama import Fore

banner=Fore.GREEN+'''                 __     ___    _  _____ _    _ 
     /\        /\\ \   / / |  | |/ ____| |  | |
    /  \      /  \\ \_/ /| |  | | (___ | |__| |
   / /\ \    / /\ \\   / | |  | |\___ \|  __  |
  / ____ \  / ____ \| |  | |__| |____) | |  | |
 /_/    \_\/_/    \_\_|   \____/|_____/|_|  |_|
                                               
                                               '''
print(banner)

banner_2=Fore.RED+''' -------------------BEST TOOL TO GET TABLES OF ANY NUMBER-----------------------------------------------------------------------------
'''

print(banner_2)



def table(numbers):
    for i in range(1,11):
        print(Fore.MAGENTA+f' {numbers} x {i} = {numbers*i}')
        
aayush=int(input(Fore.YELLOW+'enter your number to get table of it ----> '))
print('\n')

table(aayush)