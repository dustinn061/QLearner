import random
def main():
    # dictionary based on the 150 most common nouns, verbs, and adjectives. Verbs are not conjugated, user can conjugate themselves to help master their french knowledge.
    EnglishToFrench = {'i': 'je', 'we': 'nous', 'you': 'tu', 'he': 'il', 'it': 'il',
                       'she': 'elle', 'they': 'ils/elles', 'the': 'le/la', 'a': 'un/une',
                       'an': 'un/une', 'some': 'du/de la/des', 'but': 'mais', 'or': 'ou',
                       'and': 'et', 'thus': 'donc', 'therefore': 'donc', 'neither': 'ni', 'because': 'car',
                       'am': 'suis', 'are': 'es/est/êtes/sommes/sont', 'power': 'pouvoir',
                       'duty': 'devoir', 'thing': 'une chose', 'thanks': 'merci', 'few': 'peu',
                       'man': 'homme', 'woman': 'femme', 'time': 'temps', 'life': 'vie',
                       'day': 'jour', 'anyone': 'personne', 'father': 'père', 'girl': 'fille',
                       'world': 'monde', 'friend': 'ami', 'need': 'besoin', 'child': 'efant',
                       'big': 'grand', 'tall': 'grand', 'mother': 'mère', 'night': 'nuit',
                       'fear': 'peur', 'money': 'argent', 'love': 'amour', 'new': 'nouveau',
                       'history': 'histoire', 'young': 'jeune', 'have': 'avoir', 'do': 'faire',
                       'make': 'faire', 'say': 'dire', 'go': 'aller', 'voir': 'see', 'know': 'savoir',
                       'can': 'pouvoir', 'want': 'vouloir', 'must': 'devoir', 'come': 'venir',
                       'follow': 'suivre', 'speak': 'parler', 'talk': 'parler',
                       'take': 'prendre', 'think': 'croire', 'like': 'aimer', 'pass': 'passer',
                       'think': 'penser', 'arrive': 'arriver', 'give': 'donner', 'call': 'appeler', 'stay': 'rester',
                       'die': 'mourir', 'ask': 'demander', 'understand': 'comprendre', 'go out': 'sortir',
                       'hear': 'entendre', 'play': 'jouer', 'finir': 'finish', 'lose': 'perdre',
                       'small': 'petit', 'large': 'grand', 'young': 'jeune', 'old': 'vieux',
                       'handsome': 'beau', 'beautiful': 'belle', 'strong': 'fort', 'weak': 'faible',
                       'easy': 'facile', 'difficult': 'difficile', 'poor': 'pauvre', 'rich': 'riche',
                       'today': 'aujourd\'hui', 'as': 'aussi', 'a lot': 'beaucoup', 'already': 'déjà ', 'very': 'très',
                       'hello': 'bonjour'}
    FrenchToEnglish = {}
    for key in EnglishToFrench:
        FrenchToEnglish[EnglishToFrench[key]] = key


    x = int(input("Enter how many words you would like to practice today: "))
    i = 0
    while (i < x):
        french, english = random.choice(list(FrenchToEnglish.items()))
        print(french)
        answer = input('Enter your word: ').strip().lower()
        while (answer != english):
            answer = input("Try Again: ").strip().lower()
        i = i + 1


main()