#------------------------------Part1--------------------------------
# In this part we define a list that contains the player names, and 
# a dictionary with player biographies

Player_LIST = ["weather", "temperature", "humidity", "soil moisture"]

Player_BIOGRAPHY = {"weather":"Temperature is 27 degree Celcius  Humidity is 57 percent.",

"temperature":"Temperature is 27 degree Celcius.",

"humidity":"Humidity is 57 percent.",

"soil moisture":"soil moisture is 20 %"}

#------------------------------Part2--------------------------------
# Here we define our Lambda function and configure what it does when 
# an event with a Launch, Intent and Session End Requests are sent. # The Lambda function responses to an event carrying a particular 
# Request are handled by functions such as on_launch(event) and 
# intent_scheme(event).

def lambda_handler(event, context):
    if event['session']['new']:
        on_start()
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event)
    elif event['request']['type'] == "IntentRequest":
        return intent_scheme(event)
    elif event['request']['type'] == "SessionEndedRequest":
        return on_end()

#------------------------------Part3--------------------------------
# Here we define the Request handler functions

def on_start():
    print("Session Started.")

def on_launch(event):
    onlunch_MSG = "Hi, welcome to the My smart farm Alexa Skill. My available parameters are are: " + ', '.join(map(str, Player_LIST)) + ". "\
    "If you would like to hear more about a particular farm parameter, you could say for example: tell me about weather?"
    reprompt_MSG = "Do you want to hear more about a particular player?"
    card_TEXT = "Pick a parameter."
    card_TITLE = "Choose a parameter."
    return output_json_builder_with_reprompt_and_card(onlunch_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

def on_end():
    print("Session Ended.")

#-----------------------------Part3.1-------------------------------
# The intent_scheme(event) function handles the Intent Request. 
# Since we have a few different intents in our skill, we need to 
# configure what this function will do upon receiving a particular 
# intent. This can be done by introducing the functions which handle 
# each of the intents.

def intent_scheme(event):
    
    intent_name = event['request']['intent']['name']

    if intent_name == "Condition":
        return player_bio(event)        
    elif intent_name in ["AMAZON.NoIntent", "AMAZON.StopIntent", "AMAZON.CancelIntent"]:
        return stop_the_skill(event)
    elif intent_name == "AMAZON.HelpIntent":
        return assistance(event)
    elif intent_name == "AMAZON.FallbackIntent":
        return fallback_call(event)

#---------------------------Part3.1.1-------------------------------
# Here we define the intent handler functions

def player_bio(event):
    name=event['request']['intent']['slots']['status']['value']
    player_list_lower=[w.lower() for w in Player_LIST]
    if name.lower() in player_list_lower:
        reprompt_MSG = "Do you want to hear more about a particular player?"
        card_TEXT = "You've picked " + name.lower()
        card_TITLE = "You've picked " + name.lower()
        return output_json_builder_with_reprompt_and_card(Player_BIOGRAPHY[name.lower()], card_TEXT, card_TITLE, reprompt_MSG, False)
    else:
        wrongname_MSG = "You haven't used the proper name of a parameter. If you have forgotten you can pick say Help."
        reprompt_MSG = "Do you want to hear more about a particular parameter?"
        card_TEXT = "Use the proper name."
        card_TITLE = "Wrong name."
        return output_json_builder_with_reprompt_and_card(wrongname_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)
        
def stop_the_skill(event):
    stop_MSG = "Thank you. Bye!"
    reprompt_MSG = ""
    card_TEXT = "Bye."
    card_TITLE = "Bye Bye."
    return output_json_builder_with_reprompt_and_card(stop_MSG, card_TEXT, card_TITLE, reprompt_MSG, True)
    
def assistance(event):
    assistance_MSG = "You can choose among these parameters: " + ', '.join(map(str, Player_LIST)) + ". Be sure to use the proper name when asking about the parameter."
    reprompt_MSG = "Do you want to hear more about a particular parameter?"
    card_TEXT = "You've asked for help."
    card_TITLE = "Help"
    return output_json_builder_with_reprompt_and_card(assistance_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

def fallback_call(event):
    fallback_MSG = "I can't help you with that, try rephrasing the question or ask for help by saying HELP."
    reprompt_MSG = "Do you want to hear more about a particular parameter?"
    card_TEXT = "You've asked a wrong question."
    card_TITLE = "Wrong question."
    return output_json_builder_with_reprompt_and_card(fallback_MSG, card_TEXT, card_TITLE, reprompt_MSG, False)

#------------------------------Part4--------------------------------
# The response of our Lambda function should be in a json format. 
# That is why in this part of the code we define the functions which 
# will build the response in the requested format. These functions
# are used by both the intent handlers and the request handlers to 
# build the output.

def plain_text_builder(text_body):
    text_dict = {}
    text_dict['type'] = 'PlainText'
    text_dict['text'] = text_body
    return text_dict

def reprompt_builder(repr_text):
    reprompt_dict = {}
    reprompt_dict['outputSpeech'] = plain_text_builder(repr_text)
    return reprompt_dict
    
def card_builder(c_text, c_title):
    card_dict = {}
    card_dict['type'] = "Simple"
    card_dict['title'] = c_title
    card_dict['content'] = c_text
    return card_dict    

def response_field_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value):
    speech_dict = {}
    speech_dict['outputSpeech'] = plain_text_builder(outputSpeach_text)
    speech_dict['card'] = card_builder(card_text, card_title)
    speech_dict['reprompt'] = reprompt_builder(reprompt_text)
    speech_dict['shouldEndSession'] = value
    return speech_dict

def output_json_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value):
    response_dict = {}
    response_dict['version'] = '1.0'
    response_dict['response'] = response_field_builder_with_reprompt_and_card(outputSpeach_text, card_text, card_title, reprompt_text, value)
    return response_dict
