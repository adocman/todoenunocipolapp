import re

def deEmojify(palabra):
    regrex_pattern = re.compile(pattern = "["
        u"\<U+0001F600>-\<U+0001F64F>"  # emoticons
        u"\<U+0001F300>-\<U+0001F5FF>"  # symbols & pictographs
        u"\<U+0001F680>-\<U+0001F6FF>"  # transport & map symbols
        u"\<U+0001F1E0>-\<U+0001F1FF>"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',palabra)
