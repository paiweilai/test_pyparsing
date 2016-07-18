import pyparsing as pp


DOT = '.'
LPAREN = pp.Suppress('(')
RPAREN = pp.Suppress(')')
SESSION = 'session'
QUERY = 'query'
FILTER = 'filter'
COUNT = 'count'

SESSION_QUERY = SESSION + DOT + QUERY
QUERY_EXPRS = LPAREN + pp.SkipTo(RPAREN) + RPAREN
FILTER_CALL = DOT + FILTER
FILTER_EXPRS = LPAREN + pp.SkipTo(RPAREN) + RPAREN
COUNT_CALL = DOT + COUNT + LPAREN + RPAREN


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
        session_query +
        '(sqlalchemy.func.count())' +
        filter_call.rstrip() + "(" +
        _pretty_one_line(filter_exprs) +
        ').scalar()'
    )


def _pretty_one_line(exprs):
    return ' '.join(exprs.split()).rstrip().rstrip(',')
