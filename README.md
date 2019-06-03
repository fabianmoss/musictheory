# Computational Musicology - an introduction

(formerly: musictheory - thoughts about an introduction for programmers)

**GENERAL NOTES:** 
- Overarching goal is to have an ACCESSIBLE introduction for musicologists with elementary understanding of a programming language such as Python or R. Requirement should be a sound understanding of how functions, loops, and conditionals work.
- Every chapter must have:
-- a very clear focus on one musicological question
-- one particular method to answer this question
-- a range of exercises (not always involving programming) 
-- and a list of relevant references

## 1 INTRODUCTION: What is CM?
- Description and relation to related fields
-- musicology
-- music theory
-- music information retrieval
-- music cognition
-- music psychology
- modeling (!!!) very important chapter, maybe deserves its own paragraph. Modeling as a form of question/hypothesis guided research as opposed to wild tool application (''We did machine learning!'')
- How to do CM? conferences, journals, twitter, GitHub repositories, libraries
- which language to use? Matlab, R, Python, Julia...

## 2 REPRESENTATIONS AND FORMATS
(This part could e.g. feature (algorithmic) composition exercises)
1. Notes: pitches / pitch classes / pitch class sets / GISs / MIDI
2. Scores:  (MEI, music21, MusicXML, \*\*kern)
3. Chords (symbolic)

## 3 MUSIC MODELS
1. n-gram models (melody)
2. HMMs (harmony)
3. CFGs (form; choro)
4.  more advanced models

## 4 STYLE (classification)
- feature clustering (k-means, PCA, ...)

## 5 HISTORY (regression)
- trends (maybe with a non note-based dataset e.g. metadata)

## Further notes (old)
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
