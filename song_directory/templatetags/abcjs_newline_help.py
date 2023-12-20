from django import template

register=template.Library()

def js_newline(value): 
    #Replaces python's \n(which jinja interprets as a new line)
    #with "\\n", which jinja interprets as \n. Required to make abcjs work
    #with the database's stored abc files.
    out=value
    out=out.replace("\n","\\n")
    out=out.replace('\"','\\"')
    #print(out)
    return out

register.filter("js_newline", js_newline)