- Item: problem type, can be represented by a learning outcome
- domain: set of items in a course
- knowledge state: set of learned items
- knowledge structure: domain with the tree of dependencies for the states
- Knowledge Space: a structure that is closed under union
    - well-graded: for each pair of knowledge states, to go from one state to
      the next, you only add one item
- Atom: the smallest state for a particular item q (definition 12), i.e., the
  state at which a student learns q
- Base: the minmal set of atoms to form a complete knowledge space
- Learning Space:
- \*inner fringe: the most recently previous state a student was in
- \*outer fringe: the set of states to which a student can go next
