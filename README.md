# Table of Contents
* [Description](#description)
* [Sections](#sections)
* [Getting Started](#getting-started)
* [Built With](#built-with)
* [License](#license)

## Description
This project is aimed at discovering trends in fake news on social media. At the minute I am using apache kafka to live stream tweets from twitter and using machine learning to analyse the tweets. I aim to display in the trends on a webapp in real time.

:exclamation:This is still under active development so not all features are present.

## What is Fake News?
Fake news (also known as junk news, pseudo-news, or hoax news) is a form of news consisting of deliberate disinformation or hoaxes spread via traditional news media (print and broadcast) or online social media. This is the definition from Wikipedia and I think it's an accurate description. Fake news is becoming more and more prevalent so I thought it was time to do something to help stop the spread of fake news. I have created and tested a number of machine learning models on a dataset containing approximately 50,000 instances of labelled fake news. It took some time to scrape the data and I also got some data from the Kaggle dataset repository. I used pandas to concatinate the csv files using dataframes. I then used pandas to clean the data(Ensuring only 1s and 0s in the label column and a few other things). 

:exclamation: In the context of this dataset the number 0 == Reliable & 1 == Unreliable. So a news article labelled 0 is considered reliable and visa versa. 
      
## Sections

This readme is part of the documentation for this project so I am updating this as I go along. I will break the project into different parts and discuss these parts throughout the labelled parts below. For a full in depth analysis please read the dissertation. 

### Part 1. 
#### Data cleaning 
This is the most important part of the project as bad data == bad models. Data was gathered from kaggle and github(need to include refrence here). Tests were performed on the data I gathered myself vs the data I got from Kaggle. The reason being that I knew that the data from kaggle had already been cleaned and labelled therefore I had a good baseline to work off. I then tested my models against the data I gathered vs the kaggle with the models performing at similar levels. I then used pandas to combine the two csv files and did further testing. The extra data did help with the training and validation of results

#### Feature Extraction
The embeddings used for the majority of our modelling are generated using the Doc2Vec model. The goal is to produce a vector representation of each article. Before applying Doc2Vec, we perform some basic pre-processing of the data. This includes removing stopwords, deleting special characters and punctuation, and converting all text to lowercase. This produces a comma-separated list of words, which can be input into the Doc2Vec algorithm to produce an 300-length embedding vector for each article.
Doc2Vec is a model developed in 2014 based on the existing Word2Vec model, which generates vector representations for words . Word2Vec represents documents by combining the vectors of the individual words, but in doing so it loses all word order information. Doc2Vec expands on Word2Vec by adding a ”document vector” to the output representation, which contains some information about the document as a whole, and allows the model to learn some information about word order. Preservation of word order information makes Doc2Vec useful for our application, as we are aiming to detect subtle differences between text documents.

### Part 2. 
#### Models 
The main part of the project. There are many different types of model architectures out there but I decieded to use those I found pretty cool. The models I picked were SVM(support vector machine), LSTM(long short term memory), neural net using keras, neural net using tensorflow and a naive bayes model. I will discuss the results when I actually have them finalised however I will say I'm leaning towards the LSTM model. 

### Part 3. 
#### Deployment 
I will fill out this part when I actually deploy the model. I plan on putting the model into a container (Docker) and using AWS or Heroku to deploy the model. I will need to figure out a continous deployment solution so the model can continue to improve. I realise there is diminishing returns and to improve I will have to redesign the architecture or begin stacking the models.

### Part 4. 


### Part 5. 
#### Dissertation 
Fairly self explainatory. I need to write up all this work into a document many pages long :smiley: </br>
I'm using LaTeX for this.


## Getting Started

To get started just clone this repo or you can use gitpod to load the project in an online virtual enviroment</br>
LINK TO GITPOD =====> https://www.gitpod.io/.

gitpod is really neat and I'd recommned checking this out.

### Prerequisites

Jupyter notebooks =====> https://jupyter.org/ </br>
Anaconda ======> https://www.anaconda.com/ </br>
:warning: You can install jupyter notebooks through anaconda so check out anaconda first!

### How to Run Notebooks
You should have jupyter notebooks installed. Easiest way to do this is to download and run anaconda on your machine that way you can get jupyter notebooks plus a ton of other goodies! Alternatively you can use gitpod and just install the requirments from the command line using

    conda install --yes --file requirements.txt

This will install the dependencies to your conda enviroment. </br>

:bangbang: If one dependency fails then all will fail. This can happen very rarely. To get around this problem please try =>

    while read requirement; do conda install --yes $requirement; done < requirements.txt
  
For further information please refer to =====> https://gist.github.com/luiscape/19d2d73a8c7b59411a2fb73a697f5ed4 


### How to Run Scripts


#### Running the jupyter notebooks
For anyone reading this not familiar with jupyter notebooks, jupyter notebooks will not run like regular python files/scripts. You will need jupyter notebooks installed on your system. To run the notebooks you can just type the command below in the directory of your files or type the command anywhere and just use the gui to move to the files.
        
        jupyter notebook 
        
You can then view and run the notebooks in the browser. </br>
For a beginner tutorial on jupyter notebooks ====> https://www.youtube.com/watch?v=HW29067qVWk


## Built With



## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE) file for details
