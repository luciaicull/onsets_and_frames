import mido
import pretty_midi

import numpy as np

def parse_midi(path):
    midi = mido.MidiFile(path)

    time = 0
    sustain = False
    events = []
    print(midi.tracks[1][0])

    for message in midi:
        print(message)
        time += message.time

        '''
        # if the message is a control_change message with damper pedal
        
        control_change 64 
            value >= 64 damper pedal(right pedal) on
            value <= 63 damper pedal off
        control_change 66 sostenuto(middle pedal)
        control_change 67 soft pedal(left pedal)
        '''
        if message.type == 'control_change' and message.control == 64:
            if message.value >= 64:
                sustain = True
                # new_event = dict(index=len(events), time=time, type='sustain_on', note=None, velocity=0)
            else :
                sustain = False
                # new_event = dict(index=len(events), time=time, type='sustain_off', note=None, velocity=0)
            # events.append(new_event)

        if 'note' in message.type:
            if message.type == 'note_on':
                velocity = message.velocity
            else:
                velocity = 0

            new_event = dict(index=len(events), time=time, type='note', note=message.note, velocity=velocity, sustain=sustain)
            events.append(new_event)

    for i, event in enumerate(events):
        if event['velocity'] == 0:
            continue

    print(events)


if __name__ == '__main__':
    parse_midi('/ssd2/maestro/maestro-v1.0.0/2017/MIDI-Unprocessed_041_PIANO041_MID--AUDIO-split_07-06-17_Piano-e_1-01_wav--1.midi')

    pretty_midi.pretty_midi.MAX_TICK = 1e10

    mid = pretty_midi.PrettyMIDI('/ssd2/maestro/maestro-v1.0.0/2017/MIDI-Unprocessed_041_PIANO041_MID--AUDIO-split_07-06-17_Piano-e_1-01_wav--1.midi')

    print(mid.instruments[0].notes)