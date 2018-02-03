# stopwords_file = "stopwords.txt"
#
# responses = [
#     'Hello and welcome. Please ask me any question in regards to booking. If you wish to talk to a human, please say "Contact customer support"'
# ]
#
# stopwords_file = open(stopwords_file, 'r')
#
# stopwords = []
# for line in stopwords_file:
#     stopwords = [i for i in line.rstrip().split(',')]
#
# keep_going = True
#
# print responses[0]
#
# while keep_going:
#     user_input = input('')
#
#     if "contact customer support" in user_input.lower():
#         print "You will be contacted soon"
#         exit()
#     else:
#         print "I'm sorry, I don't understand that"


# Read bookings.txt and break each query up into tokens
# Remove all stopwords
# Stem each word
