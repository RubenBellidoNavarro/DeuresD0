for i in range(25):
    filename = f'exercici{i:03}.py'
    with open(filename, 'w') as file:
        file.write(f'#Arxiu {filename}') 
