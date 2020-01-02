from requests import get
import json

#####################################################################################################

url="https://api.themoviedb.org/3{}?api_key=9de7a416b343661b9eceebe857d964db"

data={}
l=[]
data["movie chat"]=l

#####################################################################################################

dict1={}
dict1["tag"]="Greetings"
dict1["patterns"]=["Hello","Sup","Greetings","What's up","Hey","Hi","Good Morning","Good Afternoon","Happy Holidays!","heyy","heyyy",
"heyyyy","heyyyyy","heyyyyyy","hii","hiii","hiiii","hiiiii","hiiiiii","hellooo","helloo","hellloooo","helo","heylo"]
dict1["response"]=["Greetings to you!","Happy Feast of Winter Veil!","Salam Walaikum"]
dict1["context_set"]=""

l.append(dict1)

#####################################################################################################

r=get(url.format("/movie/upcoming"))
ddata=r.json()

dict1={}
dict1["tag"]="Upcoming"
dict1["patterns"]=["What are the latest movies that are going to release?","Whats coming soon?",
"Name some upcoming movies","What can I watch later?","releasing soon?","whats coming up?","Whats a new movie?"]

string="Some upcoming movies are:\n"
for d in ddata["results"]:
	string+=d["original_title"]+"\n"

dict1["response"]=[string]
dict1["context_set"]=""

l.append(dict1)

######################################################################################################

r=get(url.format("/trending/movie/week"))
ddata=r.json()

dict1={}
dict1["tag"]="Trending"
dict1["patterns"]=["What are the trending movies?","Whats popular in cinemas?",
"Name some hot movies","Whats poppin?","whats hot?","What should I watch this weekend?","tell me some trending movies","popular movies"]

string="Some trending movies are:\n"
for d in ddata["results"]:
	string+=d["original_title"]+"\n"

dict1["response"]=[string]
dict1["context_set"]=""

l.append(dict1)

#######################################################################################################

dict1={}
dict1["tag"]="Details"
dict1["patterns"]=["Can I get details on a certain movie?","Tell me more information about a film","Can I search a TV Show?",
"Can I learn more about an actor?","Can I learn more about a director?","Can you tell me what ratings this movie got?",
"Can you tell what genre this show is?","Can you tell what genre this movie is?","I wanna know more about this producer?",
"Which comapny produced move?"]
dict1["response"]=["Do you want to know more about a movie, tv show, person, company, or genre?"]
dict1["context_set"]=""

l.append(dict1)

########################################################################################################

dict1={}
dict1["tag"]="Insult"
dict1["patterns"]=["Shut Up","Stupid","Fuck You","Fuck Off","Idiot","Dumb Dumb","Good For Nothing","poopy",
"dumbass","bitch","dumass","piece of shit","fuckoff","fuck u","dumbfuck","You suck","u suck"]
dict1["response"]=["That's not nice :( I'm just trying to help!","Ok boomer","ok whatever","?????","is there a problem?"]
dict1["context_set"]=""

l.append(dict1)

#########################################################################################################

dict1={}
dict1["tag"]="Goodbye"
dict1["patterns"]=["cya", "See you later", "Goodbye", "I am Leaving", "Have a Good day","bye","quit"]
dict1["response"]= ["Sad to see you go :(", "Talk to you later", "Boi Bye"]
dict1["context_set"]=""

l.append(dict1)

#########################################################################################################

dict1={}
dict1["tag"]="name"
dict1["patterns"]=["what is your name", "what should I call you", "whats your name?","who are you?","what is this?"]
dict1["response"]= ["Hi. My name is Kylo Ren. I am here to chat with you and answer your questions about the film industry to the best of my abilities.",
"I am your father"]
dict1["context_set"]=""

l.append(dict1)

#########################################################################################################

dict1={}
dict1["tag"]="aazia"
dict1["patterns"]=["Aazia is stupid","What do you think of Aazia?","Aaazia is so irritating","Aazia sucks","Aazia","Who is Aazia?"]
dict1["response"]= ["Aazia is my lord and creator.","Aazia is your dad"]
dict1["context_set"]=""

l.append(dict1)

#########################################################################################################

filepath="C:\\Users\\aazia\\OneDrive\\Desktop\\AI Chatbot"+'\\'+"MovieData.json"

with open(filepath,"w") as f:
	json.dump(data,f)
