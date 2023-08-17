# Given string
original_string = "112K Followers, 47 Following, 6,067 Posts - See Instagram photos and videos from Uttarakhand Police (@uttarakhandpolice)"

# Split the original string by commas and extract the part containing "Posts"
parts = original_string.split(",")
posts_part = [part.strip() for part in parts if "Posts" in part][0]

# Extract the numeric part from the "Posts" section
numeric_part = posts_part.split()[0]

# Remove commas if present and convert to an integer
number_of_posts = int(numeric_part.replace(",", ""))

# Print the result
print("Number of Posts:", number_of_posts)
