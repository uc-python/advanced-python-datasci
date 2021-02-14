# Advanced Python for Data Science

[![Test](https://github.com/uc-python/advanced-python-datasci/workflows/Test/badge.svg)](https://github.com/uc-python/advanced-python-datasci/actions?query=workflow%3ATest)

### Course Description

This is a two-day course that introduces how one can use Python for advanced data science tasks, such as deep learning and natural language processing.
Most of the time will be spent working through example problems end-to-end in the classroom.
Students will learn the fundamentals of the Keras package (for deep learning) and will explore several NLP packages and methodologies to see the strengths of each.
Some additional time will be reserved for discussion of real programming challenges students have encountered, and for an overview of related relevant technologies students may need in an industry setting (e.g. Git and GitHub).

### Objectives

1. Develop an intuition for what problems are suited to deep learning- and/or NLP-based solutions.
2. Build familiarity with the basic interfaces of key Python libraries for deep learning and NLP: [Keras](http://keras.io), [FuzzyWuzzy](https://github.com/seatgeek/fuzzywuzzy), and [gensim](https://radimrehurek.com/gensim/).
3. Gain a high-level understanding of the function of data science-adjacent technologies that students will encounter in the workplace, focusing on [Git](https://git-scm.com) and [GitHub](https://github.com).

### Prerequisites

- Strong understanding of core Python concepts: variables, loops, conditionals, and functions
- Some experience using Jupyter Notebooks or Jupyter Lab
- Solid grasp of Pandas and how to use it for data manipulation: filtering, selecting, aggregating, slicing (indexing), and updating
- High-level understanding of modeling concepts: training and test data, model accuracy, and overfitting

### Tentative Agenda
**This workshop will be 100% virtual over 4 half-days.**

*Exact timing TBD*

**Day 1**

| Day | Topic                                                                          |     Time      |
| :-: | :----------------------------------------------------------------------------- | :-----------: |
|  1  | Introductions                                                                  |  9:00 - 9:15  |
|     | Refresher on Key Python & Pandas Concepts                                      |  9:15 - 9:45  |
|     | Why Do We Need Deep Learning?                                                  |  9:45 - 10:00 |
|     | Why Use Python for Deep Learning?                                              | 10:00 - 10:30 |
|     | Break                                                                          | 10:30 - 10:45 |
|     | Overview of Keras and Tensorflow                                               | 10:45 - 12:00 |
|     | Q&A                                                                            | 12:00 - 12:30 |
|  2  | Q&A                                                                            |  8:30 - 9:00  |
|     | Walkthrough of Example Using Keras                                             |  9:00 - 10:00 |
|     | High-level Discussion of Deep Learning -- How Does It Work?                    | 10:00 - 10:45 |
|     | Break                                                                          | 11:00 - 11:15 |
|     | Deep Learning Case Study                                                       | 11:15 - 12:15 |
|  3  | Deep Learning Case Study Review; Q&A                                           |  8:30 - 9:00  |
|     | What is NLP and What Problems Can It Solve?                                    |  9:00 - 9:30  |
|     | Popular NLP Packages in Python                                                 |  9:30 - 9:45  |
|     | Break                                                                          |  9:45 - 10:00 |
|     | Overview of the FuzzyWuzzy Package                                             | 10:00 - 10:30 |
|     | Walkthrough of Example Using FuzzyWuzzy                                        | 10:30 - 11:00 |
|     | Overview of Word2Vec and gensim Package                                        | 11:00 - 12:00 |
|     | Q&A                                                                            | 12:00 - 12:30 |
|  4  | Q&A                                                                            |  8:30 - 9:00  |
|     | Walkthrough of Example Using gensim                                            |  9:00 - 9:45  |
|     | Discussion of Git, GitHub, and Other Data Science-adjacent Tools               |  9:45 - 10:30 |
|     | NLP Case Study                                                                 | 10:30 - 11:30 |
|     | Case Study Review; Q&A; Wrap-up                                                | 11:30 - 12:30 |

### Course Preparation

You will need to install Python, Jupyter, and the relevant libraries on your personal computer for this workshop. we also recommend downloading the course materials.

See below for instructions on doing so.

#### 1. Python, Jupyter, and Package Installation.

These easiest way to install Python, Jupyter, and the necessary packages is through Anaconda. To download and install Anaconda:

1. Visit the [Anaconda download page](https://www.anaconda.com/products/individual).
2. Select your appropriate operating system
3. Click the "Download" button for Python 3.8 - this will begin to download the Anaconda installer
4. Open the installer when the download completes, and then follow the prompts. If you are prompted about installing PyCharm, elect **not** to do so.
5. Once installed, open the Anaconda Navigator and launch a Jupyter Notebook to ensure it works.
6. Follow [the package installation instructions](https://docs.anaconda.com/anaconda/navigator/tutorials/manage-packages/#installing-a-package) to ensure `pandas`, `keras`, `seaborn`, `scikit-learn`, `fuzzywuzzy`, and `gensim` packages are installed.
    - Note that `fuzzywuzzy` may need to be installed from a non-standard "channel", or package source -- its channel is called *conda-forge*. If you have trouble installing `fuzzywuzzy`, we'll be able to help in class.

#### 2. Download Class Materials

There are two ways to download the class materials:

1. Clone it - If you're familiar with using Git, we recommend cloning the repo.
2. Download the files as a zip - This will allow you to download a static copy of the files here, but in order to get any updates you'll need to redownload the entire repo. Use [this link](https://github.com/uc-python/advanced-python-datasci/archive/master.zip).

### Your Instructors

If you have any specific questions prior to the class you can reach out to us directly via GitHub or email:

  * Ethan Swan: [GitHub](https://www.github.com/eswan18) & [Email](mailto:ethanpswan@gmail.com)
  * Bradley Boehmke: [GitHub](https://www.github.com/bradleyboehmke) & [Email](mailto:bradleyboehmke@gmail.com)
