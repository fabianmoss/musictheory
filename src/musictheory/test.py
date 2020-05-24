from musictheory import Tone, Interval
import numpy as np

if __name__ == "__main__":
    s = Tone(0,-1,-1) # C_0
    t = Tone(0,2,1) # F#'0
    c = Tone(0,0,0)
    i = Interval(source=c,target=s)
    j = Interval(source=s, target=t)
    
    t + i


    # print(s.label, t.label)
    # print(i.interval)
    # print(i.get_specific_interval(octaves=True))

    # print(t.pitch_class_chromatic)
    # print(s.pitch_class_fifths)
    # print(s.midi_pitch, t.midi_pitch)
    # print(s.frequency,t.frequency)
    # print(c.get_frequency(precision=3))

    # print(s.accidentals)
    # print(s.step)
    
    # s = Tone(0,8,-1)
    # print(s.label)

    # print(i.euclidean_distance)

    # print(s.euler_coordinate)
    # print(t.euler_coordinate)
    # print(i.source.euler_coordinate)
    # print(i.interval)
    # print(i.euclidean_distance())