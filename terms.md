- Item: problem type, can be represented by a learning outcome (q in Q)
- domain: set of items in a course (Q)
- knowledge state: set of learned items (K)
- knowledge structure: domain with the tree of dependencies for the states (fancy K)
- Knowledge Space: a structure that is closed under union
    - well-graded: for each pair of knowledge states, to go from one state to
      the next, you only add one item
- Atom: the smallest state for a particular item q (definition 12), i.e., the
  state at which a student learns q
- Single-item atom: an atom with a single item, the first items to learn (kinda
  like hydrogen)
- Base: the minmal set of atoms to form a complete knowledge space
- \*inner fringe: the most recently previous state a student was in
- \*outer fringe: the set of states to which a student can go next
- Hanging state: a state whose inner fringe is empty (definition 39)
- Learning Space: A finite knowledge space with no hanging states (theorem 41)
