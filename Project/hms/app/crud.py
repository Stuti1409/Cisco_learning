"""
crud.py

This module provides CRUD (Create, Read, Update, Delete) operations
for managing patient records in the Hospital Management System.
"""

from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.models import db, Patient
from app.exceptions import PatientNotFoundError, DatabaseError
from app.logger import logger


def create_patient(patient):
    """
    Create a new patient record in the database.

    Args:
        patient (dict): Patient data containing 'id', 'name', 'age', 'disease'.

    Returns:
        dict: The newly created patient record as a dictionary.

    Raises:
        DatabaseError: If a duplicate ID exists or a database error occurs.
    """
    try:
        patient_model = Patient(
            id=patient["id"],
            name=patient["name"],
            age=patient["age"],
            disease=patient["disease"],
        )
        db.session.add(patient_model)
        db.session.commit()
        logger.info("Patient created: %s", patient)
        return patient_model.to_dict()
    except IntegrityError as e:
        db.session.rollback()
        logger.error("Duplicate patient ID %s - %s", patient["id"], e)
        raise DatabaseError(
            f"Patient with ID {patient['id']} already exists"
        ) from e
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error("Database error while creating patient: %s", e)
        raise DatabaseError(str(e)) from e


def read_all_patients():
    """
    Retrieve all patient records from the database.

    Returns:
        list[dict]: A list of patient records as dictionaries.

    Raises:
        DatabaseError: If a database error occurs.
    """
    try:
        patients = db.session.query(Patient).all()
        logger.info("Read all patients, count: %s", len(patients))
        return [patient.to_dict() for patient in patients]
    except SQLAlchemyError as e:
        logger.error("Database error while reading all patients: %s", e)
        raise DatabaseError(str(e)) from e


def read_model_by_id(patient_id):
    """
    Retrieve a Patient model instance by ID.

    Args:
        patient_id (int): The ID of the patient to fetch.

    Returns:
        Patient | None: Patient model object if found, else None.

    Raises:
        DatabaseError: If a database error occurs.
    """
    try:
        return db.session.query(Patient).filter_by(id=patient_id).first()
    except SQLAlchemyError as e:
        logger.error("Database error while reading patient %s: %s", patient_id, e)
        raise DatabaseError(str(e)) from e


def read_by_id(patient_id):
    """
    Retrieve a patient record by ID as a dictionary.

    Args:
        patient_id (int): The ID of the patient to fetch.

    Returns:
        dict: Patient record as a dictionary.

    Raises:
        PatientNotFoundError: If no patient with the given ID exists.
        DatabaseError: If a database error occurs.
    """
    patient = read_model_by_id(patient_id)
    if not patient:
        logger.error("Patient %s not found", patient_id)
        raise PatientNotFoundError(patient_id)
    return patient.to_dict()


def update(patient_id, new_patient):
    """
    Update an existing patient record.

    Args:
        patient_id (int): The ID of the patient to update.
        new_patient (dict): Updated patient data.

    Returns:
        dict: Updated patient record as a dictionary.

    Raises:
        PatientNotFoundError: If the patient does not exist.
        DatabaseError: If a database error occurs.
    """
    patient = read_model_by_id(patient_id)
    if not patient:
        logger.error("Patient %s not found for update", patient_id)
        raise PatientNotFoundError(patient_id)
    try:
        patient.name = new_patient["name"]
        patient.age = new_patient["age"]
        patient.disease = new_patient["disease"]
        db.session.commit()
        logger.info("Patient %s updated: %s", patient_id, new_patient)
        return patient.to_dict()
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error("Database error while updating patient %s: %s", patient_id, e)
        raise DatabaseError(str(e)) from e


def delete_patient(patient_id):
    """
    Delete a patient record by ID.

    Args:
        patient_id (int): The ID of the patient to delete.

    Returns:
        bool: True if deletion was successful.

    Raises:
        PatientNotFoundError: If the patient does not exist.
        DatabaseError: If a database error occurs.
    """
    patient = read_model_by_id(patient_id)
    if not patient:
        logger.error("Patient %s not found for deletion", patient_id)
        raise PatientNotFoundError(patient_id)
    try:
        db.session.delete(patient)
        db.session.commit()
        logger.info("Patient %s deleted", patient_id)
        return True
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error("Database error while deleting patient %s: %s", patient_id, e)
        raise DatabaseError(str(e)) from e
