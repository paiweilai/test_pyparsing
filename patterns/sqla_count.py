import pyparsing as pp


DOT = '.'
LPAREN, RPAREN = '(', ')'
SESSION = 'session'
QUERY = 'query'
FILTER = 'filter'
COUNT = 'count'

SESSION_QUERY = SESSION + DOT + QUERY + LPAREN
QUERY_EXPRS = pp.SkipTo(RPAREN)
FILTER_CALL = RPAREN + DOT + FILTER + LPAREN
FILTER_EXPRS = pp.SkipTo(RPAREN)
COUNT_CALL = RPAREN + DOT + COUNT + LPAREN + RPAREN


def find(text):
    return (
        SESSION_QUERY +
        QUERY_EXPRS +
        FILTER_CALL +
        FILTER_EXPRS +
        COUNT_CALL
    ).scanString(text)


def replace(found_string):
    session_query, _, filter_call, filter_exprs, _ = found_string
    return (
        session_query.rstrip() +
        'sqlalchemy.func.count()' +
        filter_call.rstrip() +
        _pretty_one_line(filter_exprs) +
        ').scalar()'
    )


def _pretty_one_line(exprs):
    return ' '.join(exprs.split()).rstrip().rstrip(',')
