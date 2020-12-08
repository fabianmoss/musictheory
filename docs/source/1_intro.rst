Introduction
------------


What is CM?
~~~~~~~~~~~

- Description and relation to related fields
  -- musicology
  -- music theory
  -- music information retrieval
  -- music cognition
  -- music psychology
- modeling (!!!) very important chapter, maybe deserves its own paragraph. Modeling as a form of question/hypothesis guided research as opposed to wild tool application (''We did machine learning!'')
- How to do CM? conferences, journals, twitter, GitHub repositories, libraries
- which language to use? Matlab, R, Python, Julia...

- Music as the "missing Humboldt system" (Merker, 2002) with its "orthogonal discretization of spectro-temporal space" (Merker, 2002:4)

Quickstart
~~~~~~~~~~

.. warning::

   These instructions do not work yet. 

To install the Python library ``musictheory``, type the following in your terminal:

.. code-block:: bash

    pip install musictheory

Notes
~~~~~~~~~~~~~

- Overarching goal is to have an ACCESSIBLE introduction for musicologists with elementary understanding of a programming language such as Python or R. Requirement should be a sound understanding of how functions, loops, and conditionals work.
- Every chapter must have:
  -- a very clear focus on one musicological question
  -- one particular method to answer this question
  -- a range of exercises (not always involving programming, also listening and composing)
  -- and a list of relevant references
- the algorithms/methods used in each chapter should be one of the most basic instances of a class of methods. The point is not to have the best classifier, the best dimensionality reduction, the best regression model etc. but rather to understand the class of problems that we are dealing with. Thinking in these abstract problem classes helps to recognize and understand the nature of other problems more easily.


General structure:

- Theory (axiomatic, consistent, implemented framework)
- History (expressing different "theories")
- Analysis (using the library for music analysis, wide variety of musics)

Old:

General remark: Create excercises with listening, composing and analyzing tasks.

- Sounds in the external world
- Perception, constraints (e.g. audible range)
- discretization
  - Musical Universals (3-7 note scales)
  - allows symbolic representation
- scales (independent from tuning/temperament): collections of pitches
- members of scale: notes
  - neighborness
  - Schenkerian terms: neighbor notes
  - pitch classes
  - pitch class sets
- intervals
  - counterpoint
  - consonance / dissonance
  - interval classes
  - interval class vectors
- special pitch class sets: chords
  - Triads
  - Euler space
  - tonnetz
  - seventh chords

- notes in time: durations, rhythm
  - Schenkerian terms: passing notes
  - cognitive framework: meter
  - metrical hierarchies

- visualisations (pitch-time plots)
  - pianoroll
  - MIDI
  - modern Western notation
  - different keys (not only treble and bass)

Related work
~~~~~~~~~~~~~~~~

Books 
+++++

This project is inspired by a number of great books, e.g.

* Aldwell & Schachter (2010). *Harmony and Voice Leading*.
* Cadwallader & Gagné (1998). *Analysis of Tonal Music. A Schenkerian Approach*.
* Forte (1977). *The Structure of Atonal Music*.
* Lewin (1987). *Generalized Intervals and Transformations*.
* Müller (2015). *Fundamentals of Music Processing*.
* Straus (2005). *Introduction to Post-Tonal Theory*.

What is new and unique about the approach taken here is that we take 
a computational perspective and implement all introduced concepts.
This does not only provide us with sharp and unequivocal definitions,
but also allows us to scale music theory up from the analysis of individual 
bars, sections, or pieces to that of entire repertoires and corpora!

Libraries 
+++++++++

.. rubric:: music21

`music21`_, developed by **Mike Cuthbert** at MIT, is 
a very popular and powerful Python library for 
computational applications in music theory.

TBC...

.. _`music21`: https://web.mit.edu/music21/

.. rubric:: Music for Geeks and Nerds and pyknon

I recently also discovered `Music for Geeks and Nerds`_ by **Pedro Kroger**
which looks very interesting. It is based on `pyknon`_, a library for creating
MIDI files.

.. _`Music for Geeks and Nerds`: https://pedrokroger.net/mfgan/
.. _`pyknon`: http://kroger.github.io/pyknon/

.. rubric:: musthe

The Python project `musthe`_ also seems to pursue a similar goal and 
deals with basic musical objects, such as notes, chords, and scales.
Its basic functionality is similar to the approach taken here, but its 
scope is limited because it fundamentally builds on the chromatic scale
as the basic representation of notes. 

The project presented here is more general then the latter two
in that it builds tones and their relations from the perspective of interval 
ratios. The chromatic scale is thus just one of many options.

.. _`musthe`: https://github.com/gciruelos/musthe

Developed by **Gonzalo Ciruelos**

.. rubric:: mingus

`mingus`_ by **Bart Spaans**

.. _`mingus`: https://bspaans.github.io/python-mingus/

.. rubric:: musictheory 

Developed by Peter Murphy.

https://pypi.org/project/musictheory/

Acknowledgements
~~~~~~~~~~~~~~~~

- DCML