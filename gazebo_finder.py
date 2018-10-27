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

def match(posts, my_desire):
        toRet = []
        for p in posts:
            p.string = p.string.lower()
            if my_desire in p.string:
                 toRet.append(p.get("href"))
        return toRet

def execute_find_routine(url, wanted):
        links = fetch_titles(url)
        relevant_posts = get_relevantish_titles(links)
        matched = match(relevant_posts, wanted)
        return matched

def get_group_link(name):
    return "https://groups.freecycle.org/group/" + name + "/posts/offer"


if __name__ == "__main__":
    group_names = [ "CityOfLondon",
                    "LewishamUK",
                    "GreenwichUK",
                    "SouthwarkUK",
                    "LambethUK",
                    "TowerHamletsUK",
                    "WestminsterUK",
                    "HammersmithandFulhamUK",
                    "errorSite"
                    "KensingtonandChelseaUK"
                    "HackneyUK",
                    "EalingUK",
                    "KentishtownUK",
                    "BarkingandDagenham" ]

    for group_name in group_names:
        print(group_name + ": ", execute_find_routine(get_group_link(group_name), "chair"))


    # relevant_posts = [(s.lower()) for s in relevant_titles]
    # print(lower_titles)
