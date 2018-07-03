.. _linear_algebra:

==============
Linear Algebra
==============

.. contents:: :local:

Linear algebra is the branch of mathematics concerning linear equations, linear functions and their representations through matrices and vector spaces. 

Matrix
======

.. contents:: :local:

| In mathematics, a matrix (plural: matrices) is a rectangular array of numbers, symbols, or expressions, arranged in rows and columns.
| For example,matrix A has dimensions of :math:`m \times n`,its individual items denoted by :math:`a_{i,j}`, where max i = m,max j = n, 
  are called  its elements or entries. matrix A can be denoted as below: 

.. math::
   A_{m,n} = \begin{Bmatrix}
   a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\ 
   a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\ 
   \vdots  & \vdots  & \cdots & \vdots \\
   a_{m,1} & a_{m,2} & \cdots & a_{m,n} \\ 
   \end{Bmatrix} = (a_{i,j}) \ \epsilon \  \mathbb{R}^{\ m \ \times \ n}

- Row vector has dimensions: :math:`1 \times n`, it is a matrix with one row, denoted by:

.. math::
   v_{(row)} = \begin{Bmatrix}
   a_1 & a_2 & \cdots & a_n
   \end{Bmatrix}

- Column vector has dimensions: :math:`n \times 1`,it is a matrix with one column,denoted by:

.. math::
   v_{(column)} = \begin{Bmatrix}
   a_1 \\ a_2 \\ \vdots \\ a_n
   \end{Bmatrix}

Basic Operations
----------------

.. contents:: :local:

There are a number of basic operations that can be applied to modify matrices, called matrix addition, scalar multiplication, transposition, matrix multiplication, row operations, and submatrix.

Addition
********

| The sum :math:`A + B` of two m-by-n matrices :math:`A` and :math:`B` is calculated elementwise:
 :math:`(A + B)_{i,j} = A_{i,j} + B_{i,j}`, where 1 ≤ i ≤ m and 1 ≤ j ≤ n.
| Now, provide an example:

.. math::
   A & = \begin{Bmatrix}
   1 & 2 & 3 \\ 
   4 & 5 & 6
   \end{Bmatrix},
   B = \begin{Bmatrix}
   4 & 5 & 6 \\ 
   1 & 2 & 3
   \end{Bmatrix} \\\\\
   A + B  & = \begin{Bmatrix}
   1 + 4 & 2 + 5  & 3 + 6 \\ 
   4 + 1 & 5 + 2  & 6 + 3
   \end{Bmatrix}
   = \begin{Bmatrix}
   5 & 7  & 9 \\ 
   5 & 7  & 9
   \end{Bmatrix}

Scalar Multiplication
*********************

| The product :math:`c \cdot A` of a number c (also called a scalar in the parlance of abstract algebra) and a matrix A is computed by multiplying every element of A by c: 
| :math:`(c \cdot A)_{i,j} = c \cdot A_{i,j}`.
| For example: 

.. math::
   A & = \begin{Bmatrix}
   1 & 2 & 3 \\ 
   4 & 5 & 6
   \end{Bmatrix},
   c = 2 \\\\\
   c \cdot A  & = \begin{Bmatrix}
   2 \cdot 1 & 2 \cdot 2 & 2 \cdot 3 \\ 
   2 \cdot 4 & 2 \cdot 5 & 2 \cdot 6 
   \end{Bmatrix}
   = \begin{Bmatrix}
   2 & 4  & 6 \\ 
   8 & 10  & 12
   \end{Bmatrix}

Transposition
*************

| The transpose of a matrix is formed by turning its rows to columns and vice versa.denoted by: :math:`(A^T)_{i,j} = A_{j,i}`.
| Give it an example: 

.. math::
   A & = \begin{Bmatrix}
   1 & 2 & 3 \\ 
   4 & 5 & 6
   \end{Bmatrix} \\\\
   A^T & = \begin{Bmatrix}
   1 & 4  \\ 
   2 & 5  \\ 
   3 & 6  \\ 
   \end{Bmatrix}

Matrix multiplication
*********************

| Multiplication of two matrices is defined if and only if the number of columns of the left matrix is the same as the number of rows of the right matrix.
| If A is an m-by-n matrix and B is an n-by-p matrix, then their matrix product AB is the m-by-p matrix whose entries are given by dot product of the corresponding row of A and the corresponding column of B:
| :math:`[AB]_{i,j} = A_{i,1}B_{1,j} + A_{i,2}B_{2,j} + \cdots + A_{i,n}B_{n,j} = \sum_{r=1}^{n}A_{i,r}B_{r,j}` 
| Let's also see an example:

.. math::      
   A & = \begin{Bmatrix}
   1 & 2 & 3 \\ 
   4 & 5 & 6
   \end{Bmatrix},
   B = \begin{Bmatrix}
   1 & 4  \\ 
   2 & 5  \\ 
   3 & 6  \\ 
   \end{Bmatrix} \\\\
   A \cdot B & = \begin{Bmatrix}
   (1 \cdot 1) + (2 \cdot 2) + (3 \cdot 3) & (1 \cdot 4) + (2 \cdot 5) + (3 \cdot 6) \\ 
   (4 \cdot 1) + (5 \cdot 2) + (6 \cdot 3) & (4 \cdot 4) + (5 \cdot 5) + (6 \cdot 6)
   \end{Bmatrix} \\\\
   & = \begin{Bmatrix}
   14 & 32  \\ 
   32 & 77 
   \end{Bmatrix}

| Matrix multiplication satisfies the rules (AB)C = A(BC) (associativity), and (A+B)C = AC+BC as well as C(A+B) = CA+CB (left and right distributivity), whenever the size of the matrices is such that the various products are defined.
| Notice that matrix multiplication is not commutative,for example the product AB may be defined without BA being defined, namely if A and B are m-by-n and n-by-k matrices, respectively, and m ≠ k.

Square Matrix
-------------

Square matrix has dimensions :math:`n \times n`,it is a matrix with same number of rows and columns,denoted by:

.. math::
   A_{(square)} = \begin{Bmatrix}
   a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
   a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\ 
   \vdots  & \vdots  & \cdots & \vdots \\
   a_{n,1} & a_{n,2} & \cdots & a_{n,n}
   \end{Bmatrix}

Diagonal & Identity Matrix
**************************

| The main diagonal of a square matrix are the elements with same index in rows and columns,can be denoted by :math:`a_{ii}`.

| the diagonal matrix :math:`D_n` of size n is a square matrix that all entries outside the main diagonal are zero.
| For example with n = 3

.. math::
   D_n = \begin{Bmatrix}
   a_{1,1} & 0 & 0 \\
   0 & a_{2,2} & 0 \\
   0 & 0 & a_{3,3} \\
   \end{Bmatrix}

| The identity matrix :math:`I_n` of size n is the n-by-n matrix in which all the elements on the main diagonal are equal to 1 and all other elements are equal to 0, for example,

.. math::
   I_1 = \begin{Bmatrix}
   1
   \end{Bmatrix},
   I_2 = \begin{Bmatrix}
   1 & 0 \\ 
   0 & 1
   \end{Bmatrix},
   \cdots ,
   I_n = \begin{Bmatrix}
   1 & 0 & \cdots & 0 \\
   0 & 1 & \cdots & 0 \\
   \vdots  & \vdots  & \ddots & \vdots  \\
   0 & 0 & \cdots & 1 \\
   \end{Bmatrix}

Inverse Matrix
**************

| A square matrix A is called invertible or non-singular if there exists a matrix B such that
| :math:`AB = BA = I_n`
| where :math:`I_n` is the n×n identity matrix with 1s on the main diagonal and 0s elsewhere. If :math:`B` exists, it is unique and is called the inverse matrix of :math:`A`, denoted :math:`A^{−1}`.

.. rubric:: Reference:

#. https://en.wikipedia.org/wiki/Linear_algebra
#. https://en.wikipedia.org/wiki/Matrix_(mathematics)
#. https://en.wikibooks.org/wiki/LaTeX/Mathematics#Matrices_and_arrays