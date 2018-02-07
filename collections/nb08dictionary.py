import pprint

NEWS_PASSAGE = """ Bell Canada is alerting customers after hackers illegally
accessed the information of fewer than 100,000 customers, the telecom giant
told CBC News.

The breach comes just eight months after 1.9 million customer emails were
stolen from Bell's database by an anonymous hacker.

Bell is Canada's largest telecom company, with over 22 million customers.

The information obtained in the latest breach included details such as names,
email addresses, account user names and numbers, as well as phone numbers.

Bell said there was no indication that credit card, banking or other
information was accessed.

But, it would not say when the breach took place or whether it was related to
a past incident.

"We apologize to our customers and are contacting all those affected," said
Bell spokesperson Marc Choma in an email.

Bell added that it had notified appropriate government agencies including the
Office of the Privacy Commissioner of Canada.

"Bell works closely with law enforcement, government and the broader
technology industry to combat the growth of cybercrimes, and we have
successfully supported law enforcement in past prosecutions of hackers,"
Choma said.

Ongoing investigation Tobi Cohen, a spokesperson for the Office of the
Privacy Commissioner, confirmed in an email that Bell had notified it of the
breach and that it is following up with the company to get more information
and "determine follow up actions."

The RCMP is also investigating.

Chester Wisniewski, an expert at the data security firm Sophos Canada, said
the breach did make customers more likely to be victimized by potential
phishing attacks; as seen in other big breaches like those at LinkedIn and
Ashley Madison.

AshleyMadison security protocols violated privacy laws, watchdog says "When
you see email addresses leaked, that's a really goodthing for spammers and
phishing attacks through email, because they know that if you're in Bell's
database, you likely to have some sort of commercial relationship with Bell,"
he said.

"So, they can send you one of those fake emails saying, 'Hey your cell phone
bill is due, click here to login.'"

Wisniewski added that Bell was under no legal obligation to notify customers
of the breach, because stolen email addresses are not considered personally
identifiable such as a driver's licence or social insurance number.

"A lot of times when companies lose this kind of information, they don't even
tell you," he said. "The good thing about them telling us is to put us on
alert for those types of things now."

A person or group claiming to be behind the attack against Bell in May warned
in an online post that more data would be leaked if Bell did not co-operate."""

def remove_punctuation(passage):
    """
    This function returns a string with all punctuation converted to spaces

    Args:
        passage: the source string

    Returns:
        string with no punctuation only spaces

    Note:
        There is a better method for this that uses regular expressions
    """
    punctuation = ".", "'", '"', ";", ":", ",", "?"

    for i in punctuation:
        passage = passage.replace(i, " ")

    return passage

def splitstring(passage):
    passage = passage.split()
    return passage

def DicOccurances(word, dic):
    if word in dic:
        return dic[word]
    else:
        return 0

def IsWord(word):
    if word.isalpha():
        if len(word)>1 or (word == ("a" or "i")):
            return word
    else:
        return False

def makelist(Dic):

    keys_list = []
    values_list = []
    Dictionary_to_list = []

    #Separate Dic into a list of keys and a list of values
    for index in Dic:
        keys_list.append(index)
        values_list.append(get_key_value(index, Dic))

    #bubblesort the values_list in descending order, mirroring any changes in the keys_list
    for index in range(len(values_list)-1):
        for count in range(len(values_list)-1):
            if values_list[count]<values_list[count+1]:
                values_list[count],values_list[count+1] = values_list[count+1],values_list[count]
                keys_list[count],keys_list[count+1] = keys_list[count+1],keys_list[count]

    #merge values_list and keys_list into a single list
    for number in range(len(values_list)-1):
        Dictionary_to_list.append([keys_list[number],values_list[number]])
       
    return Dictionary_to_list
 
def gen_word_freq_dict(passage):
    # split passage into list of words
    passage = splitstring(passage)
    # sort word list
    passage = sorted(passage)
    # create an empty dictionary
    dic = {}

    # loop over each word in the list of raw words
    for word in passage:
        # convert the word to lower case
        word = word.lower()

        # if word is already in the words dictionary
        if word in dic:
            # increase the count for that word
            dic[word] = dic[word] + 1
            
        # else if the word is:
        # * made of alphabetical characters and
        # * is longer than a single character or is an "i", or "a"
            # add the word to the dictionary and set its counter to 1
        elif IsWord(word):
            dic[word] = 1
       
    # return the word:count dictionary
    return dic

def get_key_value(key_value_pair, Diction):
    """
    This function returns the value portion of a single dictionary item

    This is a more explicit method than using a lambda when implementing common
    sorting idioms.

    Args:
        key_value_pair: this tuple contains the current key <-> value mapping of the dictionary

    Returns:
        The value stored in the current mapping, i.e. the tuple element in position 1 []
    """
    try:
        return Diction[key_value_pair]
    except:
        return "0"

# remove the punctuation from the passage
NEWS_PASSAGE = remove_punctuation(NEWS_PASSAGE)

# create a dictionary that stores word frequencies
word_freq_dict = gen_word_freq_dict(NEWS_PASSAGE)

print("")

#prompt the user for a word and convert it to lower case
word = input("Enter a word: ")
word = word.lower()

#output how many times that lowercase word appeared in the passage
print(get_key_value(word, word_freq_dict))

## Bonus
# create a sorted list from the dictionary using the get_key_value function
# above and the `sorted()` global function
# see https://docs.python.org/3/library/functions.html#sorted and
# https://docs.python.org/3/howto/sorting.html#sortinghowto
# print the five most frequently used words and how often they were used
sortedlist = makelist(word_freq_dict)

print("\nBonus!")
for index in range(5):
    print(str(sortedlist[index]))

print("")