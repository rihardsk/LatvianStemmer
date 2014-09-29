__author__ = 'rihards'

'''
 Original Java code can be found in https://github.com/apache/lucene-solr
 Ported to Python by Rihards Krišlauks

 * Light stemmer for Latvian.
 * <p>
 * This is a light version of the algorithm in Karlis Kreslin's PhD thesis
 * <i>A stemming algorithm for Latvian</i> with the following modifications:
 * <ul>
 *   <li>Only explicitly stems noun and adjective morphology
 *   <li>Stricter length/vowel checks for the resulting stems (verb etc suffix stripping is removed)
 *   <li>Removes only the primary inflectional suffixes: case and number for nouns 
 *       case, number, gender, and definitiveness for adjectives.
 *   <li>Palatalization is only handled when a declension II,V,VI noun suffix is removed.
 * </ul>
'''


class Affix:
    def __init__(self, affix, vc, palatalizes):
        self.affix = affix
        self.vc = vc
        self.palatalizes = palatalizes

'''
Stem a latvian word. returns the new adjusted length.
'''

affixes = [
    Affix("ajiem", 3, False),
    Affix("ajai", 3, False),
    Affix("ajam", 2, False),
    Affix("ajām", 2, False),
    Affix("ajos", 2, False),
    Affix("ajās", 2, False),
    Affix("iem", 2, True),
    Affix("ajā", 2, False),
    Affix("ais", 2, False),
    Affix("ai", 2, False),
    Affix("ei", 2, False),
    Affix("ām", 1, False),
    Affix("am", 1, False),
    Affix("ēm", 1, False),
    Affix("īm", 1, False),
    Affix("im", 1, False),
    Affix("um", 1, False),
    Affix("us", 1, True),
    Affix("as", 1, False),
    Affix("ās", 1, False),
    Affix("es", 1, False),
    Affix("os", 1, True),
    Affix("ij", 1, False),
    Affix("īs", 1, False),
    Affix("ēs", 1, False),
    Affix("is", 1, False),
    Affix("ie", 1, False),
    Affix("u", 1, True),
    Affix("a", 1, True),
    Affix("i", 1, True),
    Affix("e", 1, False),
    Affix("ā", 1, False),
    Affix("ē", 1, False),
    Affix("ī", 1, False),
    Affix("ū", 1, False),
    Affix("o", 1, False),
    Affix("s", 0, False),
    Affix("š", 0, False)
]

'''
    * Most cases are handled except for the ambiguous ones:
    * <ul>
    *  <li> s -> š
    *  <li> t -> š
    *  <li> d -> ž
    *  <li> z -> ž
    * </ul>
    */
'''


def un_palatalize(s, length):
    # we check the character removed: if its -u then
    # its 2,5, or 6 gen pl., and these two can only apply then.
    if s[length] == 'u':
        # kš -> kst
        if endswith(s, length, "kš"):
            length += 1
            s[length - 2] = 's'
            s[length - 1] = 't'
            return length
        elif endswith(s, length, "ņņ"):
            s[length - 2] = 'n'
            s[length - 1] = 'n'
            return length

    # otherwise all other rules
    if endswith(s, length, "pj")\
            or endswith(s, length, "bj")\
            or endswith(s, length, "mj")\
            or endswith(s, length, "vj"):
        # labial consonant
        return length - 1
    elif endswith(s, length, "šņ"):
        s[length - 2] = 's'
        s[length - 1] = 'n'
        return length
    elif endswith(s, length, "žņ"):
        s[length - 2] = 'z'
        s[length - 1] = 'n'
        return length
    elif endswith(s, length, "šļ"):
        s[length - 2] = 's'
        s[length - 1] = 'l'
        return length
    elif endswith(s, length, "žļ"):
        s[length - 2] = 'z'
        s[length - 1] = 'l'
        return length
    elif endswith(s, length, "ļņ"):
        s[length - 2] = 'l'
        s[length - 1] = 'n'
        return length
    elif endswith(s, length, "ļļ"):
        s[length - 2] = 'l'
        s[length - 1] = 'l'
        return length
    elif s[length - 1] == 'č':
        s[length - 1] = 'c'
        return length
    elif s[length - 1] == 'ļ':
        s[length - 1] = 'l'
        return length
    elif s[length - 1] == 'ņ':
        s[length - 1] = 'n'
        return length

    return length


def endswith(s, length, suffix):
    return s[:length].endswith(suffix)


def num_vowels(s):
    vowels = {}.fromkeys('aāeēiouūAĀEĒIĪOUŪ')
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def stem(s):
    numvowels = num_vowels(s)
    length = len(s)

    for affix in affixes:
        if numvowels > affix.vc and length >= len(affix.affix) + 3 and endswith(s, length, affix.affix):
            length -= len(affix.affix)
            return un_palatalize(s, length) if affix.palatalizes else length

