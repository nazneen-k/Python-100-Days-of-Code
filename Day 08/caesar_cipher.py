
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(start_text,shift_amout,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
            shift_amout*=-1
    for char in start_text:
          if char in alphabets:
                position=alphabets.index(char)
                new_position = position+shift_amout
                end_text+=alphabets[new_position]
          else:
                end_text+=char
    print(f"The {cipher_direction}d text is {end_text} " )


from art import logo
print(logo)



should_end=False
while not should_end:
      direction=input("Type 'encode' to encrypt, type 'decrypt' to decrypt:\n")
      text=input("Type your message:\n").lower()
      shift=int(input("Type the shift number:\n"))
      shift=shift%26
      caesar(start_text=text,shift_amout=shift,cipher_direction=direction)

      restart= input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
      if restart =="no":
        should_end=True
        print("Good Bye!!")