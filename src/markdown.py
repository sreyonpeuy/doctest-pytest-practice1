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
    # odd count: last one is literal
    '<i>a</i> and _b'
    >>> compile_italic_underscore('no underscores here')
    'no underscores here'
    >>> compile_italic_underscore('')
    ''
    '''
    accumulator = ''
    inside_italic = False

    for x in line:
        if x == '_':
            if inside_italic:
                accumulator += '</i>'
            else:
                accumulator += '<i>'

            inside_italic = not inside_italic
        else:
            accumulator += x

    return print(accumulator)


'''
compile_italic_underscores('_This is italic!_ This is not italic.')
    accumulator = ''
    skip_until = -1
    for i, x in enumerate(line):
        if i <= skip_until:
            continue
        if x == '_':
            close = line.find('_', i + 1)
            if close != -1:
                accumulator += '<i>' + line[i + 1:close] + '</i>'
                skip_until = close
            else:
                accumulator += x
        else:
            accumulator += x
    return accumulator
'''


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
    accumulator = ''
    j_edited = False
    for i, x in enumerate(line):
        if x == '*' and line[i + 1] == '*':
            accumulator += '<b>'
            j_edited = True
        else:
            if not j_edited:
                accumulator += x
            j_edited = False
    return print(accumulator)


def compile_links(line):
    '''
    Add <a> tags.

    HINT:
    The links and images are potentially more complicated
    because they have many types of delimeters: `[]()`.
    These delimiters are not symmetric, however, so we can more easily
    find the start and stop locations using the strings find function.

    >>> compile_links('Click on the [course webpage](https:
    ... //github.com/mikeizbicki/cmc-csci040)!')
    'Click on the <a href="https://github.com/mikeizbicki
    /cmc-csci040">course webpage</a>!'
    >>> compile_links('[course webpage](https://github.com/
    ... mikeizbicki/cmc-csci040)')
    '<a href="https://github.com/mikeizbicki/
    cmc-csci040">course webpage</a>'
    >>> compile_links('this is wrong: [course webpage]
    ... (https://github.com/mikeizbicki/cmc-csci040)')
    'this is wrong: [course webpage]    (https://github.
    com/mikeizbicki/cmc-csci040)'
    >>> compile_links('this is wrong: [course webpage]
    ... (https://github.com/mikeizbicki/cmc-csci040')
    'this is wrong: [course webpage](https:
        //github.com/mikeizbicki/cmc-csci040'
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
            close_bracket = line.find(']', i)

            open_paren = -1
            if close_bracket != -1:
                open_paren = line.find('(', close_bracket)

            close_paren = -1
            if open_paren != -1:
                close_paren = line.find(')', open_paren)

            has_bracket = close_bracket != -1
            has_paren = open_paren == close_bracket + 1
            has_close_paren = close_paren != -1

            if has_bracket and has_paren and has_close_paren:
                text = line[i + 1:close_bracket]
                url = line[open_paren + 1:close_paren]
                accumulator += f'<a href="{url}">{text}</a>'
                skip_until = close_paren
            else:
                accumulator += x
        else:
            accumulator += x

    return print(accumulator)
