# Plagiarism-checker-Python [Clone]

This repo consists of a source code of a python script to detect plagiarism in textual document using **cosine similarity**

## How is it done?

You might be wondering on how plagiarism detection on textual data is done, well it aint that complicated as you may think.

We all all know that computer are good at numbers, so in order to compute the simlilarity between on two text documents, the textual  raw data is transformed into vectors => arrays of numbers and then from that we are going to use a basic knowledge vector to compute the the similarity between them.


## Getting started

To get started with the code on this repo, you need to either *clone* or *download* this repo into your machine just as shown below;

```bash
git clone https://github.com/Jhomar1158-ux/Plagiarism-Checker-Project
```

## Dependencies 

Before you begin playing with the source code you might need to install deps just as shown below;

```bash
pip3 install -r requirements.txt
```

## Running the App

To run this code, you need to turn on the Flask server, **type the text** in both inputs and then click the **Compare button**, it will automatically calculate the similarity between them and display it on the screen.

```bash
$-> cd Plagiarism-checker-Project
$ Plagiarism-checker-Project-> python3 server.py
('Hello World', 'Hello World', 100%)


```

## A python library ?

Would you like to use Python library instead to help you compare strings and documents without spending time writing the vectorizers by your own then take a look at [Pysimilar](https://github.com/Kalebu/pysimilar).



## Pull Requests

If you have something to add I welcome pull requests on improvement , you're helpful contribution will be merged as soon as possible

## Give it a Star

If you find this repo useful , give it a star so as many people can get to know it.

## Credits

All the credits to [kalebu](https://github.com/kalebu)

```bash
https://github.com/Kalebu/Plagiarism-checker-Python
```