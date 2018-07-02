.. _calculus:

========
Calculus
========

.. contents:: :local:

Calculus is the mathematical study of continuous change.
It has two major branches, differential calculus (concerning instantaneous rates of change and slopes of curves),
and integral calculus (concerning accumulation of quantities and the areas under and between curves).
These two branches are related to each other by the fundamental theorem of calculus. 
Both branches make use of the fundamental notions of convergence of infinite sequences and infinite series to a well-defined limit.

Derivative
==========

.. contents:: :local:

| The derivative of a function of a real variable measures the sensitivity to change of the function value (output value) with respect to a change in its argument (input value). 
 Derivatives are a fundamental tool of calculus.
| The derivative of a function of a single variable at a chosen input value, when it exists, is the `slope <https://en.wikipedia.org/wiki/Slope>`_ of the `tangent line <https://en.wikipedia.org/wiki/Tangent>`_ to the `graph of the function <https://en.wikipedia.org/wiki/Graph_of_a_function>`_ at that point.
| The red tangent line is the best `linear approximation <https://en.wikipedia.org/wiki/Linear_approximation>`_ of the function near that input value as you can see below:

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Tangent_to_a_curve.svg/440px-Tangent_to_a_curve.svg.png

Intuition
---------

The simplest case, y is a linear function, :math:`y = f(x) = mx + b`,for real numbers m and b, and the slope m is given by

.. math::

    m = \frac{change \ in \ y}{change \ in \ x} = \frac{\Delta y}{\Delta x}.  

The symbol :math:`\Delta` is an abbreviation for "change in". It can be proved:

.. math::

    & y = f(x) = mx + b \\\\
    & \Delta y = f(x + \Delta x) - f(x) = (m (x + \Delta x) + b) - (mx + b) = m \Delta x. \\\\
    & m = \frac{\Delta y}{\Delta x}.

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Wiki_slope_in_2d.svg/500px-Wiki_slope_in_2d.svg.png

Definition
----------

| Let f(x) be a real valued function defined in an open neighborhood of a real number a. 
| The derivative of y with respect to x at a is, geometrically, the slope of the tangent line to the graph of f(x) at (a, f(a)).
| The slope of the tangent line is very close to the slope of the line through (a, f(a)) and a nearby point on the graph, for example (a + h, f(a + h)). These lines are called `secant lines <https://en.wikipedia.org/wiki/Secant_line>`_.
| The slope m of the secant line is the difference between the y values of these points divided by the difference between the x values, that is,

..  math:: 

    m = \frac{\Delta f(a)}{\Delta a} = \frac{f(a+h) - f(a)}{(a+h) - (a)} = \frac{f(a + h) - f(a)}{h}.

Therefore, the limit of the difference quotient as h approaches zero, if it exists, should represent the slope of the tangent line to (a, f(a)). This limit is defined to be the derivative of the function f(x) at a:

..  math:: 

    & f'(a) = \lim_{h\to0}\frac{f(a + h) - f(a)}{h} = \lim_{\Delta x\to0}\frac{f(a + \Delta x) - f(a)}{\Delta x}.\\\\
    & f'(x) = \lim_{\Delta x\to0}\frac{f(x + \Delta x) - f(x)}{\Delta x}.

.. image:: https://upload.wikimedia.org/wikipedia/commons/c/cc/Tangent_animation.gif

Computation Example
-------------------

| We have function: \ :math:`f(x) = mx +b`. Let's try to compute the derivative by ourselves.

.. math::
   
   & f'(x)  = \lim_{\Delta x\to0}\frac{f(x + \Delta x) - f(x)}{\Delta x}.\\\\
   & \begin{align}
   f'(x) & = \lim_{\Delta x\to0}\frac{f(x + \Delta x) - f(x)}{\Delta x}\\
         & = \lim_{\Delta x\to0}\frac{(m(x + \Delta x) + b) - (mx + b)}{\Delta x}\\
         & = \lim_{\Delta x\to0}\frac{mx + m\Delta x +  b - mx - b}{\Delta x}\\
         & = \lim_{\Delta x\to0}\frac{m\Delta x}{\Delta x}\\ 
         & = \lim_{\Delta x\to0}m\\
         & = m.
    \end{align}      

| For example,we want to compute derivative of function :math:`y = f(x) = 2x +1`.
| According to the above derivative equation, we know that the derivative is :math:`y'=f'(x) = 2`.

.. rubric:: Reference:

#. https://en.wikipedia.org/wiki/Calculus
#. https://en.wikipedia.org/wiki/Derivative