'''
Your function should find all of the words
that appear in both strings. The result must be represented
as a string of words separated by commas in alphabetic order.

Example:

checkio("hello,world", "hello,earth") == "hello"
checkio("one,two,three", "four,five,six") == ""
checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two"

'''


def checkio(first, second):
    commonList = ""
    commonList = [word for word in first.split(",")
                  if word in second.split(",")]
    if len(commonList) > 1:
        return ','.join(sorted(commonList))
    else:
        return ''.join(commonList)


# These "asserts" using only for self-checking \
# and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three",
                   "four,five,one,two,six,three") == "one,three,two", "1 2 3"
