# Parser for logs in convenient format
This is a parser for logs that accept it by HTTP. Parser add string to log file if it fit for format.
Format gonna be like this a|b b|cc|d d d|e|f|g| key1=value1 key2=value2 key3=value3 … keyN=valueN.
There are also some requirements for it:
* It has fix number of pipes - 7 ( It could be also shield pipes \| in it)
* There are some pairs of key=value after last pipe
* Pairs are divided by space
* = symbol don't has space before and after it
* Key could be any value apart from = and |
* = symbol in value could be shieldeded by \
Correct strings are saved in json format like {param1: a, param2: b b, param3: cc, param4: d d d, param5: e,
param6: f, param7: g, key1: value1, key2: value2, key3: value3, …, keyN: valueN}
Parser is listen on 8443 port.
Wrong strings are also saved in separate file.
