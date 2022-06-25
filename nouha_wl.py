from pathlib import Path
import json
import typer
import time


typer.secho('How many informations obtained from victim ??', fg = typer.colors.BRIGHT_RED)

MENU = typer.secho("""    
        1) > 2 information 
        2) > 3 information 
        3) > 4 information 
        4) > 5 information """,fg = typer.colors.YELLOW)

number_info = int(typer.prompt('Select the number of information '))

#create file 
ROOT_FILE = Path(__file__).cwd() 
file_name = input('Enter the wordlist name : ')
ficher = ROOT_FILE / f'{file_name}.txt'
file_name = f'{file_name}.json'
WORDLIST = ROOT_FILE / file_name

if not Path.exists(WORDLIST):
    WORDLIST.touch()

word_array = [] 

def get_number_informations(number = number_info):
    with open(file_name, 'a') as f:
         
        if number == 1:
            for i in range(1,3):
                word = typer.prompt(f"Enter info n°{i} ")
                word_array.append(word)
                
        elif number == 2:
            for i in range(1,4):
                word = typer.prompt(f"Enter info n°{i} ")
                word_array.append(word)
                
        elif number == 3:
            for i in range(1,5):
                word = typer.prompt(f"Enter info n°{i} ")
                word_array.append(word)
        
        elif number == 4:
            for i in range(1,6):
                word = typer.prompt(f"Enter info n°{i} ")
                word_array.append(word)
                
        json.dump(word_array, f, indent=4)

get_number_informations()

# fichier .json -> .txt
def Json_file_to_txt(word_array = word_array):
    arr1 = arr2 = arr3 = arr4 = arr5= []
 

    for i in range(len(word_array)):
        arr1.append(f'{word_array}{i}')
        convert_word_array_to_string = '\n'.join(arr1)
        
        for j in word_array:
            arr2.append(f'{word_array[i]}{j}')
            convert_word_array_to_string = '\n'.join(arr2)
            
            for k in word_array:
                arr3.append(f'{word_array[i]}{j}{k}')
                convert_word_array_to_string = '\n'.join(arr3)
                
                for l in word_array:
                    arr4.append(f'{word_array[i]}{j}{k}{l}')
                    convert_word_array_to_string = '\n'.join(arr4)
                    
                    for m in word_array:
                        arr5.append(f'{word_array[i]}{j}{k}{l}{m}')
                        convert_word_array_to_string = '\n'.join(arr5)
                        
        if not Path.exists(ficher):
            ficher.touch()
                
        with open(ficher, 'a') as f:
            f.write(convert_word_array_to_string)
    
Json_file_to_txt()

def about_me():
    with typer.progressbar(range(100)) as progress:
        for _ in progress:
            time.sleep(0.01)
            
        typer.echo('\n')
        typer.secho('Contact Me : ', fg = typer.colors.BRIGHT_WHITE, bg = typer.colors.BRIGHT_BLACK)
        github = typer.secho('  Github : https://github.com/nouha404 ', fg = typer.colors.BRIGHT_GREEN)
        linkdln = typer.secho('  Linkdln : linkedin.com/in/aboubacar-m-09b427122 \n', fg = typer.colors.YELLOW)
        my_pseudo = typer.secho('  Credit : Nouha404', fg = typer.colors.RED)
        
        typer.secho(r'''
                                |            | |    \   | |  
                    \    _ \  |  |    \    _` | __ _| (  | __ _| 
                _| _| \___/ \_,_| _| _| \__,_|   _| \__/    _|  
                                                 ''', fg = typer.colors.RED)
about_me()