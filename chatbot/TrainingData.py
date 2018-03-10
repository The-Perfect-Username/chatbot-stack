training_data = {}

suburbs = ['taringa', 'indooroopilly', 'toowong']

current_context = None

training_data.update(
    {
        "problem_acknowledgment": {
            "queries": [
                "I would like to report a problem",
                "I found a problem and just wanted to report it",
                "I came across a problem",
                "I would like to report a problem I came across",
                "I would like to report an issue I came across",
                "I found an issue and just wanted to report it",
                "I found a problem and would like to report it",
                "I seemed to have found a problem",
                "I seemed to have discovered a problem"
            ],
            "response": "What kind of issue was it? \n\n a) Technical \n b) Sexual",
            "context": "problem_reporting"
        }
    }
)

training_data.update(
    {
        "do_you_deliver_to_me": {
            "queries": [
                "Can you deliver to my location?"
            ],
            "response": "What is your suburb?",
            "context": "deliveries",
            "next_class": "delivery_suburbs"
        }
    }
)

training_data.update(
    {
        "do_you_deliver": {
            "queries": [
                "Do you make deliveries?",
                "Do you deliver?",
                "Do you have a delivery service?"
            ],
            "response": "Yes, we do deliveries at {}".format(', '.join(suburbs)),
            "context": "deliveries"
        }
    }
)

training_data.update(
    {
        "delivery_suburbs": {
            "queries": ['*'],
            "response": lambda user_input: "Yes we deliver to you! Would you like to order online?" if user_input.lower() in suburbs else "No sorry, we don't.",
            "context": "deliveries",
            'next_class': ['deliveries_yes', 'deliveries_no']
        }
    }
)

# training_data.update(
#     {
#         "deliveries_yes": {
#             "queries": ["Yes", "Confirm", "Affirmative", "Indeed", "Certainly", "Sure", "Yes thanks"],
#             "response": 'You can order online from http://www.oursite.com/ordering',
#             "context": "deliveries"
#         }
#     }
# )

training_data.update(
    {
        "order_online": {
            "queries": [
                'I would like to order something online',
                'How can I order online?',
                'Show me how to order online',
                'Can I order through your site?',
                'Am I able to order through your website?',
                'How can I order online from your site?',
                'How can I order online from your website?'
            ],
            "response": 'You can order online from http://www.oursite.com/ordering',
            "context": "deliveries"
        }
    }
)

training_data.update(
    {
        "ordering_alternatives": {
            "queries": [
                'How can I order?',
                'Can I order something over the phone?',
                'How can I order something not online?',
                'How can I order something not through your site?'
            ],
            "response": 'If you do not wish to order online you can order over the phone at 0412345353',
            "context": "deliveries"
        }
    }
)
#
# training_data.update(
#     {
#         "deliveries_no": {
#             "queries": ["No", "Negative", "Not at all", "Nope", "No thanks"],
#             "response": 'If you do not wish to order online you can order over the phone at 0412345353',
#             "context": "deliveries"
#         }
#     }
# )

training_data.update(
    {
        "company_name": {
            "queries": [
                    "What is your company called?",
                    "What is the name of your company?",
                    "What are you called?",
                    "What is the name of your business?",
                    "What is your business' name?",
                    "What is the name of your organisation or business?",
                    "What is the name of your company?"
                ],
            "response": 'Our company is called TxtStyles Pty Ltd'
        }
    }
)

training_data.update(
    {
        'company_location': {
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
        }
    }
)

training_data.update(
    {
        'company_service': {
            "queries": [
                    "What service do you provide?",
                    "What does your comapny do?",
                    "What does your business do?",
                    "What does your organisation do?",
                    "What service does your company provide?",
                    "What service does your business provide?",
                    "What service does your organisation provide?",
                    "What kind of business do you do?",
                    "What kind of company are you?",
                    "What are the things that you do?",
                    "What are the things that you do as a business?",
                    "What are the things that you do as a company?",
                    "What are the things that you do as an organisation?",
                    "Tell me what you guys do",
                    "What do you do?"
                ],
            "response": 'We are an AI-as-a-service company that empowers small to medium sized businesses by providing a platform wherein they can build their own chatbots to automate their customer support and social media management'
        }
    }
)

training_data.update(
    {
        'opening_hours': {
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
        }
    }
)

training_data.update(
    {
        'contact_number': {
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
        }
    }
)

training_data.update(
    {
        'contact_email': {
            "queries": [
                    "What is your email?",
                    "What is your email address?",
                    "What is your contact email?",
                    "Can I email you?",
                    "I would like to email your company",
                    "Email address?",
                    "Contact email?"
                ],
            "response": 'You can email us at address@email.com'
        }
    }
)

training_data.update(
    {
        'contact_info': {
            "queries": [
                    "How can I contact you?",
                    "Is there anyway I can contact your company?",
                    "How can I contact someone?",
                    "What is your email address and phone number?",
                    "What is your email and phone?",
                    "What is your email and number?",
                    "What is your e-mail?",
                    "E-mail"
                ],
            "response": 'You can phone us at 0412345353 or alternatively email us at address@email.com'
        }
    }
)
