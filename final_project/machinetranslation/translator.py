"""
This module contains methods that perform language translations
from french to english and vice-versa
"""

import os
from ibm_watson import LanguageTranslatorV3, IAMTokenManager
from ibm_cloud_sdk_core.authenticators import BearerTokenAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['NLU_API_KEY']
url = os.environ['NLU_URL']

# In your API endpoint use this to generate new bearer tokens
iam_token_manager = IAMTokenManager(apikey=apikey)
token = iam_token_manager.get_token()

# in the constructor, assuming control of managing the token
authenticator = BearerTokenAuthenticator(token)
language_translator = LanguageTranslatorV3(version='2019-04-30',
                        authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(english_test):
    """
    Takes an englist text as input and returns
    the translation on french
    """
   #Check if input is null
    if english_test is None:
        french_test = None
    else:
        print('Translating ...')
        translation = language_translator.translate(
            text=english_test,
            model_id='en-fr').get_result()

        french_test = translation['translations'][0]['translation']

    return french_test

def french_to_english(french_test):
    """
    Takes an englist text as input and returns
    the translation on french
    """
    #Check if input is null
    if french_test is None:
        english_test = None
    else:
        print('Translating ...')
        translation = language_translator.translate(
            text=french_test,
            model_id='fr-en').get_result()

        english_test = translation['translations'][0]['translation']

    return english_test
