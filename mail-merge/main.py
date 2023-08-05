
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    sample_contents = starting_letter.read()

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
    for name in names:
        new_name = name.strip()
        new_content = sample_contents.replace("[name]", new_name)
        with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as new_letter:
            new_letter.write(new_content)
