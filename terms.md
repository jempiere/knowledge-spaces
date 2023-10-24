- Item: problem type, can be represented by a learning outcome (q in Q)
- \*\*Singleton: A set within a knowledge structure containing one Item
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
- QUERY: A question asked to an expert as: 'Does failing all of Z imply failing q' where Z subsets Q and Q contains q (X=Q)
- Positive Relation: P(Atom a,Atom b) describes a positive QUERY response (fancy P)
  - Failing Atom a implies failing Atom b.
  - Implies a directed edge from Atom a to Atom b (a is prerequisite to b)
  - Mutually exclusive with fancy N
- Negative Relation: N(Atom a, Atom b) describes a negative QUERY response (fancy N)
  - Implies Atom a and Atom b can be learned independently (a is not prerequisite to b)


\*\* See Jean-Paul Doignon & Mathieu Koppen, 1990 (query_alternative), 327-328
