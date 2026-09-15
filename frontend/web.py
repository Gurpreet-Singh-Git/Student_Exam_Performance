from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

# amazom.com/create-user

# GET - GET AN INFROMATION
# POST - CREATE SOMETHING NEW
# PUT - UPDATE
# DELETE - DELETE SOMETHING


students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    },
    2: {
        "name": "simmi",
        "age": 18,
        "class": "year 12"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None,
    age: Optional[int] = None,
    year: Optional[str] = None

@app.get("/")
def home():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="Give student id", gt=0)):
    return students[student_id]
#lt(less than), gt(greater than), le(less than =), ge(greater than =)



@app.get("/get-name/{student_id}")
def get_name(*, student_id: int,name: Optional[str] = None, test: int):            #optinal == parameters optional == parameter can be empty | but optinal use at last parameters
    for i in students:                                                             #optinal can work at any parameter by using *, which make every parameter, parameteric name (only (parameter_name=0)✔️ (direct parameter without name is ❌))
        if students[i]["name"] == name:
            return students[i]
    return "this student doesnt exist"


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"error": "student doesnt exist"}

    students[student_id] = student
    return students[student_id]

#github projects
#github name change