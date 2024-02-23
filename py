numbers=[1,7,3,5,2,9,10]
even=[]
odd=[]
print(numbers)

# check if even number
for x in numbers:
    if x%2==0:
        even.append(x)
print(even)

# check if odd number
for x in numbers:
    if x%2==1:
        odd.append(x)
print(odd)

# calculate the sum
total=0
for x in numbers:
   total =total+x
print(total)

# calculate the average
average = 0
for x in numbers:
    average = average+x
average = average/len(numbers)
print(average)

# find the max value
max=0
for x in numbers:
    if x >max:
        max=x
print(max)

# find the min value
min=100
for x in numbers:
    if x<min:
        min=x
print(min)

# check if a given number is in the list
num = 3
for x in numbers:
    if num==x:
        inList=True
print(inList)

# Count the number of vowels and consonants
phrase = "hey there i'm the phrase"
vowels=["a","e","i","o","u"]
vowel=0
letters=0
consanants= 0
for x in phrase:
    for y in vowels:
        if  x==y:
            vowel+=1
    if x.isalpha()==True and x!=y:
        letters+=1
consanants=letters-vowel
print(vowel)
print(consanants)

# Palindrome checker
word = "bob"
inverse= word[::-1]
if word == inverse:
     print ("palendrome")
if word != inverse:
        print ("not palendrome")

# Student grade analysis
total=0
average=0
students = [ {"name": "Bob", "grades":  [90, 97, 77]}, 
            {"name": "Theresa", "grades": [98, 89, 93]}, 
            {"name": "Chuck", "grades": [72, 77, 99]} ]
for student in students:
    avg=round((sum(student.get("grades")))/len(student.get("grades")))
    print(student.get("name") + " has an average grade of " + (str(avg)))

movies = [ {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3}, 
          {"title": "The Godfather", "genre": "Crime", "rating": 9.2}, 
          {"title": "The Dark Knight", "genre": "Action", "rating": 9.0}, 
          {"title": "Pulp Fiction", "genre": "Crime", "rating": 8.9}, 
          {"title": "Schindler's List", "genre": "Drama", "rating": 8.9} ]
rating = 0
for movie in movies:
    if movie.get("rating") > rating:
        rating = movie.get("rating")
        title = movie["title"]
        genre = movie["genre"]


print("movie name: "+ str(title)+" genre: "+str(genre)+" rating: "+str(rating))
