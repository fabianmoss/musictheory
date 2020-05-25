"""
.. module:: musictheory
    :synopsis: a python module for music theory
 
.. moduleauthor:: Fabian C. Moss <fabianmoss@gmail.com>
"""

import numpy as np
import re
from fractions import Fraction

def UnsupportedOperands(op, type1, type2):
    def as_type(x):
        return x if isinstance(x, type) else type(x)

    fmt = "unsupported operand type(s) for {}: '{}' and '{}'"
    type1 = as_type(type1)
    type2 = as_type(type2)
    return TypeError(fmt.format(op, type1.__name__, type2.__name__))

class Interval:
    """ Class for an interval between two tones `s` (source) and `t` (target). """
    def __init__(self, source, target):
        self.source = source
        self.target = target

        self.euler_coordinate = self.target.euler_coordinate - self.source.euler_coordinate
        self.generic_interval = self.get_generic_interval()
        self.specific_interval = self.get_specific_interval()
        self.euclidean_distance = self.get_euclidean_distance()
        self.interval_name = self.get_interval_name()
        self.frequency_ratio = self.get_frequency_ratio()

    def get_euclidean_distance(self, precision=2):
        '''
        Calculates the Euclidean distance between two tones
        with coordinates in Euler space.

        Args:
            precision (int): Rounding precision.
            
        Returns:
            float: The Euclidean distance between two tones `s` (source) and `t` (target).        

        Example:
            >>> s = Tone(0,0,0) # C_0
            >>> t = Tone(1,2,1) # D\'1
            >>> i = Interval(s,t)
            >>> i.get_euclidean_distance()
            2.45
        '''
        s = np.asarray(self.source.euler_coordinate)
        t = np.asarray(self.target.euler_coordinate)
        return round(np.linalg.norm(t - s), precision)

    def get_generic_interval(self, directed=True, octaves=True):
        """
        Generic interval (directed) between two tones.

        Parameters:
            directed (bool): Affects whether the returned interval is directed or not.

            octaves (bool): returns generic interval class if `False`.

        Returns:
            int: (Directed) generic interval from `s` to `t`.

        Example:
            >>> db = Tone(0,-1,-1) # Db,0
            >>> b = Tone(0,1,1) # B'0
            >>> i1 = Interval(db, b) # the interval between Db0 and B1 is an ascending thirteenth
            >>> i1.generic_interval()
            13

            >>> i2 = Interval(b, db) # the interval between B1 and Db0 is a descending thirteenth
            >>> i2.generic_interval()
            -13

            >>> i3 = Interval(b, db) # the interval between B1 and Db0 is a descending thirteenth
            >>> i3.generic_interval(directed=False)
            13
        """
        g = 7 * self.euler_coordinate[0] + 4 * self.euler_coordinate[1] + 2 * self.euler_coordinate[2]
        
        if not octaves:
            g = g % 12

        if directed:
            
            if g > 0:
                return g + 1
            elif g < 0:
                return g - 1
            else:
                return 1
        else:
            return np.abs(g)

    def get_frequency_ratio(self):
        """Frequency ratio of the interval.
        Needs :py:class:`fractions.Fraction` class.

        Returns:
            Frac -- Integer ratio of the interval.
        """

        num = Fraction(2, 1) ** self.target.euler_coordinate[0] * \
              Fraction(3, 2) ** self.target.euler_coordinate[1] * \
              Fraction(5, 4) ** self.target.euler_coordinate[2]

        den = Fraction(2, 1) ** self.source.euler_coordinate[0] * \
            Fraction(3, 2) ** self.source.euler_coordinate[1] * \
            Fraction(5, 4) ** self.source.euler_coordinate[2]

        return Fraction(num, den)

        # Remove greatest common divisor:
        # common_divisor = gcd(numer, denom)
        # (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
        
        # return np.gcd.reduce(num, den) #Fraction(num, den)
    
    def get_specific_interval(self, directed=True, octaves=True):
        """
        Specific interval (directed) between two tones.

        Parameters:
            directed (bool): Affects whether the returned interval is directed or not.

            octaves (bool): returns specific interval class if `False`.

        Returns:
            int: (Directed) specific interval from `s` to `t`.

        Example:
            >>> fs = Tone(0,2,1) # F#'0
            >>> db = Tone(0,-1,-1) # Db,0
            >>> i1 = Interval(fs, db) 
            >>> i1.specific_interval()
            17

            >>> i1.specific_interval(octaves=False)
            5

        """
        s = (12 * self.euler_coordinate[0]) + 7 * (self.euler_coordinate[1] % 12) + (4 * self.euler_coordinate[2] % 12)
        if not octaves:
            s = s % 12

        if directed:
            return s
        else: 
            return np.abs(s)

    def get_interval_name(self, directed=True):
        if directed:
            g = self.get_generic_interval(octaves=True)
            if g < 0:
                direction = "-"
            elif g > 0:
                direction = "+"
            # elif g == 0:
            #     direction = "" # does this make sense? => what is the difference between +P1 and -P1?
                ## P1 is the neutral element of the interval group! Directed intervals must be signed!
        else:
            direction = ""
        quality = "Q"
        size = str(np.abs(self.get_generic_interval(octaves=True)))

        name = direction + quality + size
        return name

    def __repr__(self):
        return f"Interval({self.interval_name})"

    def __str__(self):
        return self.interval_name

    def __add__(self, other):
        if isinstance(other, Interval):
            return Interval(Tone(0,0,0), Tone(*(self.euler_coordinate + other.euler_coordinate)))
        else:
            raise UnsupportedOperands('+', self, other)

    def __sub__(self, other):
        if isinstance(other, Interval):
            return Interval(Tone(0,0,0), Tone(*(self.euler_coordinate - other.euler_coordinate)))
        else:
            raise UnsupportedOperands('-', self, other)
        
class Tone:
    """ Class for tones. """

    diatonic = np.array(list("FCGDAEB"))
    accidentals = ["#", "b"]

    def __init__(self, octave=None, fifth=None, third=None, name=None):
        # coordinates
        self.octave = octave
        self.fifth = fifth
        self.third = third
        self.euler_coordinate = np.asarray((self.octave, self.fifth, self.third))
        self.fifths_pos = self.fifth + 4 * self.third

        # parts and name
        self.accidentals = self.get_accidentals()
        self.step = self.get_step()
        self.syntonic = self.get_syntonic()
        self.name = self.get_name()

        # other representations
        self.midi_pitch = self.get_midi_pitch()
        self.frequency = self.get_frequency()
        self.pitch_class = self.get_pitch_class()

    def get_accidentals(self):
        '''
        Gets the accidentals of the tone (flats (:math:`\\flat`) or sharps (:math:`\\sharp`))..

        Args:
            None

        Returns:
            str: The accidentals of the tone.

        Example:
            >>> t = Tone(0,7,0) # C sharp
            >>> t.get_accidentals()
            `#`
        '''
        accs = np.divmod(self.fifths_pos + 1, 7)[0] # shift 0 to "C"
        return np.abs(accs) * "b" if accs < 0 else np.abs(accs) * "#"

    def get_frequency(self, chamber_tone=440.0, precision=2):
        '''
        Get the frequency of the tone.

        Args:
            chamber_tone (float): The frequency in Hz of the chamber tone. Default: 440.0 (A)
            precision (int): Rounding precision.

        Returns:
            float: The frequency of the tone in Hertz (Hz).

        Example:
            >>> t = Tone(0,0,0)
            >>> t.get_frequency(precision=3)
            261.626
        '''
        f = chamber_tone * 2 ** ((self.midi_pitch - 69)/12)
        return round(f, precision)

    def get_name(self):
        '''
        Gets the complete name of the tone, consisting of its step, syntonic position, and octave.

        Args:
            None

        Returns:
            str: The accidentals of the tone.

        Example:
            >>> c = Tone(0,0,0)
            >>> ab = Tone(0,1,-1)
            >>> c.get_name(), ab.get_name()
            `C_0` `Ab,1`

        '''
        return self.step + self.accidentals + self.syntonic + str(self.octave)

    def get_midi_pitch(self):
        '''Get the MIDI pitch of the tone.

        Args:
            None

        Returns:
            int: The MIDI pitch of the tone if it is in MIDI pitch range (0--128)

        Example:
            >>> t = Tone(0,0,0)
            >>> t.get_midi_pitch()
            60
        '''
        m = 60 + 12 * self.octave + 7 * self.fifth + 4 * self.third

        if m in range(0,128):
            return m
        else:
            print("Outside of MIDI range.")
    
    def get_pitch_class(self, start=0, order="chromatic"):
        '''Get the pitch-class number on the circle of fifths or the chromatic circle.

        Args:
            start (int): Pitch-class number that gets mapped to C (default: 0).
            order (str): Return pitch-class number on the chromatic circle (default) or the circle of fifths.

        Returns:
            int: The pitch class of the tone on the circle of fifths or the chromatic circle.

        Example:
            >>> t = Tone(0,7,0) # C sharp
            >>> t.get_pitch_class(order="chromatic")
            1

            >>> t = Tone(0,7,0) # C sharp
            >>> t.get_pitch_class(order="fifths")
            7
        '''
        if order == "chromatic":
            return ((self.fifths_pos % 12) * 7) % 12
        elif order == "fifths":
            return start + self.fifths_pos % 12
        else:
            raise f"`order` was given a wrong keyword: {order}. Use `chromatic` or `fifths`."

    def get_step(self):
        '''
        Gets the diatonic letter name (C, D, E, F, G, A, or B) of the tone *without* accidentals.

        Args:
            None

        Returns:
            str: The diatonic step of the tone.

        Example:
            >>> t = Tone(0,7,0) # C sharp
            >>> t.get_step()
            `C`
        '''
        return self.diatonic[ (np.divmod(self.fifths_pos, 7)[1] + 1) % 7 ] # shift 0 to "C"

    def get_syntonic(self):
        '''
        Gets the value of the syntonic level in Euler space. 
        Tones on the same syntonic line as central C are marked with `_`,
        and those above or below this line with `'` or `,`, respectively.

        Args:
            None

        Returns:
            int: The number of thirds above or below the central C.

        Example:
            >>> e1 = Tone(0,4,0) # Pythagorean major third above C
            >>> e2 = Tone(0,0,1) # Just major third above C
            >>> e3 = Tone(0,8,-1) # Just major third below G sharp
            >>> e1.get_syntonic(), e2.get_syntonic(), e3.get_syntonic()
            `'` `_` `,`
            
        '''
        return self.third * "\'" if self.third > 0 else (np.abs(self.third) * "," if self.third < 0 else "_")

    def __repr__(self):
        return f"Tone({self.step + self.accidentals + str(self.octave) + self.syntonic})"

    def __str__(self):
        return self.step + self.accidentals + str(self.octave) + self.syntonic

    def __add__(self, other):
        if isinstance(other, Interval):
            return Tone(*(self.euler_coordinate + other.euler_coordinate))
        else:
            raise UnsupportedOperands('+', self, other)

    def __sub__(self, other):
        if isinstance(other, Interval):
            return Tone(*(self.euler_coordinate - other.euler_coordinate))
        else:
            raise UnsupportedOperands('-', self, other)

    # def get_pitch_class_chromatic(self, start=0):
    #     '''Get the pitch class on the tone on the chromatic circle.

    #     Args:
    #         start (int): Tone that that gets mapped to 0 (default: C=0).

    #     Returns:
    #         int: The pitch class of the tone on the chromatic circle.

    #     Example:
    #         >>> t = Tone(0,7,0) # C sharp
    #         >>> t.get_pitch_class_chromatic()
    #         7
    #     '''
    #     return ((self.fifths_pos % 12) * 7) % 12
    

    # def get_coordinates(self):
    #     match = re.match("([A-G]#*|b*)(,*|'*)\d", self.name)
    #     self.step = match[0]
    #     self.accidentals = match[1]
    #     self.syntonic = match[2]
    #     self.octave = match[3]

    # if all(v is not None for v in [self.octave, self.fifth, self.third, self.name]):
    #     assert self.name == self.inferred_name

class PitchClass(Tone):
    """Pitch class instance in :math:`\mathbb{Z}_{12}`."""
    def ___init___(self):
        self.pitch_class = self.get_pitch_class()

class PitchClassSet(Tone):
    """Pitch class sets"""
    def ___init___(self, lst):
        self.size = len(self.lst)

    def interval_vector(self):
        """
        Interval vector given a pitch-class set.
        """
        iv = ()
        return iv