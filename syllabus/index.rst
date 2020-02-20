Syllabus
========

|Gitter| |Binder| |Colab|

BIOF 509 Spring 2020
====================

This GitHub repository hosts all the material for the BIOF 509 course on Applied
Machine Learning.

Please take a look at the `course website <https://biof509.github.io/>`__.

**BIOF509 - Applied Machine Learning with Python**

**Spring 2020**

Machine learning is a computational field that consists of techniques allowing computers to learn from data and make data-driven predictions or decisions. The ability to implement machine learning approaches appropriately and intelligently is a crucial component of data analysis. BIOF 509 provides a broad practical introduction to machine learning concepts, analysis design, and implementation.

The course will give a broad and conceptual overview of the most popular machine learning algorithms, followed by examples of how and when to apply them to real data. Best practices in designing machine learning analyses will be emphasized and reviewed, along with how to avoid common pitfalls and how to interpret analysis results.

Through in-class assignments, students will implement machine learning models in Python, utilizing state-of-the-art machine learning Python packages, such as scikit-learn and tensorflow. Algorithms that will be covered include but are not limited to linear and logistic regression, random forest, K-means clustering, and deep learning.

Note that the course emphasizes hands-on application of algorithms, and mathematical derivation will not be reviewed.

The course will culminate in a short research project utilizing machine learning to analyze either the student’s own dataset or a public dataset that the student chooses.


Instructors:

* Martin Skarzynski

Teaching assistants:

* Michael Chambers
* Vinay Swamy

Important links:

* `Gitter room for announcements and assistance: <http://gitter.im/biof509/community>`_

Final classes: 6th and 13th of May 2020

*This document is subject to revision. Last revised 14th February 2020.*

Course Description
------------------

Learning Objectives
-------------------

By the end of this course you should be able to:

1. Create data analysis programs in Python language together with numpy, pandas, matplotlib in Jupyter environment
2. Describe the common types of machine learning and deep learning tasks
3. Implement simple machine learning algorithms, such as linear and logistic regression models and clustering utilizing numpy
4. Convert a data set into a form suitable for use by machine learning algorithms
5. Choose appropriate machine learning techniques for data analyses and interpret their results.
6. Properly design machine learning analysis pipelines and avoid common pitfalls.
7. Complete a short research project using machine learning. 

Logistics
---------

This is a 15 week course starting on the 7th February, and finishing on the 16th of May. Classes will take place between 5:30pm and 7:30pm each Thursday in building 60, Rathskeller Room B1A199C.

Attendance in class is strongly recommended; however, we realize other commitments will occasionally prevent attendance. Class materials will generally be distributed over the course website.

Most classes will have hands-on tutorials and assignments. Both practice and graded assignments will generally be provided. Graded assignments should be submitted prior to the following class, please follow the deadlines specified on OKpy website. So that you can follow along during class bringing a laptop to each class is strongly encouraged.

Please check with the FAES regarding the last drop out day and the last day to change status (credit or audit).

Required Materials
------------------


**Each student is encouraged to bring their own laptop to each class.** For the course, we will use Python 3. Any up-to-date python installation should work, but you must be able to install packages. The Anaconda Scientific Python Distribution from Continuum Analytics will likely be the easiest approach to configuring python if you do not already have python installed. The Anaconda installer will automatically install many of the packages we will use during the course.

Recommended Books
-----------------

**There is no required textbook for this course.**

We will link to relevant online resources throughout the course.

If you would like a refresher on the basics, the following resources may be useful:

* `Learn python the hard way (ebook freely available from the author) <http://learnpythonthehardway.org/book/>`_ by Zed A. Shaw. A video course is also `available <http://learnpythonthehardway.org/>`_.
* `Think python (ebook freely available from the author) <http://www.greenteapress.com/thinkpython/thinkpython.html>`_ by Allen B. Downey.

Further material is included on the :doc:`Week 1 page </01/index>`.

The following books cover some of the same material we will cover during the course. These books are not required, and presented solely as an alternative starting point covering the course objectives.

* `The Elements of statistical learning (ebook freely available from the authors) <http://statweb.stanford.edu/~tibs/ElemStatLearn/>`_ by Trevor Hastie, Robert Tibshirani, and Jerome Firedman.
* `Python Machine Learning <http://sebastianraschka.com/books.html>`_ by Sebastian Rashka. Release of a second edition is imminent, notebooks are `already available <https://github.com/rasbt/python-machine-learning-book-2nd-edition>`_

Assignments and Grading
-----------------------

The emphasis of the course is on learning and mastering the skills covered. It is our hope that everyone will be able to complete the assignments and project. If some of the material appears unclear please ask on the corresponding Slack channel for clarification.

The final project is 50% of the course, with the final presentation representing the remainder.


**Final Project**

The final project will consist of the following components:

1) *Project documentation.* Each project should have documentation clarifying its goal and functionality. The code itself should be well-documented,
with comments spread out to aid understanding. Functions and classes should have docstrings describing their functionality, inputs and outputs.

2) *Project code.* The code should be well-organized and easy to read. It should also be written modularly, so that each part of code is reusable.
The code should run and produce the correct output under different conditions. It should also have robust error checking.

3) *Project presentation.* Each student will present their project at the end of the semester. The idea here is to present the project's goals, input, and output,
preferably while showing snippets of code.

Project grades will be determined based on the components outlined above, with each component representing 33% of the project grade.

Some guidelines for the final projects. The *most* important factor is clarity and documentation; we need to understand what you are doing and why you are doing it.

1) We need to understand the problem you are trying to solve or explore, and your overarching goal.
2) We need to understand your approach, in ML terms (supervised / unsupervised, classification / regression, clustering, etc). Whatever ML approach you choose, justify it in terms of your overarching goal and datasets.
3) Describe your data in ML terms: what is each sample and how many are there, what are the features and how are they formatted, etc.
4) Describe the workflow clearly: from raw datasets and their sources, to formatting and preprocessing those data into samples and features, through ML approaches and final results.
5) Code should be documented with docustrings and comments, plots should be labelled in such a way that we know what we are looking at.
6) Note that project documentation and code can be combined into a single Jupyter notebook, but does not have to be.
7) While we appreciate well-written and modular code, with robust error-checking and so forth, this is not required. The most important factor is that the code is legible (docustrings, comments) so that we can follow.


Course Materials
----------------

Course materials will be distributed on this website in the corresponding weekly sections.


Schedule
--------

**1 (5 February):** Course overview. Introduction to machine learning topics

**2 (12 February):** Data retrieval and visualization with numpy, pandas, scikit-learn

**3 (19 February):** Data wrangling, preprocessing, and normalization

**4 (26 February):** Supervised learning 1: Regression problems

**5 (4 March):** Supervised learning 2: Overfitting, regularization, hyperparameter optimization, and cross-validation

**6 (11 March):** Supervised learning 3: Classification problems

**7 (18 March):** Unsupervised learning 1: Clustering

**8 (25 March):** Unsupervised learning 2: Latent variable models

**9 (1 April):** Unsupervised learning 3: Dimensionality reduction and feature selection

**10 (8 April):** Deep learning 1: Introduction to deep learning methods

**11 (15 April):** Deep learning 2: Practicum

**12 (22 April):** Implementing machine learning workflows. Common pitfalls and best practices.

**13 (29 April):** Additional topics in machine learning. Learning by examples

**14 (6 May):** Project presentations and feedback. Part I.

**15 (13 May):** Project presentations and feedback. Part II.

.. |Gitter| image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/biof309/community
   :target: https://gitter.im/biof309/community
.. |Binder| image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/biof509/spring2020/master?urlpath=lab
.. |Colab| image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/biof509/spring2020/
