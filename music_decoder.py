from mido import MidiFile

def decode_message_from_midi(file_path):

    mid = MidiFile(file_path)  # open the midi file
    bits = ''  # create an empty string


    for msg in mid.tracks[0]:
        if msg.type == 'note_on' and msg.velocity > 0:
            bits += str(msg.velocity & 1)  # extracts the least significant bit of the velocity.


    bits = bits[:len(bits) - (len(bits) % 8)] # Makes sure the length of bits is a multiple of 8.

    # Group bits into bytes (8 bits/char)
    chars = []
    for i in range(0, len(bits), 8):  # Loops through bits in chunks of 8.
        byte = bits[i:i+8]  
        char = chr(int(byte, 2))
        
        if char == '~':   # stop at terminator
            break
        chars.append(char)

    return ''.join(chars)

# Example usage
file_path = 'stego.mid'
hidden_message = decode_message_from_midi(file_path)
print("Decoded message:", hidden_message)
