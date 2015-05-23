from requests import get
from collections import Counter
from lxml import html
import sys

reddit_request = get(sys.argv[1])
#wiki_request = get('http://en.wikipedia.org/wiki/Information_extraction')

parsed_doc = html.fromstring(reddit_request.content)

    # In SQL-like terms: select all parents in <body>
parent_elements = parsed_doc.xpath('//body//*/..')

parents_with_children_counts = []

for parent in parent_elements:
        children_counts = Counter([child.tag for child in parent.iterchildren()])
        parents_with_children_counts.append((parent, children_counts))

    # This line, one could say, is what wraps this data-extraction 
    # algorithm up as a maximization/optimization algorithm
parents_with_children_counts.sort(# x[1].most_common(1)[0][1] gets the frequency value
                                key=lambda x: x[1].most_common(1)[0][1], 
                                reverse=True)

def stringify_children(node):
    from lxml.etree import tostring
    from itertools import chain
    parts = ([node.text] +
            list(chain(*([c.text, tostring(c), c.tail] for c in node.getchildren()))) +
            [node.tail])
    # filter removes possible Nones in texts and tails
    return ''.join(filter(None, parts))

print stringify_children(parents_with_children_counts[0][0])
#print stringify_children(parents_with_children_counts[0][0][1])
#print stringify_children(parents_with_children_counts[0][0][2])
#print stringify_children(parents_with_children_counts[0][0][3])
#print stringify_children(parents_with_children_counts[0][0][4])
