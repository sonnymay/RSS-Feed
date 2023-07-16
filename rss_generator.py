from feedgenerator import Rss201rev2Feed

# Create the new feed
feed = Rss201rev2Feed(
    title="My Cool Feed",
    link="http://www.example.com/coolfeed",
    description="This is my cool feed",
    language="en",
)

# Add some items
feed.add_item(
    title="Hello",
    link="http://www.example.com/hello",
    description="Hello world!",
)

# Write the feed to a file
with open("feed.rss", "w") as fp:
    feed.write(fp, "utf-8")
    