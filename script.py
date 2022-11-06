import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        
def python_project():
    folder_title = input('Folder Name: ')
    foldername = f'C:\\Users\\USER\\ENTER PATH HERE\\{folder_title}'
    createFolder(foldername)
    # Creates a folder in the current directory called data
    # Change directory to fit user's needs - this is only an example
    filename = f'C:\\Users\\USER\\ENTER PATH HERE\\{folder_title}\\main.py'

    f = open(filename, "x")
    f.close()

    print(f"Project Created Successfully at {foldername}")

def html_project():
    folder_title = input('Folder Name: ')
    foldername = f'C:\\Users\\USER\\ENTER PATH HERE\\{folder_title}'
    createFolder(foldername)
    # Creates a folder in the current directory called data

    html_filename = f'C:\\Users\\USER\\ENTER PATH HERE\\{folder_title}\\index.html'
    css_filename = f'C:\\Users\\USER\\ENTER PATH HERE\\{folder_title}\\styles.css'
    
    hf = open(html_filename, "a")
    hf.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Document</title>
</head>
<body>
    
</body>
</html>''')
    hf.close()

    cf = open(css_filename, "x")
    cf.close()

    print(f"Project Created Successfully at {foldername}")    

def menu():
    print('''Menu:
    1. New Python Project
    2. New HTML/CSS Project''')

    choice = int(input('Enter just the number of the choice you want: '))

    if choice == 1:
        python_project()

    elif choice == 2:
        html_project()

    else:
        print("Invalid option")
        menu()

menu()
