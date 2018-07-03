.. Index Page

=========================
Machine Learning Notebook
=========================
.. note::
   | In general,this notebook is divided into 5 sections.The first four sections are divided based on its difficulty as you can see below: 
   | Phase1: Math Basis; Phase2: Get Started; Phase3: Step Forward; Phase4: Get Advanced;
   | "Open Resources" section contains awesome open collections on the Internet.

.. toctree::
   :maxdepth: 1
   :glob: 
   :caption: Math Basis
   
   math_basis/*

.. toctree::
   :maxdepth: 1
   :glob: 
   :caption: Get Started
   
   get_started/*

.. toctree::
   :maxdepth: 1
   :glob: 
   :caption: Step Forward
   
   step_forward/*   

.. toctree::
   :maxdepth: 1
   :glob: 
   :caption: Get Advanced
   
   get_advanced/*

.. toctree::
   :maxdepth: 1
   :glob: 
   :caption: Open Resources
   
   open_resources/* 

.. warning::
   This notebook is under early development stage, it seems unavoidable to contain mistakes.
   If you find mistakes,it will be grateful to commit an `issue <https://github.com/lamdeyton/notebook-machine_learning/issues>`_ to me
   or contribute to correct them through `pull request <https://github.com/lamdeyton/notebook-machine_learning/pulls>`_.

Tom M. Mitchell provided a formal definition of the algorithms studied in the `Machine Learning <https://en.wikipedia.org/wiki/Machine_learning>`_:
    "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P if its performance at tasks in T, as measured by P, improves with experience E". 

I think the key of machine learning is to discover appropriate computable models through data training to solve specific tasks.

| In general, any machine learning problem can be assigned to one of two broad classifications: 

- | Supervised learning
  
  | In supervised learning, we are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.
  
  | Supervised learning problems are categorized into "regression" and "classification" problems. In a regression problem, we are trying to predict results within a continuous output, meaning that we are trying to map input variables to some continuous function. In a classification problem, we are instead trying to predict results in a discrete output. In other words, we are trying to map input variables into discrete categories

- | Unsupervised Learning
  
  | Unsupervised learning, on the other hand, allows us to approach problems with little or no idea what our results should look like. We can derive structure from data where we don't necessarily know the effect of the variables.
  
  | We can derive this structure by clustering the data based on relationships among the variables in the data.

.. rubric:: Reference:

#. https://en.wikipedia.org/wiki/Machine_learning
#. https://www.coursera.org/learn/machine-learning/resources/JXWWS