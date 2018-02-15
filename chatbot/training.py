from nltk.stem.porter import *
import re

training_data = []

training_data.append({"class": 'payment_method', "message": "Do you accept cash?", "response": 'We accept cash, Visa, Master Card, and Paypal'})
training_data.append({"class": 'payment_method_online', "message": "Can I pay online?", "response": 'You can pay online with Paypal, Visa, or Master Card'})
training_data.append({"class": 'payment_crypto', "message": "Can I pay with bitcoin?", "response": 'We do not accept any crypto-currency'})
training_data.append({"class": 'payment_crypto', "message": "Can I pay with crypto?", "response": 'We do not accept any crypto-currency'})
training_data.append({"class": 'how_to_pay', "message": "How can I pay?", "response": 'You can pay in-store or online'})
training_data.append({"class": 'how_to_pay', "message": "How can I make a payment?", "response": 'You can pay in-store or online'})

class_words = {}
corpus_words = {}
response_messages = {}

stemmer = PorterStemmer()
classes = list(set(data['class'] for data in training_data))

for c in classes:
    class_words[c] = []
for data in training_data:
    tokens = [word for word in re.sub('[!?]', '', data['message']).split(' ')]
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


# print(corpus_words)
# print(class_words)


# training_data.append({'class': 'inventory', 'message': 'what items are on your menu?'})
# training_data.append({'class': 'inventory', 'message': 'What items do you have in stock?'})
# training_data.append({'class': 'inventory', 'message': "Do you have in stock?"})
# training_data.append({'class': 'inventory', 'message': "How much does this cost?"})
# training_data.append({'class': 'inventory', 'message': "What is the price of this item?"})
# training_data.append({'class': 'inventory', 'message': "What is in your inventory?"})
# training_data.append({'class': 'inventory', 'message': "What do you sell?"})
# training_data.append({'class': 'inventory', 'message': "What can I buy?"})
# training_data.append({'class': 'inventory', 'message': "What can I buy from you?"})
# training_data.append({'class': 'inventory', 'message': "What can I purchase from you?"})
# training_data.append({'class': 'inventory', 'message': "What can I purchase from your store?"})
# training_data.append({'class': 'inventory', 'message': "What can I purchase from your business?"})
# training_data.append({'class': 'inventory', 'message': "What can I purchase from your company?"})
# training_data.append({'class': 'inventory', 'message': "What is the cheapest item in your stock?"})
# training_data.append({'class': 'inventory', 'message': "What is the cheapest item on your menu?"})
# training_data.append({'class': 'inventory', 'message': "How much is the cheapest item?"})
# training_data.append({'class': 'inventory', 'message': "How much is the most expensive item on your menu?"})
# training_data.append({'class': 'inventory', 'message': "What is the most expensive item on your menu?"})
# training_data.append({'class': 'inventory', 'message': "What is the least expensive item?"})
# training_data.append({'class': 'inventory', 'message': "What is the least expensive?"})
# training_data.append({'class': 'inventory', 'message': "Show me what is the most expensive"})
# training_data.append({'class': 'inventory', 'message': "Show me the most expensive item"})
# training_data.append({'class': 'inventory', 'message': "Show me the most expensive thing"})
# training_data.append({'class': 'inventory', 'message': "Show me the least expensive thing"})
# training_data.append({'class': 'inventory', 'message': "Show me the cheapest thing"})
