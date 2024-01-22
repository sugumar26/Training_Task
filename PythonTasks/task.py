import pandas as pd, numpy as np
from pyspark.sql import Row, SparkSession
import time
from functools import reduce
import math, random as rd
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, JSON, TIMESTAMP
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import json
from collections import defaultdict
from sqlalchemy import Boolean

def extend_and_addSubList():

    extend_list =  ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sub_list = ["h", "i", "j"]
    
    for i in range(len(sub_list)):
     extend_list[2][1][2].extend([sub_list[i]]) 

    print(len(extend_list))


def list_to_dict():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    res = dict(map(lambda i,j : (i,j) , keys,values))
    print(res)


def delete_keys():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    my_dict_copy = sample_dict.copy()
    keys = ["name", "salary"]
    
    for key,value in sample_dict.items():
      if key in keys:
          del my_dict_copy[key]
    print(my_dict_copy)

def rename_key():
    sample_dict = {
    "name": "Kelly",
    "age":25,
    "salary": 8000,
    "city": "New york"
    }
    sample_dict['location'] = sample_dict.pop('city')
    print(sample_dict)



def min_from_dict():
    sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
    }
    min_value = None
    min_key = None

    for key, value in sample_dict.items():
        if min_value is None or value < min_value:
            min_value = value
            min_key = key


    min_pair = {min_key: min_value}
    print(min_pair)
        



class reading_files():
    def checkWord(word):
        file = open("file.txt", "r")
        for line in file:
            if word in line:
                return True
        return False
    
    def count_word(filename):
        count_words = {}
        with open(filename,'r') as file:   
         for line in file:        
            for word in line.split(): 
                if word in count_words: 
                    count_words[word] += 1
                else:      
                     count_words[word] = 1
        print(count_words)
            

def pandas_dataframe():
            read_data = pd.read_csv('industry_data.csv')
            itter_df = pd.DataFrame(read_data)

            start_time = time.time()
            years = []
            values = []

            for index, row in itter_df.iterrows():
                if row["year"] == 2011 and row ["value"] == "32155":
                    years.append(row["year"])
                    values.append(row["value"])

            print("Years:", years)
            print("Values:", values)
            print("Time taken itterows:", time.time() - start_time)
            years1 = []
            values1 = []
            for row in itter_df.itertuples():
                if row.year == 2011 and row.value == "32155":
                    years1.append(row.year)
                    values1.append(row.value)

            print("Years:", years)
            print("Values:", values)
            print("Time taken itertuples:", time.time() - start_time)
            
            new  = itter_df.apply(lambda year:year)
            
            
    
       

def lambda_funtion():
    names = ["vijay" , "ajai" , "rahul" , "bob" , "kumar" , "ramesh"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in names:
        print(i)
        map_names = list(map(lambda x:x,names))
    print(map_names.index("vijay"))

    namewith_A = list(filter(lambda x: 'a' in x, names))
    print("Contains A: ", namewith_A)
    sum = reduce(lambda x, y: x + y, names)
    print("sum of all numbers:", sum) 


def sort_sorted():
    
    names = ["ajai" , "mohan" , "babu" , "cummins"]
    print(sorted(names))
    words = ["Geeks", "For", "Geeks"]
    words.sort()
    
    print(words)

class greeting:
    def __init__(self ,name , age):
        print("Hello,",name,"your age is,",age)

class circle():
    def __init__(self, radius):
        self.radius = radius
    
    def area(self ,name):
        print(math.pi * self.radius ** 2 ,name)
    
class rectangle():
    def __init__(self , length ,width):
        self.length = length
        self.width = width
        
    def area(self):
        print(self.length * self.width)
        
def find_number():
    guess_number = str(rd.randint(10000 , 100000))
    wrong = "A"
    wrong_position = "B"
    correct = "C"
    print(guess_number)
    
    for i in range(0,5):
        indicate = ""
        print(" Attempt = " ,i ,"\n" ,"Remaining = " ,5-i)
        Guessed_number = input("Enter 5 digit: ")
        if int(Guessed_number) == guess_number:
            print("Entered number is correct...")
            break
        else:
            for i in range(len(Guessed_number)):
                if (Guessed_number[i]) == guess_number[i]:
                    indicate+=correct
                elif Guessed_number[i] not in guess_number:
                    indicate+=wrong
                elif Guessed_number[i] in guess_number:
                    indicate+=wrong_position
        print(indicate)
        if indicate == "CCCCC":
            print("correct")
            break
                
                
        print("Try exceeded The number is: " , guess_number)
        
def working_data():
    data= [
    {"roll_no": 1,"name": "John", "games": ["cricket", "football"],
    "marks": {"maths": 90, "science": 93, "history": 81}, "rank": 1},
    {"roll_no": 2,"name": "Mick", "games": ["football", "hockey"],
    "marks": {"maths": 95, "science": 86, "cs": 70}, "rank": 2},
    {"roll_no": 3,"name": "June", "games": ["badminton", None],
    "marks": {"maths": 92, "science": 92, "geography": 78}, "rank": 3},
    {"roll_no": 4,"name": "Adam", "games": ["soccer", "badminton"],
    "marks": { "maths": 86 ,"science": 91, "cs": 82},"rank": 4},
    {"roll_no": 5,"name": "Robb", "games": ["cricket", None],
    "marks": {"maths": 88, "science": 90, "economics": 84}, "rank": 5},
    {"roll_no": 6,"name": "Arya", "games": ["football", "hockey"],
    "marks": {"maths": 89, "science": 88, "history": 97}, "rank": 6}
    ]
    cs_data = list(filter(lambda row: 'cs' in row['marks'] , data))
    for item in data:
        total_marks = 0
        if 'maths' in item['marks']:
            total_marks += 3 * item['marks']['maths']
        if 'science' in item['marks']:
            total_marks += 2 * item['marks']['science']
        for subject, marks in item['marks'].items():
            if subject not in ['maths', 'science']:
                total_marks += marks
        item["total_mark"] = total_marks

        item["percentage"] = (item["total_mark"] / 600) * 100
    for student in data:
        student['games'] = [game for game in student["games"] if game is not None]

    data_df = pd.DataFrame(data)
    data_df["pre_rank"] = data_df["rank"]
    data_df['new_rank'] = data_df.groupby("total_mark", sort=True).ngroup()+1
    data_df = data_df.sort_values(by="new_rank")
    data_df['change_in_ranks'] = data_df.apply([lambda row:1 if row['new_rank'] < row["pre_rank"] 
                                               else -1 if row['new_rank'] > row["pre_rank"]
                                              else '-'] , axis=1)
    data_df_rank = data_df[['name', 'percentage' , 'pre_rank' , 'new_rank' , 'change_in_ranks']].copy()

    print(data_df_rank)
    
    
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://postgres:1234@localhost/sample_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional but recommended for performance

db = SQLAlchemy(app)
class Metrics(db.Model):
    __tablename__ = 'dataset_metrics'
    refresh_count = db.Column(db.Integer, primary_key=True)
    new_row_count = db.Column(db.Integer)
    metric_threshold = db.Column(db.Integer)
    Window_size = db.Column(db.Integer)
    moving_base_average = db.Column(db.Integer)
    percent_drift = db.Column(db.Integer)
    threshold_alert = db.Column(Boolean)
    def __init__(self, refresh_count,new_row_count, metric_threshold ,Window_size, moving_base_average,percent_drift, threshold_alert):
        self.refresh_count = refresh_count
        self.new_row_count = new_row_count
        self.metric_threshold = metric_threshold
        self.Window_size = Window_size
        self.moving_base_average = moving_base_average
        self.percent_drift = percent_drift
        self.threshold_alert = threshold_alert
with app.app_context():
    db.create_all()
    
refresh_id = 1
window_list = []
@app.route("/")
def get_param(methods=["GET"]):
    global refresh_id
    base_rowcount = 50
    global window_list
    moving_base_average = 0
    percent_drift = 0
    threshold_alert = False
    refresh_id+=1
    last_row = Metrics.query.order_by(Metrics.refresh_count.desc()).first()
    if last_row is not None:
        new_row_count = int(request.args.get('new_row_count'))
        metric_threshold = int(request.args.get('metric_threshold'))
        Window_size = int(request.args.get('Window_size'))
        if last_row.moving_base_average == 0:
            percent_drift = 0
        else:
            percent_drift = ((new_row_count -last_row.moving_base_average ) / last_row.moving_base_average) * 100
        window_list.append(new_row_count)
        sumofList = sum(window_list)
        moving_base_average =sumofList  / len(window_list)
        if percent_drift >= metric_threshold:
            threshold_alert = True
        new_metric = Metrics(refresh_id , new_row_count, metric_threshold, Window_size, moving_base_average ,percent_drift ,threshold_alert)
        db.session.add(new_metric)
        db.session.commit()
    else:
        new_row_count = int(request.args.get('new_row_count'))
        metric_threshold = int(request.args.get('metric_threshold'))
        Window_size = int(request.args.get('Window_size'))
        percent_drift = 0
        Moving_average = 0
        new_metric = Metrics(refresh_id , new_row_count, metric_threshold, Window_size,  Moving_average ,percent_drift, threshold_alert)
        db.session.add(new_metric)
        db.session.commit()
        return "Base refresh completed"
        
        

    return jsonify({
        "refresh_id": refresh_id,
        "row": new_row_count,
        "threshold": metric_threshold,
        "window_size": Window_size
    })
if __name__ == "__main__":
    app.run()

class AttributeIssueCount(db.Model):
    __tablename__ = 'attribute_issue_count'

    issue_count_id = db.Column(Integer, primary_key=True, autoincrement=True)
    tenant_id = db.Column(Integer, nullable=False)
    integration_id = db.Column(Integer, nullable=False)
    meta_data_id = db.Column(Integer, nullable=False)
    created_month = db.Column(TIMESTAMP, nullable=False)
    issue_count = db.Column(Integer, nullable=False)
    issue_details = db.Column(JSON, nullable=False)
    data_set_id = db.Column(Integer, nullable=False)
    env_id = db.Column(Integer, nullable=False)

    def __init__(self, tenant_id, integration_id, meta_data_id, created_month, issue_count, issue_details, data_set_id, env_id):
        self.tenant_id = tenant_id
        self.integration_id = integration_id
        self.meta_data_id = meta_data_id
        self.created_month = created_month
        self.issue_count = issue_count
        self.issue_details = issue_details
        self.data_set_id = data_set_id
        self.env_id = env_id

class DatasetIssueCount(db.Model):
    __tablename__ = 'dataset_issue_count'

    issue_count_id =db.Column(Integer, primary_key=True ,autoincrement=True)
    tenant_id = db.Column(Integer, nullable=False)
    integration_id = db.Column(Integer, nullable=False)
    data_set_id = db.Column(Integer, nullable=False)
    created_month = db.Column(TIMESTAMP, nullable=False)
    issue_count = db.Column(Integer, nullable=False)
    issue_details = db.Column(JSON, nullable=False)
    env_id = db.Column(Integer, nullable=False)

    def __init__(self, tenant_id, integration_id, data_set_id, created_month, issue_count, issue_details, env_id):
        self.tenant_id = tenant_id
        self.integration_id = integration_id
        self.data_set_id = data_set_id
        self.created_month = created_month
        self.issue_count = issue_count
        self.issue_details = issue_details
        self.env_id = env_id
class DatasourceIssueCount(db.Model):
    __tablename__ = 'datasource_issue_count'

    issue_count_id =db.Column(Integer, primary_key=True ,autoincrement=True)
    env_id = db.Column(Integer, nullable=False)
    tenant_id = db.Column(Integer, nullable=False)
    integration_id = db.Column(Integer, nullable=False)
    created_month = db.Column(TIMESTAMP, nullable=False)
    issue_count_dataset_level = db.Column(Integer, nullable=False)
    issue_details_dataset_level = db.Column(JSON, nullable=False)
    issue_count_attribute_level = db.Column(Integer, nullable=False)
    issue_details_attribute_level = db.Column(Integer, nullable=False)

    def __init__(self, env_id , tenant_id, integration_id, created_month,
                 issue_count_dataset_level, issue_details_dataset_level,
                 issue_count_attribute_level, issue_details_attribute_level,):
        self.env_id = env_id
        self.tenant_id = tenant_id
        self.integration_id = integration_id
        self.created_month = created_month
        self.issue_count_dataset_level = issue_count_dataset_level
        self.issue_details_dataset_level = issue_details_dataset_level
        self.issue_count_attribute_level = issue_count_attribute_level
        self.issue_details_attribute_level = issue_details_attribute_level

def store_details():
    with app.app_context(): 
        attr_issue_value = AttributeIssueCount.query.all()
        dataset_issue_value = DatasetIssueCount.query.all()
        issue_count_dataset_level  =AttributeIssueCount.query.with_entities(func.sum(AttributeIssueCount.issue_count)).scalar()
        issue_count_attribute_level  = DatasetIssueCount.query.with_entities(func.sum(DatasetIssueCount.issue_count)).scalar()
       
        unique_integration = db.session.query(AttributeIssueCount.integration_id).distinct().all()
        unique_integration_ids = [result.integration_id for result in unique_integration]
        
        for integ_id in unique_integration_ids:
            attr_details = json.dumps(calculate_issue_details_count(attr_issue_value , integ_id))
            print((attr_details))
            dataset_details = json.dumps(calculate_issue_details_count(dataset_issue_value , integ_id))
            print(dataset_details)
            IntegId_Row =db.session.query(AttributeIssueCount).filter_by(integration_id=integ_id).first()
            values_issue_count = DatasourceIssueCount(
            env_id=IntegId_Row.env_id,
            tenant_id=IntegId_Row.tenant_id,
            integration_id=IntegId_Row.integration_id,
            created_month=IntegId_Row.created_month,
            issue_count_dataset_level= issue_count_dataset_level,
            issue_details_dataset_level = attr_details,
            issue_count_attribute_level=issue_count_attribute_level,
            issue_details_attribute_level = dataset_details
        )
            db.session.add(values_issue_count)
            db.session.commit()
                     
def calculate_issue_details_count(rows, integration_id):
        details_count = defaultdict(int)
        for row in rows:
            if row.integration_id == integration_id:
                issue_details = row.issue_details
                for key, value in issue_details.items():
                    details_count[key] += value
        return details_count



def value_size_threetables():
    with app.app_context(): 
       name= "packed-chart"
       chart = {"name" : name , "children": []} 
       unique_env_ids = [result[0] for result in db.session.query(AttributeIssueCount.env_id).distinct().all()]
       for  env in (unique_env_ids):
            env_data = {"env": env, "children": []}
            chart["children"].append(env_data)          
            env_integ = [result[0] for result in AttributeIssueCount.query.filter(AttributeIssueCount.env_id == env).with_entities(AttributeIssueCount.integration_id).distinct().all()]
            for integ in env_integ:
                integ_data = {"Integration_id": integ, "children": []}
                env_data["children"].append(integ_data) 
                dataset_id = [result[0] for result in AttributeIssueCount.query.filter(AttributeIssueCount.integration_id == integ).with_entities(AttributeIssueCount.data_set_id).distinct().all()]
                
                dataset_count = 0
                for dataset in dataset_id:
                    dataset_data = {"dataset_id": dataset, "children": []}
                    integ_data["children"].append(dataset_data)
                    attr_dataset_id = [result[0] for result in AttributeIssueCount.query.filter(AttributeIssueCount.data_set_id == dataset).with_entities(AttributeIssueCount.meta_data_id).all()]
                    issue_count = [result[0] for result in AttributeIssueCount.query.filter(AttributeIssueCount.data_set_id == dataset).with_entities(AttributeIssueCount.issue_count).all()]
                    
                    value = int(DatasetIssueCount.query.filter(DatasetIssueCount.data_set_id == dataset).with_entities(DatasetIssueCount.issue_count).scalar())
                    
                    result = DatasourceIssueCount.query.with_entities(
                            DatasourceIssueCount.issue_count_dataset_level,
                            DatasourceIssueCount.issue_count_attribute_level
                        ).filter(DatasourceIssueCount.integration_id == integ).first()

                    if result:
                        datasource1, datasource = map(int, result)
                    else:
                        # Handle the case where the query doesn't return any results
                        datasource1 = datasource = 0 
                    integration_count = datasource + datasource1
                    dataset_count += value
                    for attr, count in zip(attr_dataset_id, issue_count):
                         dataset_count += count
                         dataset_data["children"].append({"metadata_id":attr , "size":count})
                    dataset_data["children"].append({"value":value})           
                env_data["children"].append({"value":dataset_count})
            chart["children"].append({"value" : integration_count})
    print(chart)           

# extend_and_addSubList()
# list_to_dict()
# delete_keys()
# rename_key()
# min_from_dict()
# reading_files.count_word("file.txt")
# pandas_dataframe()
# lambda_funtion()
# sort_sorted()
# circle = circle(5)
# circle.area("vijay")
# rectangle  = rectangle(4,3)
# find_number()
# working_data()
# store_details()
# value_size_threetables()