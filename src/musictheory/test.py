from musictheory import Tone, Interval
import numpy as np

if __name__ == "__main__":
    c = Tone(0,0,0)
    s = Tone(1,-1,1) 
    t = Tone(0,2,0) 
    i = Interval(source=c,target=s)
    j = Interval(source=c, target=t)
    
    print(i.get_frequency_ratio())

    # print(c + j, c - j)
    # print(i+j, i-j)
    # print(i.get_frequency_ratio())
    # print(i.frequency_ratio)

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