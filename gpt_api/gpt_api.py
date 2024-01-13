from openai import OpenAI


def summarize_link(url):
    client = OpenAI(api_key="input-api-key")
    completion = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are an article summary assistant, skilled in finding key information on "
                                          "each url and providing it for the user."},
            {"role": "user", "content": f"look at this {url} and provide answers to the following: -title:. -category:"
                                        f" a word that is not 'News' eg. business, politics, technology, etc. "
                                        f"-length: short, medium, long. -summary: one sentence. "
                                        f"-url: the link I gave you."}
        ]
    )
    ans = completion.choices[0].message.content
    return ans


def find_links(url):
    client = OpenAI(api_key="input-api-key")
    completion = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are a web browsing assistant, skilled in finding different news "
                                          "articles and providing the url for the user."},
            {"role": "user", "content": f"from {url} find me the 5 newest links and return each of their urls ONLY, "
                                        f"no title or any other information needed, do not user hyperlink just the URL "
                                        f"is enough, do not provide any description text either, "
                                        f"I only want the 5 links"}
        ]
    )
    links = completion.choices[0].message.content
    return links


# find_links('https://ca.news.yahoo.com/world/')
# summarize_link('https://ca.news.yahoo.com/huge-ring-galaxies-challenges-thinking-023325122.html')


def store_data(data_input, infos):
    infos = infos.split('\n')
    for info in infos:
        info = info[2:]
        info.split(': ', 1)
        data_input[info[0]] = info[1]


def main():
    links = find_links('https://ca.news.yahoo.com/world/')
    links = links.split('\n')
    data = {}
    for link in links:
        info = summarize_link(link)
        store_data(data, info)
    return data


if __name__ == '__main__':
    main()
