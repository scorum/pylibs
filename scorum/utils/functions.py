import itertools
import operator


def most_common(elems):
    """
    Get most common element in list.
    Source: https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list

    :param list elems:
    :return: Most common element
    """
    # get an iterable of (item, iterable) pairs
    sl = sorted((x, i) for i, x in enumerate(elems))
    # print 'SL:', SL
    groups = itertools.groupby(sl, key=operator.itemgetter(0))

    # auxiliary function to get "quality" for an item
    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(elems)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        # print 'item %r, count %r, minind %r' % (item, count, min_index)
        return count, -min_index

    # pick the highest-count/earliest item
    return max(groups, key=_auxfun)[0]
