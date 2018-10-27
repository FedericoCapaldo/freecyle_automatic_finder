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

def get_links(group_name):
        req_url = get_group_link(group_name)
        links = fetch_titles(req_url)
        relevant_posts = get_relevantish_titles(links)
        return relevant_posts

def get_group_link(name):
    return "https://groups.freecycle.org/group/" + name + "/posts/offer"

def get_all_posts_for_each_group(group_names):
        group_map = {}
        for group_name in group_names:
            try:
                print(f"fetching from {group_name}...")
                group_map[group_name] = get_links(group_name)
            except:
                print(f"Error fetching data from {group_name}")
        return group_map


def perform_multiple_matching(stuff_I_want, group_names, posts_by_group):
        for word in stuff_I_want:
            print("---->", word.upper())
            for group_name in group_names:
                if group_name in posts_by_group:
                    matched_posts = match(posts_by_group[group_name], word)
                    matched_posts and print(f"{group_name}: ", matched_posts)
                else:
                    print(f"Data not found in {group_name}. Check that posts were downloaded correctly for this group.")
            print()

if __name__ == "__main__":
    group_names = [ "CityOfLondon",
                    "LewishamUK",
                    "GreenwichUK",
                    "SouthwarkUK",
                    "LambethUK",
                    "TowerHamletsUK",
                    "WestminsterUK",
                    "HammersmithandFulhamUK",
                    "KensingtonandChelseaUK",
                    "HackneyUK",
                    "EalingUK",
                    "KentishtownUK",
                    "BarkingandDagenham" ]

    posts_by_group = get_all_posts_for_each_group(group_names)

    stuff_I_want = ["kitchen"]
    perform_multiple_matching(stuff_I_want, group_names, posts_by_group)
