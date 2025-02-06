def is_palindrome(word):
    cleaned_word = ''.join(e for e in word if e.isalnum()).lower()
    return cleaned_word == cleaned_word[::-1]
print(is_palindrome("lowkey"))
print(is_palindrome("kirarik"))
