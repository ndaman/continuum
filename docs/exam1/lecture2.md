# AE831
## Continuum Mechanics
Lecture 2 - Tensor Algebra<br/>
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering

August 20, 2020

----

## schedule

- 20 Aug - Tensor Algebra
- 25 Aug - Tensor Calculus, HW1 Due
- 27 Aug - Material Derivative
- 1 Sep - Conservation and Compatibility, HW2 Due

----
## outline

<!-- vim-markdown-toc GFM -->

* symmetry
* transformation
* examples
* principal values
* invariants
* principal directions
* examples

<!-- vim-markdown-toc -->

---
# symmetry

----
## symmetry

- Symmetry can be a very powerful tool
- Here we define some useful forms of symmetry in index notation
- Symmetric
	- `\(a_{ij...z} = a_{z...ji}\)`
	- `\(a_{ij...m...n...z} = a_{ij...n...m...z}\)`
- Anti-symmetric (skew symmetric)
	- `\(a_{ij...z} = -a_{z...ji}\)`
	- `\(a_{ij...m...n...z} = -a_{ij...n...m...z}\)`

----
## symmetry

- Useful identity
	- If `\(a_{ij...m...n...k}\)` is symmetric in `\(mn\)` and `\(b_{pq...m...n...r}\)` is antisymmetric in `\(mn\)`, then the product is zero
`\[a_{ij...m...n...k}b_{pq...m...n...r} = 0\]`

- We can also write any tensor as the sum of its symmetric and anti-symmetric parts
`\[a_{ij} = \frac{1}{2} (a_{ij} + a_{ji}) + \frac{1}{2} (a_{ij} - a_{ji})\]`

- This textbook uses a special shortcut notation (S and A superscript) for the symmetric and anti-symmetric portions of a tensor

---

# transformation

----
## linear transformation

- Let us consider some transformation, `\(\textbf{T}\)`, which transforms any vector into another vector
- If we transform `\(\textbf{Ta} = c\)` and `\(\textbf{Tb} = d\)`
- We call `\(\textbf{T}\)` a linear transformation (and a tensor) if
`\[\begin{aligned}
	\textbf{T}(\textbf{a} + \textbf{b}) &= \textbf{Ta} + \textbf{Tb}\\
	\textbf{T}(\alpha \textbf{a}) = \alpha\textbf{Ta}
\end{aligned}\]`

- Where `\(\alpha\)` is any arbitrary scalar and `\(\textbf{a}\)`, `\(\textbf{b}\)` are arbitrary vectors

----
## 2d coordinate transformation 

![2d coordinate transformation example with vector pointing from (0,0) to (1,1)](../images/transform2d.svg)

----
## 2d coordinate transformation 

- The vector, `\(v\)`, remains fixed, but we transform our coordinate system
- In the new coordinate system, the `\(x_2^\prime\)` portion of `\(v\)` is zero.
- To transform the coordinate system, we first define some unit vectors.
- `\(\hat{e}_1\)` is a unit vector in the direction of `\(x_1\)`, while `\(\hat{e}_1^\prime\)` is a unit vector in the direction of `\(x_1^\prime\)`

----
## 2d coordinate transformation 

![2d coordinate transformation from previous figure with unit vectors drawn along the x and y axes](../images/transform2d-unit.svg)

----
## 2d coordinate transformation

- For this example, let us assume `\(v = \langle 2, 2 \rangle\)` and `\(\theta = 45^\circ\)`
- We can write the transformed unit vectors, `\(\hat{e}_1^\prime\)` and `\(\hat{e}_2^\prime\)` in terms of `\(\hat{e}_1\)`, `\(\hat{e}_2\)` and the angle of rotation, `\(\theta\)`. 
`\[\begin{aligned}
	\hat{e}_1^\prime &= \langle \hat{e}_1 \cos \theta , \hat{e}_2 \sin \theta\rangle\\
	\hat{e}_2^\prime &= \langle -\hat{e}_1 \sin \theta , \hat{e}_2 \cos \theta \rangle
\end{aligned}\]`

----
## 2d coordinate transformation 

- We can write the vector, `\(v\)`, in terms of the unit vectors describing our axis system
- `\(v = v_1 \hat{e}_1 + v_2 \hat{e}_2\)`
- (note: `\(\hat{e}_1=\langle 1, 0 \rangle\)` and `\(\hat{e}_2 = \langle 0,1 \rangle\)`)
- `\(v = \langle 2, 2 \rangle = 2 \langle 1, 0 \rangle + 2 \langle 0,1 \rangle\)`

----
## 2d coordinate transformation

- When expressed in the transformed coordinate system, we refer to `\(v^\prime\)`
- `\(v^\prime = \langle v_1 \cos \theta + v_2 \sin \theta, -v_1 \sin \theta + v_2 \cos \theta \rangle\)`
- `\(v^\prime = \langle 2\sqrt{2}, 0 \rangle\)`
- We can recover the original vector from the transformed coordinates:
- `\(v = v_1^\prime \hat{e}_1^\prime + v_2^\prime \hat{e}_2^\prime\)`

----
## 2d coordinate transformation

- note:
`\[\hat{e}_1^\prime=\langle \frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2} \rangle\]`
    and
`\[\hat{e}_2^\prime = \langle -\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2} \rangle\]`
- therefore
`\[v = 2\sqrt{2}\langle \frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2} \rangle, 0 \langle -\frac{\sqrt{2}}{2},\frac{\sqrt{2}}{2} \rangle = \langle 2, 2 \rangle\]`

----
## coordinate transformation

- Coordinate transformation can become much more complicated in three dimensions, and with higher-order tensors
- We define `\(Q_{ij}\)` as the cosine of the angle between the `\(x_i^\prime\)` axis and the `\(x_j\)` axis.

----
## coordinate transformation

- This is also referred to as the "direction cosine" `\[Q_{ij} = \cos (x_i^\prime, x_j)\]`
- *health warning* the direction cosine can also be defined inversely (`\(Q_{ij} =\cos (x_i, x_j^\prime)\)`), and the indexes are switched in the transformation law

----
## coordinate transformation

<div class="left" width="30%">

- We can use this form on our 2D transformation example

</div>

<div class="right" width="70%">

`\[\begin{aligned}
	Q_{ij} &= \cos (x_i^\prime, x_j)\\
	&= \begin{bmatrix}
	\cos (x_1^\prime, x_1) & \cos (x_1^\prime, x_2)\\
	\cos (x_2^\prime, x_1) & \cos (x_2^\prime, x_2)
	\end{bmatrix}\\
	&= \begin{bmatrix}
	\cos \theta & \cos (90-\theta)\\
	\cos (90+\theta) & \cos \theta
	\end{bmatrix} \\
	&= \begin{bmatrix}
	\cos \theta & \sin \theta \\
	-\sin \theta & \cos \theta
	\end{bmatrix}
\end{aligned}\]`

</div>

----
## coordinate transformation

- We can transform any-order tensor using `\(Q_{ij}\)`
- Vectors (first-order tensors): `\(v^\prime_i = Q_{ij}v_j\)`
- Matrices (second-order tensors):
`\[\sigma_{mn}^\prime =Q_{mi}Q_{nj}\sigma_{ij}\]`
- Fourth-order tensors:
`\[C_{ijkl}^\prime = Q_{im}Q_{jn}Q_{ko}Q_{lp}C_{mnop}\]`

----
## coordinate transformation

- We can similarly use `\(Q_{ij}\)` to find tensors in the original coordinate system
- Vectors (first-order tensors): `\(v_i = Q_{ji}v_j^\prime\)`
- Matrices (second-order tensors): `\(\sigma_{mn} =Q_{im}Q_{jn}\sigma_{ij}^\prime\)`
- Fourth-order tensors: `\(C_{ijkl} = Q_{mi}Q_{nj}Q_{ok}Q_{pl}C_{mnop}^\prime\)`

----
## coordinate transformation

- We can derive some interesting properties of the transformation tensor, `\(Q_{ij}\)`
- We know that `\(v_i = Q_{ji}v_j^\prime\)` and that `\(v^\prime_i = Q_{ij}v_j\)`
- If we substitute (changing the appropriate indexes) we find:
`\[v_i = Q_{ji}Q_{jk}v_k\]`
- We can now use the Kronecker Delta to substitute `\(v_i = \delta_{ik}v_k\)` which gives
`\[\delta_{ik}v_k = Q_{ji}Q_{jk}v_k\]`

---
# examples

----
## example

<div class="left">

![3d coordinate system to start general transformation example](../images/transform3d-1.svg)

</div>

<div class="right">

- Find `\(Q_{ij}^1\)` for rotation of `\(60^\circ\)` about `\(x_2\)`
- Find `\(Q_{ij}^2\)` for rotation of `\(30^\circ\)` about `\(x_3^\prime\)`
- Find `\({e}_i^{\prime\prime}\)` after both rotations

</div>

----
## example

![3d illustration of first transformation](../images/transform3d-2.svg)

----
## example

![3d illustration of second transformation (about the axes of the first)](../images/transform3d-3.svg)

----
## example

- `\(Q_{ij}^1 = \cos (x_i^\prime,x_j)\)`
- `\(Q_{ij}^2 = \cos (x_i^{\prime\prime},x_j^\prime)\)`
`\[Q_{ij}^1 = \begin{bmatrix}
	\cos 60 & \cos 90 & \cos 150\\
	\cos 90 & \cos 0 & \cos 90\\
	\cos 30 & \cos 90 & \cos 60
	\end{bmatrix}\]` `\[Q_{ij}^2 = \begin{bmatrix}
	\cos 30 & \cos 60 & \cos 90\\
	\cos 120 & \cos 30 & \cos 90\\
	\cos 90 & \cos 90 & \cos 0
\end{bmatrix}\]`

----
## example

- We now use `\(Q_{ij}\)` to find `\(\hat{e}_i^\prime\)` and `\(\hat{e}_i^{\prime \prime}\)`
- First, we need to write `\(\hat{e}_i\)` in a manner more consistent with index notation
- We will indicate axis direction with a superscript, e.g. `\(\hat{e}_1 = e_i^1\)`
- `\(e_i^\prime = Q^1_{ij} e_j\)`
- `\(e_i^{\prime\prime} = Q^2_{ij} e_j^\prime\)`

----
## example

- How do we find `\(e_i^{\prime\prime}\)` in terms of `\(e_i\)`?
- `\(e_i^{\prime\prime} = Q^2_{ij} Q^1_{jk} e_k\)`

---
# principal values

----
## principal values

- In the 2D coordinate transformation example, we were able to eliminate one value from a vector using coordinate transformation
- For second-order tensors, we desire to find the "principal values" where all non-diagonal terms are zero
- The direction determined by the unit vector, `\(n_j\)`, is said to be the *principal direction* or *eigenvector* of the symmetric second-order tensor, `\(a_{ij}\)` if there exists a parameter, `\(\lambda\)`, such that `\[a_{ij} n_j = \lambda n_i\]`
- Where `\(\lambda\)` is called the *principal value* or *eigenvalue* of the tensor

----
## principal values

- We can re-write the equation
`\[(a_{ij} - \lambda \delta_{ij})n_j = 0\]`

- This system of equations has a non-trivial solution if and only if `\(\det [a_{ij} - \lambda \delta_{ij}] = 0\)`
- This equation is known as the characteristic equation, and we solve it to find the principal values of a tensor

----
## example

- Find the principal values of the tensor 
`\[A_{ij} = \begin{bmatrix}
	1 & 2\\
	2 & 4
\end{bmatrix}\]`

- From the characteristic equation, we know that `\(\det [A_{ij} - \lambda \delta_{ij}] = 0\)`, or 
`\[\begin{vmatrix}
	1-\lambda & 2\\
	2 & 4 - \lambda
\end{vmatrix} = 0\]`

----
## example

- Calculating the determinant gives `\[(1-\lambda)(4-\lambda) - 4 = 0\]`
- Multiplying out and simplifying, we find
`\[\lambda^2 - 5\lambda = \lambda(\lambda-5) = 0\]`

- This has the solution `\(\lambda = 0, 5\)`

---
# invariants

----
## invariants

- Every tensor has some invariants which do not change with coordinate transformation
- These are known as *fundamental invariants*
- The characteristic equation for a tensor in 3D can be written in terms of the invariants
`\[\det [ a_{ij} - \lambda \delta_{ij}] = -\lambda^3 + I_\alpha \lambda^2 - II_\alpha \lambda + III_\alpha = 0\]`

----
## invariants

- The invariants can be found by the following equations
`\[\begin{aligned}
	I_\alpha &= a_{ii}\\
	II_\alpha &= \frac{1}{2}(a_{ii} a_{jj} - a_{ij}a_{ij})\\
	III_\alpha &= \det [ a_{ij}]
\end{aligned}\]`

----
## invariants

- In the principal direction, `\(a_{ij}^\prime\)` will be
`\[a_{ij}^\prime = \begin{bmatrix}
	\lambda_1 & 0 & 0\\
	0 & \lambda_2 & 0\\
	0 & 0 & \lambda_3
\end{bmatrix}\]`

- Since invariants do not change with coordinate systems, we can also write the invariants as 
`\[\begin{aligned}
	I_\alpha &= \lambda_1 + \lambda_2 + \lambda_3\\
	II_\alpha &= \lambda_1\lambda_2 + \lambda_2 \lambda_3 + \lambda_3 \lambda_1\\
	III_\alpha &= \lambda_1 \lambda_2 \lambda_3
\end{aligned}\]`

---
# principal directions

----
## principal directions

- We defined principal directions earlier
`\[(a_{ij} - \lambda \delta_{ij})n_j = 0\]`

- `\(\lambda\)` are the principal values and `\(n_j\)` are the principal directions
- For each eigenvalue there will be a principal direction
- We find the principal direction by substituting the solution for `\(\lambda\)` back into this equation

----
## example

- Find the principal directions for the earlier principal values example
- Recall `\(\lambda = 0,5\)`, let us say `\(\lambda_1 = 5\)`, we find `\(n_j^{(1)}\)` by 
`\[\begin{bmatrix}
	1-\lambda_1 & 2\\
	2 & 4-\lambda_1
\end{bmatrix} \begin{Bmatrix}
	n_1 \\ n_2
\end{Bmatrix} = 0\]`

- This gives 
`\[\begin{bmatrix}
	-4 & 2\\
	2 & -1
\end{bmatrix} \begin{Bmatrix}
	n_1 \\ n_2
\end{Bmatrix} = 0\]`

----
## example

- We proceed to solve the equations using row-reduction, but we find
`\[\begin{bmatrix}
	2 & -1\\
	0 & 0
\end{bmatrix} \begin{Bmatrix}
	n_1 \\ n_2
\end{Bmatrix} = 0\]`

- This means we cannot uniquely solve for `\(n_j\)`
- We are only concerned with the direction, magnitude is not important
- Choose `\(n_2 = 1\)`, solve for `\(n_1\)`
- `\(n^{(1)} = \langle \frac{1}{2}, 1 \rangle\)`

----
## example

- Similarly, for `\(\lambda_2 =0\)`, we find 
`\[\begin{bmatrix}
	1 & 2\\
	2 & 4
\end{bmatrix} \begin{Bmatrix}
	n_1 \\ n_2
\end{Bmatrix} = 0\]`

- Which, after row-reduction, becomes 
`\[\begin{bmatrix}
	1 & 2\\
	0 & 0
\end{bmatrix} \begin{Bmatrix}
	n_1 \\ n_2
\end{Bmatrix} = 0\]`

- If we choose `\(n_2 = 1\)`, we find `\(n_1 = -2\)`
- This gives `\(n^{(2)} = \langle -2, 1 \rangle\)`

----
## example

- We can assemble a transformation matrix, `\(Q_{ij}\)`, from the principal directions
- First we need to normalize them to unit vectors
- `\(||n^{(1)}|| = \sqrt{\frac{5}{4}}\)`
- `\(\hat{n}^{(1)} = \frac{2}{\sqrt{5}} \langle \frac{1}{2}, 1 \rangle = \langle \frac{1}{\sqrt{5}}, \frac{2}{\sqrt{5}} \rangle\)`
- `\(||n^{(2)}|| = \sqrt{5}\)`
- `\(\hat{n}^{(2)} = \langle \frac{-2}{\sqrt{5}}, \frac{1}{\sqrt{5}} \rangle\)`

----
## example

- This gives 
`\[Q_{ij} = \frac{1}{\sqrt{5}}\begin{bmatrix}
	1 & 2\\
	-2 & 1
\end{bmatrix}\]`

- And we find 
`\[A_{mn}^\prime = Q_{mi}Q_{nj}A_{ij}\]`
`\[A_{ij}^\prime = \begin{bmatrix}
	5 & 0 \\
	0 & 0
\end{bmatrix}\]`

---
# examples

----
## example

- Find principal values, principal directions, and invariants for the tensor 
`\[c_{ij} = \begin{bmatrix}
	8 & 0 & 0\\
	0 & 3 & 1\\
	0 & 1 & 3
\end{bmatrix}\]`

----
## example

- Characteristic equation simplifies to
- `\(-\lambda^3 + 14\lambda^2 -56 \lambda + 64 = 0\)`
- Which has the solutions `\(\lambda = 2, 4, 8\)`

----
## example

- To find the principal direction for `\(\lambda_1 = 8\)`
`\[\begin{bmatrix}
	8-8 & 0 & 0\\
	0 & 3-8 & 1\\
	0 & 1 & 3-8
\end{bmatrix}\begin{Bmatrix}
	n_1 \\ n_2 \\ n_3
\end{Bmatrix} = 0\]`

----
## example

- After row-reduction, we find 
`\[\begin{bmatrix}
	0 & 0 & 0\\
	0 & 0 & -24\\
	0 & 1 & -5
\end{bmatrix}\begin{Bmatrix}
	n_1 \\ n_2 \\ n_3
\end{Bmatrix} = 0\]`

- This means that `\(n_3 = 0\)` and, as a result, `\(n_2 = 0\)`.
- `\(n_1\)` can be any value, we choose `\(n_1 = 1\)` to give a unit vector.
- `\(n^{(1)} = \langle 1, 0, 0 \rangle\)`

----
## example

- To find the principal direction for `\(\lambda_2 = 4\)`
`\[\begin{bmatrix}
	8-4 & 0 & 0\\
	0 & 3-4 & 1\\
	0 & 1 & 3-4
\end{bmatrix}\begin{Bmatrix}
	n_1 \\ n_2 \\ n_3
\end{Bmatrix} = 0\]`

----
## example

- After row-reduction, we find 
`\[\begin{bmatrix}
	4 & 0 & 0\\
	0 & -1 & 1\\
	0 & 0 & 0
\end{bmatrix}\begin{Bmatrix}
	n_1 \\ n_2 \\ n_3
\end{Bmatrix} = 0\]`

- This means that `\(n_1 = 0\)`
- We also know that `\(n_2 = n_3\)`, so we choose `\(n_2 = n_1 = 1\)`
- This gives `\(n^{(2)} = \frac{1}{\sqrt{2}}\langle 0, 1, 1 \rangle\)` after normalization

----
## example

- To find the principal direction for `\(\lambda_3 = 2\)`
`\[\begin{bmatrix}
	8-2 & 0 & 0\\
	0 & 3-2 & 1\\
	0 & 1 & 3-2
\end{bmatrix}\begin{Bmatrix}
	n_1 \\ n_2 \\ n_3
\end{Bmatrix} = 0\]`

----
## example

- After row-reduction, we find 
`\[\begin{bmatrix}
	6 & 0 & 0\\
	0 & 1 & 1\\
	0 & 0 & 0
\end{bmatrix}\begin{Bmatrix}
	n_1 \\ n_2 \\ n_3
\end{Bmatrix} = 0\]`

- This means that `\(n_1 = 0\)`
- We also know that `\(n_2 = -n_3\)`, so we choose `\(n_2 = 1\)` and `\(n_1 = -1\)`
- This gives `\(n^{(3)} = \frac{1}{\sqrt{2}}\langle 0, 1, -1 \rangle\)` after normalization

----
## example

- In summary, for `\(c_{ij}\)` we have:
- `\(\lambda_1 = 8\)` and `\(n^{(1)} = \langle 1, 0, 0 \rangle\)`
- `\(\lambda_2 = 4\)` and `\(n^{(2)} = \frac{1}{\sqrt{2}}\langle 0, 1, 1 \rangle\)`
- `\(\lambda_3 = 2\)` and `\(n^{(3)} = \frac{1}{\sqrt{2}}\langle 0, 1, -1 \rangle\)`
- We can assemble `\(n^{(i)}\)` into a transformation tensor
`\[Q_{ij} = \frac{1}{\sqrt{2}}\begin{bmatrix}
	\sqrt{2} & 0 & 0\\
	0 & 1 & 1\\
	0 & 1 & -1
\end{bmatrix}\]`

----
## example

- What is `\(c_{ij}^\prime\)`?
- `\(c_{ij}^\prime = Q_{im}Q_{jn}c_{mn}\)`
`\[c_{ij}^\prime = \begin{bmatrix}
	8 & 0 & 0 \\
	0 & 4 & 0 \\
	0 & 0 & 2
\end{bmatrix}\]`

----
## example

- We can also find the invariants for 
`\[c_{ij} = \begin{bmatrix}
	8 & 0 & 0\\
	0 & 3 & 1\\
	0 & 1 & 3
\end{bmatrix}\]`

- Recall: 
`\[\begin{aligned}
	I_\alpha &= a_{ii}\\
	II_\alpha &= \frac{1}{2}(a_{ii} a_{jj} - a_{ij}a_{ij})\\
	III_\alpha &= \det [ a_{ij}]
\end{aligned}\]`

----
## example

- First invariant `\[I_\alpha = a_{ii} = 8 + 3 + 3 = 14\]`
- Second invariant
`\[II_\alpha = \frac{1}{2}(a_{ii} a_{jj} - a_{ij}a_{ij})\]`
`\[a_{ii} a_{jj} = 14 \times 14\]`
`\[a_{ij}a_{ij} = a_{11}a_{11} + a_{12}a_{12} + a_{13}a_{13} + ... + a_{33}a_{33}\]`
`\[II_\alpha = \frac{1}{2}(196 - 84) = 56\]`

----
## example

- Third invariant `\[III_\alpha = \det [ a_{ij}]\]`
`\[III_\alpha = 8 \times (3 \times 3 - 1 \times 1) = 64\]`
