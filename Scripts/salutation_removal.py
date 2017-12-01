import re
import string

def get_salutation(email_text):
    
    salutation_opening_statements = ["sir",
                                     "ma'am",
                                     "greetings",
                                     "hi",
                                     "dear",
                                     "to",
                                     "hey",
                                     "hello",
                                     "thanks",
                                     "good morning",
                                     "good afternoon",
                                     "good evening",
                                     "thankyou",
                                     "thank you",
                                     "Sir/Ma'am"]
    pattern = "(?P<salutation>(" + "|".join(salutation_opening_statements) + ")+(\s*\w*)(\s*\w*)(\s*\w*)(\s*\w*)(\s*\w*)[\.,\xe2:]+\s*)"
    groups = re.match(pattern, email_text, re.IGNORECASE)
    salutation = None
    if not groups is None:
        if "salutation" in groups.groupdict().keys():
            salutation = groups.groupdict()["salutation"]
    return(salutation)

def get_signature(email_text):    
    
    salutation = get_salutation(email_text)
    if salutation: email_text = email_text[len(salutation):]    
    
    sig_opening_statements = ["best regards",
                              "Thanks and Regards",
                              "warm regards",
                              "kind regards",
                              "regards",
                              "cheers",
                              "many thanks",
                              "thanks",
                              "thanks and regards",
                              "sincerely",
                              "ciao",
                              "Best",
                              "bGIF",
                              "thank you",
                              "thankyou",
                              "talk soon",
                              "cordially",
                              "yours truly",
                              "thanking You",
                              "sent from my iphone",
                              "yours thankfully",
                              "yours sincerely",
                              'thankfully'
                              'Best Wishes'
                              ]

    pattern = "\s*(?P<signature>(" + "|".join(sig_opening_statements) + ")+(.)*)"
    groups = re.search(pattern, email_text, re.IGNORECASE + re.DOTALL)
    signature = None
    if groups:
        if "signature" in groups.groupdict().keys():
            signature = groups.groupdict()["signature"]       
            tmp_sig = signature
            for s in sig_opening_statements:
                if tmp_sig.lower().find(s) == 0:
                    tmp_sig = tmp_sig[len(s):]
            groups = re.search(pattern, tmp_sig, re.IGNORECASE + re.DOTALL)
            if groups: signature = groups.groupdict()["signature"]
        
       
    if not signature:        
        pass
    
    
    body_without_sig = get_body(email_text, check_signature=False)
    if signature==body_without_sig: signature = None
    
    return(signature)

def get_body(email_text, check_salutation=True, check_signature=True, check_reply_text=True):
    email_text=email_text.replace("\\"," ")
    if check_salutation:
        sal = get_salutation(email_text)
        print(sal)
        if sal: email_text = email_text[len(sal):]
    
    if check_signature:
        sig = get_signature(email_text)
        if sig: email_text = email_text[:email_text.find(sig)]          
    return( email_text)

print(get_body("Dear Sir/Ma'am, The wifi in my room is not working. I live in Room 7 of SH-3. Please help me with this. Thanks and Regards, XYZ"))




