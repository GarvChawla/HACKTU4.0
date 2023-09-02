import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks', 'thnx'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    response('Great! How May I Help You ', ['i', 'am', 'also', 'fine', 'good', 'great'], single_response=True)
    response('You can use upi, netbanking, debit or credit card', ['which', 'payments', 'payment', 'pay', 'how', 'can', 'i', 'pay', 'methods', 'method', 'are', 'available', '?'], single_response=True)
    response('You can Use Filter to get Favourable results',
             ['how', 'to', 'get', 'cheaper', 'food', 'low', 'less', 'price', 'minimum', 'maximum', 'high', 'rated',
              'rating', 'veg', 'non', 'non-veg', 'expensive', 'affordable', 'prices', 'at'], single_response=True)
    response('Yes you Can Use This Payments Method', ['availabe', 'can', 'i', 'use', 'upi', 'debit', 'card', 'cards', 'paytm', 'pay', 'google', 'phonepay', 'bharatpay', 'can', 'be', 'used', 'is', 'cod', 'cash', 'cashondelivery', 'cashon', 'delivery', 'cash on delivery'],
             single_response=True)
    response('It depends Upon Your Location ', ['how', 'much', 'time', 'does', 'it', 'takes', 'to', 'get', 'my', 'food', 'order', 'delivered', 'deliver','take','?'], single_response=True)
    response('Please Consider Ratings',
             ['which', 'is', 'best', 'restraunt', 'dhaba', 'good', 'star', 'how', 'to', 'find'], single_response=True)
    response('Add Food To Basket after checking rating and Check Out', ['how', 'to', 'order', 'food'], single_response=True)
    response('There Might Be a Network Issue', ['i', 'am', 'unable', 'to', 'make', 'payment', 'transaction', 'pay'], single_response=True)


    response('You can Check Ratings',  ['how', 'to', 'get', 'high', 'food', 'good', 'quality', 'rating', 'healthy', 'best', 'tasty', 'nutritious', 'veg', 'non', 'non-veg', 'expensive', 'at'], single_response=True)
    response('You can Check Ratings', ['how', 'to', 'order', 'food','get','tasty','best','rating','healthy','nutritional'], single_response=True)

   # Longer responses
                                                       #CHAT BOT

    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_RATE,  ['how', 'to', 'get', 'high', 'food', 'good', 'quality', 'rating', 'healthy', 'best', 'tasty', 'nutritious',
              'veg', 'non', 'non-veg', 'expensive', 'at'], required_words=['rate', 'good', 'healthy', 'nutritious', 'how', 'to', 'order', 'buy', 'food'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))