from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from pycorenlp import StanfordCoreNLP

interrogative_words = ["could you", "which", "please reply", "please confirm", "what", "whose", "who", "whom", "where",
                       "when", "how", "why", "do reply", "awaiting your response","can you","please","help","hope","can","asap"]

negative_words = ["unsubscribe", "no-reply", "noreply", "mailer", "automated"]





corenlp = StanfordCoreNLP('http://localhost:9000')







# output = corenlp.semgrex("Your Id card has been blocked. you have to come to the desk to unblock the id card. wi-fi* is not wolring. What is the progress? I keep thinking what will happen with my future. ", pattern='{tag: SBARQ}', filter=False)
# print(output)
# nlp.semgrex(text, pattern='{tag: VBD}', filter=False)



def words_present(all_text, keyword_list, count):  # checks if any word in all_text is present in keyword_list
    if all_text is None:
        return 0
    for word in keyword_list:
        if word in all_text.lower():
            count = count+1
            pos=all_text.lower().index(word)
            all_text=all_text[:pos]+all_text[pos+len(word):]
    # print keyword_list, count
    return count


def verify(sub, bod):
    subject = sub
    body = bod
    count = 0
    # # sent=sent_tokenize(subject)
    # words = word_tokenize(body)
    # pos = pos_tag(words)
    # # print pos

    output = corenlp.annotate(body,
                              properties={
                                  'annotators': 'tokenize,ssplit,pos,depparse,sentiment,parse',
                                  'outputFormat': 'json',
                                  'timeout': 1500}
                              )
    #To print sentiments for each statement
    for s in output["sentences"]:
        print "%d: '%s': %s %s" % (
            s["index"],
            " ".join([t["word"] for t in s["tokens"]]),
            s["sentimentValue"], s["sentiment"])

    for i in range(0, len(output['sentences'])):
        check = output['sentences'][i]['parse']
        print check
        if "SBARQ" in check:
            print "reply"
            return True

    for i in output['sentences']:
        # if i['sentiment'] == "Neutral":
        if (words_present(sub, negative_words, 0) + words_present(body, negative_words, 0) > 0):
            print "no reply"
            return False
        else:
            count = words_present(body, interrogative_words, 0)
            if count == 0:
                print "no reply"
                return False
            else:
                print "reply"
                return False



# verify("hi","Please fix this. We are pleased to announce.")

verify("New-ID Card","hi,\n\nThank you so much.")
