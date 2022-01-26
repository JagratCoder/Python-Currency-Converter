def convert(inr):
    '''This Function Converts Indian Rupees to United States Dollar'''
    # 1 usd = 74.93
    # usd = 1
    # rupees = 74.93
    converted = inr/74.93
    return converted

print(convert(80000))