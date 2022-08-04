for row in table.xpath("//tr"):
    try:
        print(row.xpath("td//text()")[0].extract())
    except IndexError:
        pass
