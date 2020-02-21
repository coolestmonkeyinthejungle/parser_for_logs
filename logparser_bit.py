import re


def string_parse(s):
    '''Our string parser'''
    if re.fullmatch(r'(?:(?:\\\||[^|])*\|){7}(?: [^=| ]+=(?:[^=]|\\=)+)*',s):
        l = re.fullmatch(r'((?:\\\||[^|])*)\|((?:\\\||[^|])*)\|((?:\\\||[^|])*)\|((?:\\\||[^|])*)\|((?:\\\||[^|])*)\|((?:\\\||[^|])*)\|((?:\\\||[^|])*)\|(.*)',s)
        d = dict()
        for i in range(1,8):
            d['param{0}'.format(i)] = l.group(i).replace(r"\|", "|")
        if l.group(8) != '':
            m = re.findall(r'([^=| ]+=(?:[^=]|\\=)+ )', l.group(8) + ' ')
            for p in m:
                key, value = p[0:-1].split("=",1)
                d[key] = value.replace(r"\=", "=")
        return d
    else:
        return s


if __name__ == "__main__":
    print(string_parse(r'a|b | b|cc|d d d|e|f|g| key1=value1 key2=value2 key3=value3 keyN=valueN'))
