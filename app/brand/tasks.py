import loggings
import os

def process_create_brand(data):
    """
    This should take the form data and the discovery token
    :param data:
    :return:
    """

    return {'status': 200, 'message': 'Brand created successfully'}


def process_delete_brand(data):
    """
    Delete the brand from the database
    :param data:
    :return:
    """

    return {'status': 200, 'message': 'Brand deleted'}
