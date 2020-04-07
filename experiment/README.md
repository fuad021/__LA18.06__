### Experiment Design 0: Finding the number of vectors in xyz space that can have all negative dot product

#### Idea:

Introduction to Linear Algebra by Gilbert Strang, 4e, page 21, Problem Set 1.2 (28)

#### Algorithm:

1. Generate a list of vector pair in xyz space that yeilds negative dot product (ndp).
2. Find any other vector in that list or randomly generated that yeild ndp to vector pairs.
3. Iteratively find the number of vectors possible in space that yeild ndp with each other.

#### Conclusion:

1. 4 vectors can be found such that they have ndp wrt every other vectors in that set in xyz space. [I've found 86K vector quadruples in range -500 to 500].
2. <strong>Hypothesis: n-1 vectors can be found in n-d space.</strong>
