# my_list = []
# my_list[4] = "Hi"
# print(my_list[4])
# The list above must contain items for "Hi" to be added to the 4th position

my_list = ["A", "B", "C", "D", "E"] # <-- List
my_list.append("F")

my_list = my_list + ["G"]
print(my_list)
print(len(my_list))

song_genres = ("Rock", "Classical", "Alternative") #<-- Tuple
print(song_genres)

for g in song_genres:
    print(g)

# LIST --> You can change it
# TUPLE --> You cannot change it (immutable)
    #constant
    #speed