from collections import Counter
import string
import pandas as pd
import math
from functools import reduce
import random
from sqlalchemy import create_engine, Column, Integer, TIMESTAMP, JSON, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
def one():
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sub_list = ["h", "i", "j"]
    list1[2][1][2].extend(sub_list)
    print(list1)
    # ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

# one()
def two():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    my_dict = {}
    for i, key in enumerate(keys):
       my_dict[key] = values[i]
    print(my_dict)
# two()
def three():
    sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
     }
    keys = ["name", "salary"]
    for i in keys:
        if i in sample_dict:
            del sample_dict[i]
    print(sample_dict)
# three()   
def four():
   sample_dict = {
     "name": "Kelly",
     "age":25,
     "salary": 8000,
     "city": "New york"
    }
   sample_dict['location']=sample_dict.pop('city')
   print(sample_dict)
# four() 
def five():
    sample_dict = {
      'Physics': 82,
      'Math': 65,
      'history': 75
     }
    print(min(sample_dict))
# five() 
def six1():
    with open("sample.txt", "w") as f:
        l = "This function reads a line from a file and returns it as a string. It reads at most n bytes for the specified n. But even if n is greater than the length of the line, it does not read more than one line. The code above shows that the function is returning the letter based on the number specified to it, while the function is returning every string assigned to including the . That is, the function will print out all data in the file."
        f.write(l)
    with open('sample.txt', 'r') as file:
        file_contents = file.read()
        word = 'sugumar'
        if word in file_contents:
            print("yes")
        else:
            print("no")
# six1()
def six2():
    word_freq_counter = Counter()
    with open('sample.txt', 'r') as file:
        file_contents = file.read()
        lower = file_contents.lower()
        words = lower.split()
        word_freq_counter.update(words)
        print(word_freq_counter)
# six2()
def seven():
    
        data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
        df = pd.DataFrame(data)
        for index, row in df.iterrows():
            print(f'Index: {index}, A: {row["A"]}, B: {row["B"]}')
        for row in df.itertuples():
            print(f'Index: {row.Index}, A: {row.A}, B: {row.B}')
        def my_function(row):
            return row['A'] + row['B']
        df['C'] = df.apply(my_function, axis=1)
        print(df)
        df['D'] = df['A'].map(lambda x: x * 2)
        print(df['D'])

# seven()
def eight():
        n = [1, 2, 3, 4, 5]
        squared_numbers = map(lambda x: x**2, n)
        print("Squared Numbers:", list(squared_numbers))

        even_numbers = filter(lambda x: x % 2 == 0, n)
        print("Even Numbers:", list(even_numbers))

        product = reduce(lambda x, y: x * y, n)
        print("Product of Numbers:", product)
        
# eight()
def nine():
    list1= [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    list2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("Original List:", list1)
    print("og2",list2)
    sorted_list = sorted(list1)
    list2.sort()
    print("Sorted List:", sorted_list)
    print("with sort",list2)
# nine()  
def ten():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def detail(self):
            print("name:", self.name)
            print("age:", self.age)

    person1 = Person('Shuruthi', 3)
    person1.detail()

    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            print(math.pi * self.radius ** 2)

    class Rectangle:
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
            print(self.length * self.width)

    circle_op = Circle(6)
    rect_op = Rectangle(3,5)
    print("Circle Area:")
    circle_op.area()
    print("Rectangle Area:")
    rect_op.area()

# ten()
def eleven():

        def generate_random_number():
            return str(random.randint(10000, 99999))

        def evaluate_guess(actual, guessed):
            wrong = "A"
            wrong_position = "B"
            correct = "C" 
            feedback = ""
            for i in range(len(guessed)):
                if int(guessed[i]) == int(actual[i]):
                    feedback += correct
                elif guessed[i] in actual:
                    feedback += wrong_position
                else:
                    feedback += wrong   
            return feedback
        def find_number():
            guess_number = generate_random_number()
            print(guess_number)
            print("5-digit number.")
            print("  A - Wrong digit, B - Right digit but wrong position, C - Correct digit and position")
            
            for attempt in range(1, 6):
                print("\nAttempt:", attempt)
                guessed_number = input("Enter 5-digit guess: ")
                
                if guessed_number == guess_number:
                    print("correct number:", guess_number)
                    break
                else:
                    feedback = evaluate_guess(guess_number, guessed_number)
                    print(feedback)
            
            else:
                print("Sorry,out of attempts. The correct number was:", guess_number)
        find_number()

   
# eleven()
def twelve():
    data = [
        {"roll_no": 1, "name": "John", "games": ["cricket", "football"],
        "marks": {"maths": 90, "science": 93, "history": 81}, "rank": 1},
        {"roll_no": 2, "name": "Mick", "games": ["football", "hockey"],
        "marks": {"maths": 95, "science": 86, "cs": 70}, "rank": 2},
        {"roll_no": 3, "name": "June", "games": ["badminton", None],
        "marks": {"maths": 92, "science": 92, "geography": 78}, "rank": 3},
        {"roll_no": 4, "name": "Adam", "games": ["soccer", "badminton"],
        "marks": {"maths": 86, "science": 91, "cs": 82}, "rank": 4},
        {"roll_no": 5, "name": "Robb", "games": ["cricket", None],
        "marks": {"maths": 88, "science": 90, "economics": 84}, "rank": 5},
        {"roll_no": 6, "name": "Arya", "games": ["football", "hockey"],
        "marks": {"maths": 89, "science": 88, "history": 97}, "rank": 6}
    ]
    df = pd.DataFrame(data)
    cs_students = df[df['marks'].apply(lambda x: 'cs' in x.keys() if isinstance(x, dict) else False)]
    print(cs_students)
    df['Percentage'] = df['marks'].apply(lambda x: (3 * x.get('maths', 0) + 2 * x.get('science', 0) +
                                                    sum([v for k, v in x.items() if k not in ['maths', 'science']])))
    df['Percentage'] /= 6
    df['games'] = df['games'].apply(lambda x: [game for game in x if pd.notnull(game)])
    print(df)
    df['Previous Rank'] = df['rank']
    df['rank'] = df['Percentage'].rank(ascending=False).astype(int)
    df['Change in Rank'] = df.apply(lambda x: -(x['rank'] - x['Previous Rank']) if x['rank'] != x['Previous Rank'] else '-', axis=1)

    result_df = df[['name', 'Percentage', 'Previous Rank', 'rank', 'Change in Rank']].sort_values(by='rank')

    print(result_df)    
    
twelve()
# def fourteen():
     
#     from sqlalchemy import create_engine, Column, Integer, TIMESTAMP, JSON, func
#     from sqlalchemy.ext.declarative import declarative_base
#     from sqlalchemy.orm import sessionmaker

#     DATABASE_URL = "postgresql://postgres:sugu2002@localhost:5433/sugumar"
#     engine = create_engine(DATABASE_URL)

#     Base = declarative_base()

#     class AttributeIssueCount(Base):
#         # ... (same as in your code)

#     class DatasetIssueCount(Base):
#         # ... (same as in your code)

#     class DatasourceIssueCount(Base):
#         # ... (same as in your code)

#     Base.metadata.create_all(bind=engine)

#     Session = sessionmaker(bind=engine)
#     session = Session()

#     attribute_records = [
#         (1664, 322384, 1, '2023-11-01 00:00:00.000000', 1, '{"44961": 1}', 55396, 1485),
#         # ... (replace with other records)
#     ]

#     dataset_records = [
#         (1664, 55396, 3, '2023-11-01 00:00:00.000000', 1, '{"44961": 1, "44967": 1, "44982": 1}', 1485),
#         # ... (replace with other records)
#     ]

#     for record in attribute_records:
#         session.add(AttributeIssueCount(tenant_id=record[0], integration_id=record[1], meta_data_id=record[2],
#                                         created_month=record[3], issue_count=record[4], issue_details=record[5],
#                                         data_set_id=record[6], env_id=record[7]))

#     for record in dataset_records:
#         session.add(DatasetIssueCount(tenant_id=record[0], integration_id=record[1], data_set_id=record[2],
#                                     created_month=record[3], issue_count=record[4], issue_details=record[5],
#                                     env_id=record[6]))

#     session.commit()

#     result = (
#         session.query(DatasetIssueCount.integration_id,
#                     func.sum(DatasetIssueCount.issue_count).label('total_issue_count_dataset_level'),
#                     func.jsonb_object_agg(DatasetIssueCount.issue_details).label('total_issue_details_dataset_level'),
#                     func.sum(AttributeIssueCount.issue_count).label('total_issue_count_attribute_level'),
#                     func.jsonb_object_agg(AttributeIssueCount.issue_details).label('total_issue_details_attribute_level'))
#         .join(AttributeIssueCount, DatasetIssueCount.integration_id == AttributeIssueCount.integration_id)
#         .group_by(DatasetIssueCount.integration_id)
#         .all()
#     )

#     for row in result:
#         session.add(DatasourceIssueCount(tenant_id=1664, integration_id=row[0],
#                                         issue_count_dataset_level=row[1], issue_details_dataset_level=row[2],
#                                         issue_count_attribute_level=row[3], issue_details_attribute_level=row[4]))

#     session.commit()
#     session.close()
# fourteen()    
   
          

 
    

    
      
    

        

