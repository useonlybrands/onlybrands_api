import logging
import os


def process_create_bid(data):

    return {'status': 200, 'message': 'Bid created successfully'}

def process_accepted_bid(data):
    return {'status': 200, 'message': 'Bid Accepted successfully'}


def process_complete_bid(data):
    return {'status': 200, 'message': 'Bid completed successfully'}



def process_delete_bid(data):

    return {'status': 200, 'message': 'Bid deleted'}
