file = open('./file.txt', 'w')
file.write("yippee!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! :D")
file.close()

# filter = Filters(
#     start_date = "2020-05-01",
#     end_date = "2020-05-02",
#     num_records = 250,
#     keyword = "climate change",
#     domain = ["bbc.co.uk", "nytimes.com"],
#     country = ["UK", "US"],
#     theme = "GENERAL_HEALTH",
#     near = near(10, "airline", "carbon"),
#     repeat = repeat(5, "planet")
# )

# gd = GdeltDoc()

# # Search for articles matching the filters
# articles = gd.article_search(filter)

# print(articles)

# # Get a timeline of the number of articles matching the filters
# timeline = gd.timeline_search("timelinevol", filter)