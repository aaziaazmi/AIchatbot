import nltk
nltk.download('punkt')

from nltk.stem.lancaster import LancasterStemmer
stemmer=LancasterStemmer

import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import pickle

with open("MovieData.json") as file:
	data=json.load(file)

try:
	with open("data.pickle","rb") as f:
		words, labels, training, output = pickle.load(f)

except:
	words=[]
	labels=[]
	docs_x=[]
	docs_y=[]

	for chat in data["movie chat"]:
		for pattern in chat["patterns"]:
			wrds=nltk.word_tokenize(pattern)
			words.extend(wrds)                										 #extend is like append but it adds lists without their brackets
			docs_x.append(wrds)               										 #list of list of words in a pattern
			docs_y.append(chat["tag"])      										 #list of tag associated to each pattern

			if chat["tag"] not in labels:
				labels.append(chat["tag"])

	"""convert each word in words to lower and then:
		1: stem each word using stem function in stemmer
		2: remove repetitions using stem (this returns a tuple or set)
		3: convert back to list
		4: sort the list"""

	words=sorted(list(set([stemmer().stem(w.lower()) for w in words if w!="?"]))) 

	labels=sorted(labels)                      #just sort labels

	training=[]                                #one hot encoded list of list of all words where postition of words in each pattern are highlighted
	output=[]                                  #one hot encoded list of list where position of label of each pattern is highlighted

	out_empty=[0 for _ in range(len(labels))]  #unedited line for hot encoded labels

	for x,patternwords in enumerate(docs_x):
	 	bag=[]                                 #hot encoded list for each patern where position of each word is highlighted

	 	patternwrds=[stemmer().stem(w.lower()) for w in patternwords]

	 	for w in words:
	 		if w in patternwrds:
	 			bag.append(1)
	 		else:
	 			bag.append(0)

	 	output_row=out_empty[:]
	 	output_row[labels.index(docs_y[x])]=1                           	#for the index of the label

	 	training.append(bag)                                            	#list of bags 
	 	output.append(output_row)

	training=np.array(training)
	output=np.array(output)

	with open("data.pickle", "wb") as f:
		pickle.dump((words, labels, training, output),f)

tf.reset_default_graph()                                                 	#for resetting the graph

net=tflearn.input_data(shape=[None,len(training[0])])                    	#define input shape
net=tflearn.fully_connected(net,9)                                       	#hidden layer 1
net=tflearn.fully_connected(net,9)                                          #hidden layer 2
net=tflearn.fully_connected(net,len(output[0]),activation="softmax")        #softmax gives probability
net=tflearn.regression(net)                    

model=tflearn.DNN(net)  

try:
	x
	model.load("model.tflearn")

except:
	model=tflearn.DNN(net) 
	model.fit(training, output, n_epoch=700, batch_size=8, show_metric=True)
	model.save("model.tflearn")



def bag_of_words(s, words):                                                    #to hot encode input
	bag=[0 for _ in range(len(words))]

	s_words=[stemmer().stem(w.lower()) for w in nltk.word_tokenize(s)]

	for x in s_words:
		for i,w in enumerate(words):
			if w==x:
				bag[i]=1
	return np.array(bag)


def chat():
	print("\n\n\n\n\n\n\n\n\n\n\nType 'Quit' to exit\n\n\n\n\n\n\n")
	inp=""
	while(inp.lower()!="quit"):
		inp=input("You: ")

		results=model.predict([bag_of_words(inp,words)]) 						#.predict() takes a list of inputs (though we only give one)
		
		results_index=np.argmax(results)
		tag=labels[results_index]
		
		for x in data["movie chat"]:
			if x["tag"]==tag:
				responses=x["response"]

		print("Kylo: "+random.choice(responses))                       #.choice() chosses a random element from a tuple, list or dictionary
		
		if tag=="Goodbye":
			break

chat()
