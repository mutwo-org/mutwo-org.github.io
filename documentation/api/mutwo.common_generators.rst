
mutwo.common_generators
=======================

.. contents:: Table of content
   :depth: 3

.. automodule:: mutwo.common_generators
   :members:


.. list-table::
   :width: 95%
   :header-rows: 1

   * - Object
     - Documentation
   * - :class:`mutwo.common_generators.random_walk_noise`
     - Generate an instance of Brownian motion (i.e. the Wiener process).
   * - :class:`mutwo.common_generators.make_bruns_euclidean_algorithm_generator`
     - Make generator which runs Bruns adaption of the Euclidean algorithm.
   * - :class:`mutwo.common_generators.NonTerminal`
     - Can be used as a Mixin to define context-free grammar.
   * - :class:`mutwo.common_generators.Terminal`
     - Can be used as a Mixin to define context-free grammar.
   * - :class:`mutwo.common_generators.ContextFreeGrammarRule`
     - Describe a context_free_grammar_rule for a :class:`ContextFreeGrammar`
   * - :class:`mutwo.common_generators.ContextFreeGrammar`
     - Describe a context-free grammar and resolve non-terminals
   * - :class:`mutwo.common_generators.ActivityLevel`
     - Python implementation of Michael Edwards activity level algorithm.
   * - :class:`mutwo.common_generators.reflected_binary_code`
     - Make gray code where each tuple has `length` items with `modulus` different numbers.
   * - :class:`mutwo.common_generators.Tendency`
     - Tendency offers an interface for dynamically changing minima / maxima areas.
   * - :class:`mutwo.common_generators.Backtracking`
     - Abstract base class to implement a backtracking algorithm
   * - :class:`mutwo.common_generators.IndexBasedBacktracking`
     - Abstract base class for index based backtracking algorithms
   * - :class:`mutwo.common_generators.euclidean`
     - Return euclidean rhythm as described in a 2005 paper by G. T. Toussaint.
   * - :class:`mutwo.common_generators.paradiddle`
     - Generates rhythm using the paradiddle method described by G. T. Toussaint.
   * - :class:`mutwo.common_generators.alternating_hands`
     - Generates rhythm using the alternating hands method described by G. T. Toussaint.




.. autofunction:: random_walk_noise
    


.. autofunction:: make_bruns_euclidean_algorithm_generator
    


.. autofunction:: reflected_binary_code
    


.. autofunction:: euclidean
    


.. autofunction:: paradiddle
    


.. autofunction:: alternating_hands
    

.. autoclass:: NonTerminal
        .. autoclasstoc::
    

.. autoclass:: Terminal
        .. autoclasstoc::
    

.. autoclass:: ContextFreeGrammarRule
        .. autoclasstoc::
    

.. autoclass:: ContextFreeGrammar
        .. autoclasstoc::
    

.. autoclass:: ActivityLevel
        .. autoclasstoc::
    

.. autoclass:: Tendency
        .. autoclasstoc::
    

.. autoclass:: Backtracking
        .. autoclasstoc::
    

.. autoclass:: IndexBasedBacktracking
        .. autoclasstoc::
    


mutwo.common_generators.constants
---------------------------------

.. automodule:: mutwo.common_generators.constants
   :members:

