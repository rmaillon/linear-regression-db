from app import db

class Result(db.Model):
    __tablename__ = "lin_reg_results"

    Id = db.Column(db.Integer, primary_key = True)
    Name = db.Column(db.String())
    YearsExperience = db.Column(db.Float)
    Prediction = db.Column(db.Float)

    def __init__(self, Name, YearsExperience, Prediction):
        self.Name = Name
        self.YearsExperience = YearsExperience
        self.Prediction = Prediction
