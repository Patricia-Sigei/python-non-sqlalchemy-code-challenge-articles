class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            print("Name must be a non-empty string")
        self._name = name  

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list(set([magazine.category for magazine in self.magazines()]))
        return categories if categories else None


class Magazine:
    all_magazines = []  

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            print ("Name must be a string between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            print ("Category must be a non-empty string")
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)

    @classmethod
    def top_publisher(cls):
        magazines_with_articles = {mag: 0 for mag in cls.all_magazines}
        for article in Article.all_articles:
            magazines_with_articles[article.magazine] += 1
        return max(magazines_with_articles, key=magazines_with_articles.get, default=None)

    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self.articles())
        return [author for author, count in author_counts.items() if count > 2] or None


class Article:
    all_articles = []  

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            print ("Author must be an instance of the Author class")
        if not isinstance(magazine, Magazine):
             print ("Magazine must be an instance of the Magazine class")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            print ("Title must be a string between 5 and 50 characters")
        self.author = author
        self.magazine = magazine
        self._title = title  
        Article.all_articles.append(self)

    @property
    def title(self):
        return self._title
