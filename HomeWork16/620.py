def html(html_tag, string):
    print("<" + html_tag + ">" + string + "</" + html_tag + ">")


a = "strong Python"

html(a.split()[0], a.split()[1])
