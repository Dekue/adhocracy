import urllib
import re
from webhelpers.text import truncate
from unicodedata import normalize, category
from adhocracy.forms import FORBIDDEN_NAMES

#INVALID_CHARS = re.compile(u"[\?#\&]", re.U)

def chr_filter(ch): 
    """ Filter by unicode character category. """
    if ch == u'_':
        return ch
    cat = category(ch)[0].upper()
    if cat in ['Z']:
        return u'_' # replace spaces
    if cat in ['P']:
        return u'' # remove punctuation
    return ch


def variant_normalize(variant):
    var = escape(variant)
    if var.lower() in FORBIDDEN_NAMES:
        return u""
    return var


def title2alias(title, pseudo=u'pg'):
    #title = urllib.unquote(title)
    title = escape(title)
    #title = INVALID_CHARS.sub(u"", title)
    if not len(title) or (title.lower() in FORBIDDEN_NAMES):
        return pseudo
    try:
        tint = int(title)
        return pseudo + tint
    except:
        return title


def label2alias(label):
    title = escape(label)
    return title[:40]


def escape(title):
    title = unicode(title).strip()
    title = normalize('NFKD', title)
    title = u''.join([chr_filter(c) for c in title])
    title = normalize('NFKC', title)
    return title
