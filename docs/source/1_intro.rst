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

Acknowledgements
~~~~~~~~~~~~~~~~

- DCML