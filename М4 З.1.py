import os

text = input()

def write_and_read(text):
    file_path = os.path.join("/tmp", "temp_file.txt")
    
    # Write text to file
    with open(file_path, "w") as file:
        file.write(text)
    
    # Read text from file
    with open(file_path, "r") as file:
        text_from_file = file.read()
    
    # Remove the temporary file
    os.remove(file_path)
    
    return text_from_file

print(write_and_read(text))