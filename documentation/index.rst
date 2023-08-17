.. mutwo documentation master file, created by
   sphinx-quickstart on Wed Feb  3 23:07:56 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to mutwos documentation!
=================================

**Mutwo** is a flexible, event based framework for composing music or other time-based arts in Python.
It aims to help composers to build musical structures in a meaningful way and translate those structures to different third party objects (e.g. midi files, `csound <http://www.csounds.com/>`_ scores, musical notation with `Lilypond <https://lilypond.org/>`_ via `Abjad <https://github.com/Abjad/abjad>`_).
The general design philosophy stresses out the independence and freedom of the user with the help of generic data structures and an easily extensible and tweakable software design.

**Features**:

- generalized model to describe & generate musical (or any other time-based) structures
- export & import MIDI files
- export to musical notation
- create sound files by writing & rendering csound scores
- builtin support for microtonality
- hackable: designed with a high focus on extendability & flexibility
- fully open source & not related to any big institution

Why *mutwo*?
############

There already exist many similar :ref:`alternatives` projects, so why would we need another one?
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

It's fascinating to see how many computer-assisted composition framework exist (and existed) within the not-so-long history of computer-assisted composition.
A lot of musicians create their own system that they use for themselves, accompanied by a mostly small circle of similar-minded people (who are perhaps the musicians students).
In my understanding there are mainly two reasons for this high variety:

1. Nowadays composers often have a very individualistic and idiosyncratic way how to think and how to compose the music. They tend to take their specific way as the starting point for their composition tools, which is why these tools become extremely specialised - & therefore useless for anyone else with any different approach.

2. On the other hand, if systems are more broad, they aren't broad enough and miss the possibility to express specificness within them, which is why them become useless again for someone who wants to express her/his/* idiosyncratic thinking.

*Mutwo* is deliberately boring and unobtrusive.
It doesn't offer an innovative composition interface nor does it provide shiny ideas how to find wonderful music.
Conversely *mutwo* aims to provide a minimal common ground onto which anyone could build her/his/* preferred model of thinking.
This *anyone* explicitly includes practices that aren't built upon the Western music tradition, but which may be based on Non-European traditions.
In this way *mutwo* aims to commit its tiny part to the massive task of `decolonizing music technology <https://pitchfork.com/thepitch/decolonizing-electronic-music-starts-with-its-software/>`_.
While *mutwo* lacks the actual representations that may be needed for a specific tradition (& this also includes the various traditions in experimental music), it provides the groundwork to add these representations.
Once these representations are added, they can be used within *mutwos* ecosystem of small, useful, practical functionalities.
*Mutwo* wants to join the utopian hope for a more neutral, unbiased technology.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   quickstart
   installation
   events
   parameters
   converters
   generators
   overview
   cookbook
   api/api_documentation
   license
   alternatives


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
