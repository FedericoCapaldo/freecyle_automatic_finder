from bs4 import BeautifulSoup
import urllib.request

def fetch_titles(source_url):
    with urllib.request.urlopen(source_url) as url:
        page_content = url.read()
        soup = BeautifulSoup(page_content, "html.parser")

    links = []
    for link in soup.find_all('a'):
        links.append(link)
    return links

def get_relevantish_titles(links):
        relevant_links = list(filter(lambda link: True if "post" in link.get("href") else False, links))
        return [post for post in relevant_links if post.string is not None]

def match(my_desire):
        toRet = []
        for p in relevant_posts:
            p.string = p.string.lower()
            if my_desire in p.string:
                 toRet.append(p.get("href"))
        return toRet

if __name__ == "__main__":
    url = "https://groups.freecycle.org/group/CityOfLondon/posts/offer"
    links = fetch_titles(url)
    relevant_posts = get_relevantish_titles(links)
    matched = match("gazebo")
    print(matched)


    # relevant_posts = [(s.lower()) for s in relevant_titles]
    # print(lower_titles)
