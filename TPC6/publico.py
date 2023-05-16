import newspaper

url = "https://www.publico.pt/"


publico = newspaper.build(url)

for article in publico.articles:
    print(article.url, article.title)
    ar = newspaper.article.Article(article.url)
    ar.download()
    ar.parse()
    print(f'''
          <arcticle>
          <url>{article.url}</url>
          <autor>{ar.authors}</autor>
          <date>{ar.publish_date}</date>
          <text>{ar.text}</text>
          </article>
          ''', file=open("publico.xml", "a"))
