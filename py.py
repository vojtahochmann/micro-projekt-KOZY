def markdown_to_html(markdown):
    html = ''
    lines = markdown.split('\n')
    in_block = False

    for line in lines:
        # Headers
        if line.startswith('#'):
            level = line.count('#')
            html += f'<h{level}>{line.strip("# ")}</h{level}>'
        # Lists
        elif line.startswith('* '):
            if not in_block:
                html += '<ul>'
                in_block = True
            html += f'<li>{line[2:]}</li>'
        else:
            if in_block:
                html += '</ul>'
                in_block = False
            html += line + '<br>'
    
    if in_block:
        html += '</ul>'

    return html

markdown_text = """# ahoj kozy

## miluju kozy

Seznam:
* kozy1
* kozy2
"""

html_output = markdown_to_html(markdown_text)
print(html_output)
