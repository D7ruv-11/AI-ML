class Book:
    def __init__(self,title,author,list_of_review):
        self.title = title,
        self.author = author ,
        self.list_of_review = list_of_review  

    def new_review(self,review):
        self.list_of_review.append(review)
    
    def count_review(self):
        return len(self.list_of_review)
        
    def display(self):
        return self.list_of_review
    

b = Book(
    "atomic habbits ",
    "Dhruv ",
    ["good","nice"]
)
print(b.display())



