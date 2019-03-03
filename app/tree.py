from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import time

# REMOVE RANDOM STRING FUNCTIONS FOR VARIABLES


#target_site = input()


# Ensure target has a page on wikipedia.
def scrape_page(target, limit):
    links = set()
    print('TARGET ====> ' + str(target))
    if 'Wikipedia does not have an article with this exact name' not in str(target):
        target = requests.get('https://en.wikipedia.org/wiki/' + str(target))
        print('https://en.wikipedia.org/wiki/' + str(target))
        soup = BeautifulSoup(target.content, "html.parser")
        links.update([a['href'] for a in soup.find_all('a', href=True)])

    else:
        print('No Results')

    wiki_links = [s for s in links if "/wiki/" in s]
    print('==== START ====')
    for i in wiki_links[:limit]:
        print(i)
    print('==== END ====')
    return wiki_links[0:limit]


# Get blacklist of strings that will exclude links from the final list
def get_blacklist():
    try:
        df = pd.read_csv('blacklist/blacklist.txt', sep='\n', header=None)
        df = df[0].tolist()
    except:
        print('Error: Could not find blacklist (blacklist/blacklist.txt), using "Category:"')
        df = ['Category:']
    return df


# Set blacklist to a variable to avoid pulling blacklist via function every time.
blacklist = get_blacklist()


# Clean list, exclude any strings from the blacklist from the newly generated list.
def clean_list(input, blacklist):
    b = blacklist
    output = [word for word in input if not any(black in word for black in b)]
    return sorted(output)


# Replace remaining elements of URLs with appropriate characters.
def get_topics_from_list(input):
    output = [w.replace('_', ' ').replace('/wiki/', '').replace('%', ' ') for w in input]
    return output


def string_format(input):
    output = str(input).replace('_', ' ')
    return output

# Write list to file.
def write_to_file(topic, input):
    filename = str('data/' + str(string_format(topic)) + '.txt')
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass
    with open(filename, mode="a") as outfile:
        print('Creating list file with topic...')
        for s in get_topics_from_list(clean_list(input, blacklist)):
            outfile.write("%s\n" % s)


def create_list(topic, limit):
    topic = str(topic)
    output = scrape_page(topic, limit)
    output = clean_list(output, blacklist)
    output = get_topics_from_list(output)
    write_to_file(topic, output)
    return output

def link_format(input):
    output = str(input).replace(' ', '_')
    return output

def create_tree(topic, depth, limit):
    topic = str(topic)
    origin = create_list(topic, limit)
    finished_lists = [str(topic)]
    finished_lists.append(origin)

    print('Origin == ' + str(origin))
    for o in origin:
        print('o == ' + str(o))
        print('================>>> create_list(' + link_format(o) + ', limit)')
        create_list(link_format(o), limit)

    # file_list = os.listdir(r"data/")
    #
    # for i in file_list:
    #     for l in finished_lists:
    #         print(str(l) + '==' + str(i))
    #         if l in i:
    #             pass
    #             print('pass')
    #         else:
    #             create_list(i, limit)



create_tree('K-Pop', 1, 50)


# Finished.
print('Finished')
