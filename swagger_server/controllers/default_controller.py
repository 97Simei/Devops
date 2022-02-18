from swagger_server.service import student_service
from swagger_server.service.student_service import *
import connexion
import six

from swagger_server.models.student import Student  # noqa: E501
from swagger_server import util


def add_student(body=None):  # noqa: E501
    """Add a new student
    Adds an item to the system # noqa: E501
    :param body: Student item to add
    :type body: dict | bytes
    :rtype: float
    """
    if connexion.request.is_json:
        body = Student.from_dict(connexion.request.get_json())
        #noqa: E501
        return add(body)
    return 500,'error'


def delete_student(student_id):  # noqa: E501
    res = student_service.delete(student_id)
    if res:
        return res
    return 'Not Found', 404


def get_student_by_id(student_id, subject=None):  # noqa: E501
    res = student_service.get_by_id(student_id, subject=subject)
    if res:
        return res
    return 'Not Found', 404
