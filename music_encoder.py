from mido import Message, MidiFile, MidiTrack
import random


def text_to_binary(text):  # 8 bits each letter
    return ''.join(format(ord(c), '08b') for c in text)


def create_stego_midi(message, output_filename='stego.mid'):

    binary = text_to_binary(message) # get the binary expression
    mid = MidiFile() # create an empty midi file
    track = MidiTrack() 
    mid.tracks.append(track) # combine all tracks

    track.append(Message('program_change', program=12, time=0)) # Marimba

    start_note = 60  # Middle C
    for bit in binary:
        
        note = random.randint(60, 71)  # Pick a random pitch between C4 (60) and B4 (71)
        velocity = 64 if bit == '0' else 65
        track.append(Message('note_on', note=note, velocity=velocity, time=200))
        track.append(Message('note_off', note=note, velocity=64, time=200))


    mid.save(output_filename)
    print(f"MIDI saved with hidden message: {message}")

# Example usage
create_stego_midi("hi")
