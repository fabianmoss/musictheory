Fundamentals
============

.. module:: musictheory

The theory presented in here can be described as a *tonal theory* in the sense 
that its most fundamental objects are *tones*, discrete musical entities that have
a certain location in tonal space. 
A tonal space is then a metrical space describing all possible tone locations,
and the metric is given by an *interval function* between the tones. Note that by this definition,
there are as many different tonal spaces as there are interval functions.

While many aspects and examples will be taken 
from Western (classical) music, the theory is in principle not restricted to this 
tradition but extends well to virtually all musical cultures where a tone is a meaningful concept.

Tones
-----

Let's start with a mental exercise: imagine a tone.
Contemplate for a while what this means.
Does this tone have a pitch? A duration? A velocity (volume)?

* Riemann (1916). *Ideen zu einer Lehre von den Tonvorstellungen*:

"The ultimate elements of the tonal imagination are single tones." (Wason & Martin, 1992, 92)

Bearing that in mind, let's create (or *instantiate*) a tone. To do so, we need to 
conceptualize ("vorstellen" in Riemann's terminology) a *tone location* ("Tonort", Mazzola 1985, 241).
There are many different ways to do this. In fact, the way we specify the location of a tone 
defines the tonal space in which it is situated.

Euler Space 
~~~~~~~~~~~

One option is to locate a tone `t` as a point :math:`p=(o, q, t)` in Euler Space, defined by
a number of octaves `o`, fifths `q`, and thirds `t`. We will use the :class:`musictheory.Tone`
class for this

.. code-block:: python

   from musictheory import Tone

   t = Tone(octave=0, fifth=0, third=0)

Printing this tone will give us the common name.

.. code-block:: python

   t
   >>> Tone(C)

A shorter way to initialize a tone is by just passing a triple to the class:

.. code::

   g = Tone(0,1,0)
   >>> Tone(G)

From this representation we can derive a variety of others, corrsponding to transformations of 
tonal space.

Frequencies
~~~~~~~~~~~

Each tone corresponds to some *fundamental frequency* :math:`f` in Hertz (Hz),
oscillations per second.

- Overtone series
- frequency ratios 
- logarithm: multiplication => addition

The frequency of a tone can be accessed via the :py:meth:`Tone.get_frequency()` method.
attribute:

.. code-block:: python

   t.get_frequency()
   >>> 261.63

Octave equivalence
~~~~~~~~~~~~~~~~~~

Octave equivalance considers all tones to be equivalent that are separated by one or
multiple octaves, e.g C1, C2, C4, C10 etc. More precisely, all tones whose fundamental frequencies
are related by multiples of 2 are octave equivalent.

Tonnetz
~~~~~~~

The *Tonnetz* does not contain octaves and thus corresponds to a projection 

.. math::
   
   \pi: (o, q, t) \mapsto (q, t).

Pitch classes
-------------

A very common object in music theory is that of a *pitch class*. Pitch classes
are equivalence classes of tones that incorporate some kind of invariance.
The two most common equivalences are *octave equivalence* and *enharmonic equivalence*.


Enharmonic equivalence
~~~~~~~~~~~~~~~~~~~~~~

If, in addition to octave equivalence, one further assumes enharmonic equivalence, 
all tones separated by 12 fifths on the line of fifths
are considered to be equivalent, e.g. :math:`\text{A}\sharp` and :math:`\text{B}\flat`, 
:math:`\text{F}\sharp` and :math:`\text{G}\flat`, :math:`\text{G}\sharp`, and :math:`\text{A}\flat` etc.

The notion of a pitch class usually entails both octave and enharmonic equivalence.
Consequently, there are twelve pitch classes. If not mentioned otherwise, we adopt this convention here.
The twelve pitch classes are usually referred to by their most simple representatives, i.e.

.. math::
   \text{C, C$\sharp$, D, E$\flat$, F, F$\sharp$, G, A$\flat$, A, B$\flat$, B},

but it is more appropriate to use *integer notation* in which each pitch class is represented
by an integer :math:`k \in \mathbb{Z}_{12}`.

.. math::
   \mathbb{Z}_{12}=\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11\},

and usually one sets :math:`0\equiv \text{C}`. This allows to use *modular arithmetic*
do calculations with pitch classes.

Other invariances
~~~~~~~~~~~~~~~~~

OPTIC

Tuning / Temperament
~~~~~~~~~~~~~~~~~~~~~~~

Intervals
---------

We can add an interval to a tone:

.. code::

   >>> t = Tone(0,1,0) # G 
   
   >>> f = Tone(0,-1,0) # F 
   >>> a = Tone(0,-1,1) # A 
   >>> i = Interval(f,a) # +M3

   >>> t + i 
   B 

Analogously, we can also substract an interval from a tone: 

.. code::

   >>> t - i
   Eb

Moreover, we can add or substract intervals from each other: 

.. code::

   >>>j = Interval(a, f) # +m6
   >>> i + j 
   P8 

   >>> i - j 
   -A4

- Pitch intervals
- Ordered pitch-class intervals (-> rather directed)
- Unordered pitch-class intervals
- Interval classes
- Interval-class content
- Interval-class vector

GISs
~~~~

Pitch-Class Sets
----------------

Let :math:`y=\{y_1,\ldots,y_m\}` be a pitch-class set. 

- Sets that contain pitch classes
- ordered: {0,4,7}
- unordered: {7,0,4}

Normal Form 
~~~~~~~~~~~

- smallest difference between last and first element
- (see algorithm in Straus,2005)

Transposition
~~~~~~~~~~~~~

transposition: adding n to each pc (mod 12)

- {0,4,7} + 7 = {7,11,14} = {7,11,2}

The *transposition* of a pitch-class set `y` by `n` semitones is given by

.. math::
   T_n(y) &= y + n\mod~12\\ 
          &= \{y_1 + n\mod~12, \ldots, y_m + n\mod~12\}

Inversion
~~~~~~~~~

inversion: reversing the sign of each pc (mod 12)

- [0,4,7] => [0,-4,-7] = [0,8,5]

The *inversion* of a pitch-class set `y` is given by 

.. math::
   I(y) &= -y\mod~12 \\ 
        &= \{-y_1\mod~12, \ldots,-y_m\mod~12\}


- Inversion In, Ixy

.. note::
   Note that this definition is an entirely different concept
   than *chord inversion* with which we will deal in later chapters.

Index number 
~~~~~~~~~~~~

- Forte numbers: <cardinal number>-<ordinal number>

- ordinal number is position on the list
- [0,1,3,6,9] => 5-31


Set Class
~~~~~~~~~

Prime Form 
~~~~~~~~~~

- 0 is first entry
- 220 different pc sets in prime form (equivalence by transposition or inversion)


Transformations between representations of tones are actually *transformations of tonal space*.

[Diagram of relations between different representations.]

Western tonal music
-------------------

The diatonic scale
~~~~~~~~~~~~~~~~~~

Music in the Western tradition fundamentally builds on
so-called *diatonic* scales, an arrangement of seven tones
that are named with latin letters from A to G. "Diatonic" can 
be roughly translated into "through all tones". Within this scale,
no tone is privileged, so the diatonic scale can be appropriately 
represented by a circle with seven points on it. Mathemacally, 
this structure is equivalent to :math:`\mathbb{Z}_7`.

[tikz figure here]

Now, if we want to determine the relative relations between the tones, 
it is necessary to assign a reference tone that is commonly called the *tonic*, 
or *finalis* in older music.

For example, if the tone D is the tonic, we can determine all other scale degrees 
as distance to this tone. Scale degrees are commonly notated with arabic numbers with a caret:

.. math::
   \text{D}: \hat{1}\\
   \text{E}: \hat{2}\\
   \text{F}: \hat{3}\\
   \text{G}: \hat{4}\\
   \text{A}: \hat{5}\\
   \text{B}: \hat{6}\\
   \text{C}: \hat{7}\\

Modes
~~~~~

scale plus order plus hierarchy (but order already defined above?)

Keys
~~~~

Other scales
~~~~~~~~~~~~

- chromatic
- hexatonic
- octatonic
- whole tone

Time
----

Notes
~~~~~

(Tones + Duration)
blablabla...

.. Sinve the relations between tones only given by 
   their location in tonal space (and the interval function)
   generalizing the notion of neighbor notes etc. corresponds
   to changing what the *lines* in Western notation mean.
   Traditionally, two lines separate tones that are a generic third apart.
   But there have been other representations. 
   For instance, the first attempts of Guido separated notes by steps.
   Let's reinterpret the lines as seconds and fifths. 
   There have also been a number of attempts to develop a fully chromatic
   notation system (Parncutt).


Rhythm
~~~~~~

(Duration patterns)

Meter
~~~~~

(Hierarchy)

Musical time vs. performance time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notes on Segmentation
---------------------

- Straus 2005
- Hanninen 2012