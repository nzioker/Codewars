# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
# Your task is to write a function maskify, which changes all but the last four characters into '#'.


def maskify(x):
    holder = ""
    for i in x[:-4]:  # slice off the first x - 4 elements and add them to a variable
        holder += "#"
    holder += x[-4:]  # add the last 4 items to a variable
    print(holder)


maskify("4556364607935616")
