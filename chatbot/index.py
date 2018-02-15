
from nltk.stem.porter import *
import re

training_data = []

training_data.append(
    {
        "class": 'company_name',
        "queries": [
                "What is your company called?",
                "What is the name of your company?",
                "What are you called?",
                "What is the name of your business?",
                "What is your businesses name?",
                "What is the name of your organisation or business?",
                "What is the name of your company?"
            ],
        "response": 'Our company is called TxtStyles Pty Ltd'
    })

training_data.append(
    {
        "class": 'company_location',
        "queries": [
                "Where are you located?",
                "Where can I visit you?",
                "Where can I visit your store?",
                "What is the location of your company?",
                "What is your address?",
                "What's your address?",
                "Where is your building located?",
                "What is the address of your building?"
            ],
        "response": 'We are located at 3/12 Queen St, Brisbane City 4000'
    })

training_data.append(
    {
        "class": 'opening_hours',
        "queries": [
                "What time do you open?",
                "What time do you start?",
                "What time do you close?",
                "What are your operating hours?",
                "What are your hours?",
                "What are your opening hours?",
                "What are your opening times?",
                "How long are you open for?",
                "What days are you open?",
            ],
        "response": 'We are open from 9AM to 5PM Monday to Friday, but you may contact us at any time.'
    })

training_data.append(
    {
        "class": 'contact_number',
        "queries": [
                "What is your number?",
                "What is your phone number?",
                "What is your contact number?",
                "What number can I call you from?",
                "Can I call you?",
                "I would like to call your company",
                "I would like to talk over the phone",
                "I want to talk over the phone",
                "Phone number?",
                "Contact number?"
            ],
        "response": 'You can contact us at 0412345353'
    })

training_data.append(
    {
        "class": 'contact_info',
        "queries": [
                "How can I contact you?",
                "Is there anyway I can contact your company?",
                "How can I contact someone?"
            ],
        "response": 'You can phone us at 0412345353 or alternatively email us at address@email.com'
    })

class_words = {}
corpus_words = {}
response_messages = {}

stemmer = PorterStemmer()
classes = list(set(data['class'] for data in training_data))

for c in classes:
    class_words[c] = []

for data in training_data:
    tokens = []

    queries = [re.sub('[!?]', '', query) for query in data['queries']]
    for query in queries:
        tokens.extend(query.split(" "))

    for word in tokens:
        stemmed_word = stemmer.stem(word)
        if stemmed_word not in corpus_words:
            corpus_words[stemmed_word] = 1
        else:
            corpus_words[stemmed_word] += 1

        class_words[data['class']].extend([stemmed_word])
        response_messages[data['class']] = data['response']


user_input = None
print ("Hello, I am a chatbot designed to help you answer questions about payment. Please feel free to ask me anything payment related")
while user_input is not 'Exit':
    user_input = input()

    if user_input is not "" and user_input is not None:
        score = 0
        tokens = [word for word in re.sub('[!?]', '', user_input).split(' ')]
        responses = {}
        for word in tokens:
            stemmed_word = stemmer.stem(word)
            for classes in class_words:
                if stemmed_word in class_words[classes]:
                    score += (1 / corpus_words[stemmed_word])
                    if classes not in responses:
                        responses[classes] = score
                    else:
                        responses[classes] += score

        sorted_responses = sorted(responses.items(), key=lambda x:x[1], reverse=True)
        if len(sorted_responses) > 0:
            print(response_messages[sorted_responses[0][0]])
        else:
            print("I'm sorry, I don't fully understand what you mean")
