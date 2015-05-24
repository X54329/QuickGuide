from pyteaser import SummarizeUrl, Summarize
import sys
import duckduckgo as d

#q = sys.argv[1]
#for i in range(2, len(sys.argv)-1):
#    q += " " + sys.argv[i]

#print q

#3g = d.get_zci(q, True)

#if "(" in g:
#    print g
#else:
#    print "5 Sentence Summary:"
#    print SummarizeUrl(g, 5)
#    print "Extended Summary:"
#    print SummarizeUrl(g, 15)
#    print "Whole Article:"
#    print SummarizeUrl(g, 1000)


def shortSummaryFromQuery(query):
	g = d.get_zci(query, True)
	if "(" in g:
		return Summarize(query, g, 5)
	else:
		return SummarizeUrl(g, 5)


def longSummaryFromQuery(query):
	g = d.get_zci(query, True)
	if "(" in g:
		return Summarize(query, g, 15)
	else:
		return SummarizeUrl(g, 15)


def wholeArticleFromQuery(query):
	g = d.get_zci(query, True)
	if "(" in g:
	 	return Summarize(query, g, 1500)
	else:
		return SummarizeUrl(g, 1500)
