# example python script that generates a table in markdown and saves it as table.md

rows = [
    "| Status | Name | Icon |",
    "|---|---|---|",
    "|OK|Test 1| ![badge](https://img.shields.io/badge/test-ok-blue)",
    "|TODO|Test 2| ![badge](https://img.shields.io/badge/test-todo-yellow)",
    "|FAILING|Test 3| ![badge](https://img.shields.io/badge/test-failing-red)",
]

with open("table.md", "w", encoding="utf-8") as f:
    for row in rows:
        print(row, file=f)
