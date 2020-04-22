##This deals with consuming the data created using our java backend 
from kafka import KafkaConsumer
import re# regular expressions
import clean
from clean2 import cleanup, constructLabeledSentences
import queue
from sklearn.externals import joblib
import pandas
#Need this so that my model can understand the text
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
tk = Tokenizer()


#Need to regex match the text in each message
#Add to the queue 
#And have model predict on the queue 
#Will need to look into a multiprocessor queue 
#Check if tweet is english 
#(?<=lang=).*?(?=user)

#Get the text of the tweet
#(?<=text=).*?(?=lang)
q = queue.Queue(maxsize=100)
cleanQueue = queue.Queue(maxsize=100)
#Load in the model
LSTM = joblib.load("LSTM.pkl")
consumer = KafkaConsumer('live-data')
for message in consumer:
    
    #Get contents
    #This will be in the form of
    match = re.search('(?<=text=).*?(?=lang)', str(message))
    if match is not None:
        q.put(match.group(0))
        for q_item in q.queue:
            #For each tweet in the queue, we want to clean it, add to the cleanQueue and then make a prediction
            cleanText = cleanup(q_item)
            #I will need to convert the cleanstrings to a pandas dataframe and then use doc2vec
            cleanQueue.put(cleanText)
            for cleanQ_item in cleanQueue.queue:
                #for each piece of clean text make a prediction
                #Getting an error so I need to vectorise the input
                tk.fit_on_texts(cleanQ_item)
                index_list = tk.texts_to_sequences(cleanQ_item)
                modelReadableTweet = pad_sequences(index_list, maxlen=500)
                
                
                prediction = LSTM.predict(modelReadableTweet)  
                print(prediction)
            
           
