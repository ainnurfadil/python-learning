## Data List
teman_teman = {
    "cup":"ucup surucup",
    "tong":"otong surotong",
    "dung":"dudung surudung",
    "sep":"asep so kasyep",
    "cuy":"ucuy surucuy"
}

friends = teman_teman

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# Copy Dictionary
friends = teman_teman.copy()

teman_teman["cup"]="ucup si kweren"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# Pop dictionary (berdasarkan key)
dataAsep = friends.pop("sep")

print(f"teman-teman: {teman_teman}\n")
print(f"asep: {dataAsep}\n")
print(f"friends: {friends}\n")

# Popitem Dictionary (yang terakhir aja)
dataTerakhir = friends.popitem()

print(f"data terakhir: {dataTerakhir}\n")
print(f"friends: {friends}\n")