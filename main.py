# Завдання 1
# Створіть програму роботи зі словником.
# Наприклад, англо-іспанський, французько-німецький
# або інша мовна пара.
# Програма має:
# ■ надавати початкове введення даних для словника;
# ■ відображати слово та його переклади;
# ■ дозволяти додавати, змінювати, видаляти
# переклади слова;
# ■ дозволяти додавати, змінювати, видаляти слово;
# ■ відображати топ-10 найпопулярніших слів
# (визначаємо популярність спираючись на лічильник
# звернень);
# ■ відображати топ-10 найнепопулярніших слів
# (визначаємо непопулярність спираючись на лічильник
# звернень).
# Використовуйте дерево для виконання цього
# завдання.
import bintrees

class Dictionary:
    def __init__(self):
        self.tree = bintrees.AVLTree()

    def add_word(self, word, translations):
        word_data = self.tree.get(word)
        if word_data is not None:
            word_data['translations'] = translations
        else:
            self.tree.insert(key=word, value={'translations': translations, 'popularity': 0})
        self.increase_popularity(word)

    def update_translations(self, word, translations):
        if word in self.tree:
            self.tree[word]['translations'] = translations
        else:
            print('Слова немає у словнику')

    def remove_word(self, word):
        if word in self.tree:
            self.tree.remove(word)
        else:
            print('Слова немає у словнику')

    def display_word_translations(self, word):
        if word in self.tree:
            print(f'Слово: "{word}", переклад: {", ".join(self.tree[word]["translations"])}')
        else:
            print('Слова немає у словнику')

    def increase_popularity(self, word):
        if word in self.tree:
            self.tree[word]['popularity'] += 1
        else:
            print('Слова немає у словнику.')

    def top_popular(self):
        top_words = self.tree.items()[-10:] if len(self.tree) > 10 else self.tree.items()
        print("Топ 10 популярних слів:")
        for word, data in top_words:
            print(word, "-", data["popularity"])

    def top_unpopular(self):
        unpopular_words = self.tree.items()[:10] if len(self.tree) > 10 else []
        print("Топ 10 непопулярних слів:")
        for word, data in unpopular_words:
            print(word, "-", data["popularity"])


dictionary = Dictionary()
dictionary.add_word("incredible", ["неймовірно"])
dictionary.add_word("cat", ["кіт", "кішка"])
dictionary.add_word("hello", ["привіт"])
dictionary.add_word("world", ["світ"])

dictionary.display_word_translations("cat")

dictionary.add_word("cat", "котик")

dictionary.remove_word("world")

dictionary.top_popular()

dictionary.top_unpopular()


