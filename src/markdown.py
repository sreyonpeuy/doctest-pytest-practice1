'''
All the functions in this file convert markdown syntax into html.
Implementing these functions will give you practice learning
the correct markdown syntax.
'''


def compile_italic_underscore(line):
    '''
    Convert "_italic_" into "<i>italic</i>".

    >>> compile_italic_underscore('_This is italic!_ This is not italic.')
    '<i>This is italic!</i> This is not italic.'
    >>> compile_italic_underscore('_This is italic!_')
    '<i>This is italic!</i>'
    >>> compile_italic_underscore('This is _italic_!')
    'This is <i>italic</i>!'
    >>> compile_italic_underscore('This is not _italic!')
    'This is not _italic!'
    >>> compile_italic_underscore('_')
    '_'
    >>> compile_italic_underscore('_a_ and _b_')
    '<i>a</i> and <i>b</i>'
    >>> compile_italic_underscore('_a_ and _b')
    '<i>a</i> and _b'
    >>> compile_italic_underscore('no underscores here')
    'no underscores here'
    >>> compile_italic_underscore('')
    ''
    '''
    underscores = line.count('_')
    converts = underscores - (underscores % 2)
    accumulator = ''
    inside_italic = False
    count = 0
    for x in line:
        if x == '_' and count < converts:
            if inside_italic:
                accumulator += '</i>'
            else:
                accumulator += '<i>'
            inside_italic = not inside_italic
            count += 1
        else:
            accumulator += x
    return accumulator


def compile_bold_stars(line):
    '''
    Convert "**bold**" to "<b>bold</b>".

    >>> compile_bold_stars('**This is bold!** This is not bold.')
    '<b>This is bold!</b> This is not bold.'
    >>> compile_bold_stars('**This is bold!**')
    '<b>This is bold!</b>'
    >>> compile_bold_stars('This is **bold**!')
    'This is <b>bold</b>!'
    >>> compile_bold_stars('This is not **bold!')
    'This is not **bold!'
    >>> compile_bold_stars('**')
    '**'
    >>> compile_bold_stars('**a** **b**')
    '<b>a</b> <b>b</b>'
    >>> compile_bold_stars('a * b * c')
    'a * b * c'
    >>> compile_bold_stars('***')
    '***'
    '''
    twostar = line.count('**')
    con = twostar - (twostar % 2)
    accumulator = ''
    c = 0
    in_bold = False
    skip = False
    for i, x in enumerate(line):
        if skip:
            skip = False
            continue
        if (x == '*' and i + 1 < len(line) and  line[i + 1]  == '*' and c < con):
            if (in_bold):
                accumulator += '</b>'
            else:
                accumulator += '<b>'
            in_bold = not in_bold
            con += 1
            skip = True
        else:
            accumulator += x
    return accumulator


def compile_links(line):
    '''
    Add <a> tags.

    HINT:
    The links and images are potentially more complicated
    because they have many types of delimeters: `[]()`.
    These delimiters are not symmetric, however, so we can more easily
    find the start and stop locations using the strings find function.

    >>> compile_links('[a](1) and [b](2)')
    '<a href="1">a</a> and <a href="2">b</a>'
    >>> compile_links('(parens) then [t](u)')
    '(parens) then <a href="u">t</a>'
    >>> compile_links('nothing here](oops)')
    'nothing here](oops)'
    '''
    accumulator = ''
    skip_until = -1
    for i, x in enumerate(line):
        if i <= skip_until:
            continue
        if x == '[':
            c_b = line.find(']', i)
            if (c_b != -1 and c_b + 1 < len(line) and line[c_b + 1] == '('):
                open_paren = c_b + 1
                close_paren = line.find(')', open_paren)
            if close_paren != -1:
                text = line[i + 1:c_b]
                url = line[open_paren + 1:close_paren]
                accumulator += f'<a href="{url}">{text}</a>'
                skip_until = close_paren
                continue
        accumulator += x
    return accumulator
