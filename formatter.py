# This formats Cornell's movie dialogues into a format that chatterbot's ListTrainer can easily use.
# Desired output: each line is a conversation, a list of strings where each string is a statement said by a character.
import ast

with open('training.txt', 'w+') as training:
    training_str = ""
    with open('movie_conversations.txt') as conversations:
        with open('movie_lines.txt') as movie_lines:
            statements = {}
            for lin in movie_lines:
                ay = lin.split(" +++$+++ ")
                statements[ay[0]] = ay[4]

        for line in conversations:
            training_line = []

            line_list = line.split(" +++$+++ ")
            statement_codes = ast.literal_eval(line_list[3]) # list of strings

            for statement_code in statement_codes:
                # search for the correct statement code somehow,
                # and then write it to new file comma seperated
                training_line.append(statements[statement_code].rstrip())

            #training.write("++".join(training_line) + "\n")
            training_str += "++".join(training_line) + "\n"

    training.write(training_str)
