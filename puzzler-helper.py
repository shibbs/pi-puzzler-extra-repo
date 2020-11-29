
def encode_message( message):
    foo = len(message)
    ch = bytes(message, 'utf-8')
    message_out=""
    for bar in range(foo) :
        s = bytes([ch[bar] + 1])
        s = str(s)
        message_out= message_out+s[2]
    return message_out

def decode_message(message):
    foo = len(message)
    ch = bytes(message, 'utf-8')
    message_out=""
    for bar in range(foo) :
        s = bytes([ch[bar] - 1])
        s = str(s)
        message_out= message_out+s[2]
    return message_out

decoded = decode_message("Tpnf`djqifst`bsf`tuspohfs`uibo`puifst")
print(decoded)
