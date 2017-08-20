# class

##### article variables

##### Article class with __init
class Article:
    author = "마르코"
    view_count = 0

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def read(self):
        self.view_count = self.view_count + 1

article1 = Article("개발", "개발은 쉬어요")
article2 = Article("코칭", "코칭은 쉬어요")
article3 = Article("창업", "창업은 쉬어요")

print(article1.view_count)
article1.read()
print(article1.view_count)

##### Article class inheritance 상속
class BrunchArticle(Article):
    source = "브런치"

    def read(self):
        self.view_count = self.view_count + 2

brunch_article = BrunchArticle("개발", "개발은 쉬어요")
print(brunch_article.title)
print(brunch_article.source)
print(brunch_article.view_count)
brunch_article.read()
print(brunch_article.view_count)
