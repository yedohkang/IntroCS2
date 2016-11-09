def final (filename):
    csv = open (filename 'rU')
    content = csv.read()
    csv.close()
    content = content.split("\n")
    content = content.pop(0)
    