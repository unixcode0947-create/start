def count_vowels_and_consonants(text: str) -> dict:
    result = {
        'unli' : 0,
        'undosh' : 0,
    }
    unli_harf = 'aeiouAEIOU'
    for harf in text:
        if harf.isalpha():
            if harf in unli_harf:
                result['unli'] += 1
            else:
                result['undosh'] += 1
    return result

print(count_vowels_and_consonants("Salom Dunyo!"))