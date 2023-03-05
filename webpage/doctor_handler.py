from enum import Enum

Speciality = Enum(
    "Speciality",
    [
        "CARDIOLOGIST",
        "DENTIST",
        "DERMATOLOGIST",
        "ENDOCRINOLOGIST",
        "GASTROENTEROLOGIST",
        "GENERAL_PRACTITIONER",
        "GYNECOLOGIST",
        "HEMATOLOGIST",
        "INFECTIOUS_DISEASES_SPECIALIST",
        "NEPHROLOGIST",
        "NEUROLOGIST",
        "NEUROSURGEON",
        "OBSTETRICIAN",
        "ONCOLOGIST",
        "OPHTHALMOLOGIST",
        "ORTHOPEDIST",
        "OTORHINOLARYNGOLOGIST",
        "PEDIATRICIAN",
        "PHYSIATRIST",
        "PSYCHIATRIST",
        "RADIOLOGIST",
        "RHEUMATOLOGIST",
        "SURGEON",
        "UROLOGIST",
    ],
)

Insurence = Enum("Insurence", ["ALINA_HEALTH", "ALLIANZ", "ASANATOARE"])

Language = Enum("Language", ["ENGLISH", "FRENCH", "GERMAN", "ITALIAN", "SPANISH"])

Gender = Enum("Gender", ["NO_PREFERENCE", "MALE", "FEMALE", "NON_BINARY"])

