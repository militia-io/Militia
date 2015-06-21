import militia.tools.facebook
import militia.tools.twitter
import militia.tools.google
import militia.tools.wikipedia

def attempts(load):
	try:
		load
		return 'Succeeded'
	except Exception:
		return 'Failed'

#Testing credentials	
check = militia.tools
platforms = [('Facebook',check.facebook.Load_FB), ('Twitter', check.twitter.twitterObj), ('Google Maps', check.google.Gmap), ('Wikipedia', check.wikipedia.wikiObj)]
for i in platforms:
	print '%s: %s' % (i[0], attempts(i[1]))


