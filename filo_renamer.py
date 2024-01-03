import os

# Specify the directory containing the .txt files
directory_path = '/home/soma1/문서/swm_team_filo/kohya_ss/trained_outputs/try_5_multi_lora_reg/img/20_waj style'

# Function to append "hta style" to a .txt file
def append_hta_style(file_path, word):
    content = ""
    with open(file_path, 'r') as file:
        content = file.read()
    content = content.replace('\n', '')
    idx = content.find('style')
    if idx != -1:
        print('found style! \n', content)
    # Append "hta style" without adding a newline
    # content += word
    
    with open(file_path, 'w') as file:
        file.write(content)
        # file.write(''.join(content.splitlines()))

# Iterate through files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory_path, filename)
        word = ", hta style" # this will be added at the end of the sentence
        append_hta_style(file_path, word)

print(f"Done appending '{word}' to .txt files.")
