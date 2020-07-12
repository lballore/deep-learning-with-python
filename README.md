# TensorFlow 2.* exercises for the book "Deep Learning with Python" by François Chollet.
This repository contains Jupyter notebooks implementing the code samples found in the book [Deep Learning with Python (Manning Pubblications)](https://www.manning.com/books/deep-learning-with-python?a_aid=keras&a_bid=76564dff) by [François Chollet](https://github.com/fchollet), gathered by chapter.

## Disclaimer
The author [already published notebooks with the exercises in his Github account](https://github.com/fchollet/deep-learning-with-python-notebooks). Those you can find in this repository are made by myself for my own learning, with no intention so steal any intellectual property. **Exercises that worked flawlessly in TF 2 have been simply copied**.

## Requirements
- Create a virtual environment with `conda` or `virtualenv`. Recommended `conda` with Python 3.6.
```
conda create --name <your_project> python=3.6
```
- Install dependencies:
```
pip install -r requirements.txt
```

## Contents
The exercises in the book are written for `tensorflow 1.*` and `Keras 2.0.8`. All the code in this repo have been rewritten to work with `tensorflow 2.2.*` and the corresponding Keras version `2.2.4-tf`.

---

### Chapter 1. - What is deep learning?
No relevant exercises

### Chapter 2. - Before we begin: the mathematical building blocks of neural networks
- 01: a first look at a neural network - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_02/01%20-%20A%20first%20look%20at%20a%20neural%20network.ipynb)

### Chapter 3. - Getting started with neural networks
- 01: binary classification - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_03/01%20-%20Binary%20classifier.ipynb)
- 02: multiclass classification - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_03/02%20-%20Multiclass%20classifier.ipynb)
- 03: logistic regression - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_03/03%20-%20Logistic%20regression.ipynb)

### Chapter 4. - Fundamentals of machine learning
- 01: binary classification: mitigate overfitting and underfitting - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_04/01%20-%20Binary%20classifier%20-%20mitigate%20overfitting.ipynb)

### Chapter 5. - Deep learning for computer vision
- 01: introduction to CNN - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_05/01%20-%20Introduction%20to%20CNN.ipynb)
- 02: using CNNs with small datasets - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_05/02%20-%20Using%20convnets%20with%20small%20datasets.ipynb)
- 03: using a pretrained CNN - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_05/03%20-%20Using%20a%20pretrained%20CNN.ipynb)
- 04: visualizing what a CNN learn - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_05/04%20-%20Visualizing%20what%20CNN%20learn.ipynb)

### Chapter 6. - Deep learning for text and sequences
- 01: one-hot encoding of words or characters - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_06/01%20-%20One-hot%20encoding%20of%20words%20or%20characters.ipynb)
- 02: using word embeddings - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_06/02%20-%20Using%20word%20embeddings.ipynb)
- 03: understanding RNNs - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_06/03%20-%20Understanding%20RNNs.ipynb)
- 04: advanced use of RNNs - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_06/04%20-%20Advanced%20use%20of%20RNNs.ipynb)
- 05: sequence processing with convnets - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_06/05%20-%20Sequence%20processing%20with%20convnets.ipynb)

### Chapter 7. - Advanced deep-learning best practices
- 01: the Keras functional API - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_07/01%20-%20The%20Keras%20functional%20API.ipynb)

### Chapter 8. - Generative deep learning
- 01: text generation with LSTM - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_08/01%20-%20Text%20generation%20with%20LSTM.ipynb)
- 02: Deep Dream - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_08/02%20-%20Deep%20Dream.ipynb)
- 03: neural style transfer - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_08/03%20-%20Neural%20style%20transfer.ipynb)
- 04: variational autoencoders (VAEs) - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_08/04%20-%20Variational%20autoencoders.ipynb)
- 05: introduction to GANs - [notebook](https://github.com/lucone83/deep-learning-with-python/blob/master/notebooks/chapter_08/05%20-%20Introduction%20to%20GANs.ipynb)
