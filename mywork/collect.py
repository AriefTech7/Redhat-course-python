def collect():
    prompt = "Enter a number (or the word 'end' to quit) "
    collect_data = []
    while True:
        data = input(prompt)
        if data != "end":
            collect_data.append(int(data))
        elif data == "end":
            break
        # Remainder of while loop goes here

    return collect_data
    # return  f"this is a sum number {sum(collect_data)}"

