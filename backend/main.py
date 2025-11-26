from fastapi import FastAPI
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI()

json_path = Path(__file__).parent / "activity_averages.json"

with json_path.open() as f:
    activity_data = json.load(f)

def age_to_group(age: int) -> str:
    if age <= 18:
        return "15-18"
    elif age <= 27:
        return "19-27"
    elif age <= 54:
        return "28-54"
    elif age <= 64:
        return "55-64"
    else:
        return "65+"


class UserInput(BaseModel):
    age: int
    gender: int   # 1 = male, 2 = female


@app.post("/lookup")
def lookup(user: UserInput):
    age_group = age_to_group(user.age)

    matches = [
        row for row in activity_data
        if row["age_group"] == age_group and row["TESEX"] == user.gender
    ]

    if not matches:
        return {"error": "No data found"}

    return {
        "age_group": age_group,
        "gender": user.gender,
        "averages": matches[0]
    }
