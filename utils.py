import newspaper
import sqlite3

from newspaper import Article


def get_all(query):
    conn = sqlite3.connect("data/newsdb.db")
    data = conn.execute(query).fetchall()
    conn.close()

    return data


def get_news_by_id(news_id):
    conn = sqlite3.connect("data/newsdb.db")
    sql = '''
    select N.subject,N.description,N.image,N.original_url,C.name,C.url
    from news N inner join category C on
    N.category_id = C.id 
    where N.id = ?
    '''
    news = conn.execute(sql, (news_id,)).fetchone()
    conn.close()

    return news


def add_comment(news_id, content):
    conn = sqlite3.connect("data/newsdb.db")
    sql = """
    INSERT INTO comment(content, news_id)
    VALUES (?, ?)
    """
    conn.execute(sql, (content, news_id))
    conn.commit()
    conn.close()


def add_news(conn, url, category_id):
    sql = '''
    INSERT INTO news(subject, description, image, original_url, category_id)
    VALUES (?,?,?,?,?)
    '''
    article = Article(url)
    article.download()
    article.parse()
    conn.execute(sql, (article.title, article.text,
                       article.top_img, article.url, category_id))
    conn.commit()


def get_news_url():
    cats = get_all("select * from category")
    conn = sqlite3.connect("data/newsdb.db")
    for cat in cats:
        cat_id = cat[0]
        url = cat[2]
        cat_paper = newspaper.build(url)
        for article in cat_paper.articles:
            try:
                print("===", article.url)
                add_news(conn, article.url, cat_id)
            except Exception as ex:
                print("ERROR: " + str(ex))
                pass

    conn.close()


if __name__ == "__main__":
    get_news_url()
