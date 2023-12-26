user_text = input("enter your text: ")
final_pass = []
for i in user_text:
    user_encoder = str(ord(i) + 12)
    final_pass.append(user_encoder)
    
print(",".join(final_pass))
############################
user_pass = input("enter the password: ").split(",")
final_str = ""
for i in user_pass:
    chr_user = chr(int(i) - 12)
    final_str += "".join(chr_user)

print(final_str) 

