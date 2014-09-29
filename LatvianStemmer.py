__author__ = 'rihards'

'''
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


class LatvianStemmer:
    '''
    Stem a latvian word. returns the new adjusted length.
    '''
    @staticmethod
    def stem(s):
        numVovels = LatvianStemmer.numVovels(s)
        length = len(s)

        for affix in LatvianStemmer.affixes:
            if numVovels > affix.vc and length >= len(affix.affix) + 3 and s.endswith(affix.affix):
                length -= len(affix.affix)
                return LatvianStemmer.unpalatalize(s, length) if affix.palatalizes else length

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
    @staticmethod
    def unpalatalize(s, length):
        # we check the character removed: if its -u then
        # its 2,5, or 6 gen pl., and these two can only apply then.
        if s[length] == 'u':
            # kš -> kst
            if LatvianStemmer.endsWith(s, length, "kš"):
                length += 1
                s[length - 2] = 's'
                s[length - 1] = 't'
                return length
            elif LatvianStemmer.endsWith(s, length, "ņņ"):
                s[length - 2] = 'n'
                s[length - 1] = 'n'
                return length

        # otherwise all other rules
        if LatvianStemmer.endsWith(s, length, "pj") or LatvianStemmer.endsWith(s, length, "bj") or LatvianStemmer.endsWith(s, length, "mj") or LatvianStemmer.endsWith(s, length, "vj"):
            # labial consonant
            return length - 1
        elif LatvianStemmer.endsWith(s, length, "šņ"):
            s[length - 2] = 's'
            s[length - 1] = 'n'
            return length
        elif LatvianStemmer.endsWith(s, length, "žņ"):
            s[length - 2] = 'z'
            s[length - 1] = 'n'
            return length
        elif LatvianStemmer.endsWith(s, length, "šļ"):
            s[length - 2] = 's'
            s[length - 1] = 'l'
            return length
        elif LatvianStemmer.endsWith(s, length, "žļ"):
            s[length - 2] = 'z'
            s[length - 1] = 'l'
            return length
        elif LatvianStemmer.endsWith(s, length, "ļņ"):
            s[length - 2] = 'l'
            s[length - 1] = 'n'
            return length
        elif LatvianStemmer.endsWith(s, length, "ļļ"):
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

    @staticmethod
    def endsWith(s, length, suffix):
        return s[:length].endswith(suffix)

    @staticmethod
    def numVovels(s):
        vowels = {}.fromkeys('aāeēiouūAĀEĒIĪOUŪ')
        count = 0
        for char in s:
            if char in vowels:
                count += 1
        return count



class Affix:
    def __init__(self, affix, vc, palatalizes):
        self.affix = affix
        self.vc = vc
        self.palatalizes = palatalizes

