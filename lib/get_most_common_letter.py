def get_most_common_letter(text):
    counter = {}
    for char in text:
        print(f" char, {char}")
        counter[char] = counter.get(char, 0) + 1
        print(f" counter(char), '{counter(char)}'")
    letter = sorted(counter.items(), key=lambda item: item[1])[-2][0]
    print(f"* Sorted counter {letter}")
    return letter

print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
