"""
models.py

Defines the SQLAlchemy models for the Hospital Management System.
Currently includes the Patient model.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Patient(db.Model):
    """
    Patient model representing a hospital patient.

    Attributes:
        id (int): Unique identifier for the patient.
        name (str): Full name of the patient.
        age (int): Age of the patient.
        disease (str): Disease/diagnosis of the patient.
    """

    __tablename__ = "patients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    disease = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        """Return a string representation of the Patient object."""
        return f"[id={self.id}, name={self.name}, age={self.age}, disease={self.disease}]"

    def to_dict(self):
        """Convert the Patient object into a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "disease": self.disease,
        }
