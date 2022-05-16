import string
import unittest

import requests
from requests import Response
from utils import get, post, put, delete, patch, ping, auth_URL, booking_URL, credentials

global booking_id
global booking_id_to_be_deleted


class TestCreateToken(unittest.TestCase):
    def test_should_create_token(self):
        resp: Response = requests.post(auth_URL, credentials)
        token: string = resp.json()['token']

        self.assertTrue(token is not None)
        self.assertEqual(200, resp.status_code)

    def test_should_fail_due_to_bad_credentials(self):
        bad_credentials = {"username": "admin",
                           "password": "password1234"}
        resp: Response = requests.post(auth_URL, bad_credentials)
        reason: string = resp.json()['reason']
        status_code: int = resp.status_code

        self.assertEqual('Bad credentials', reason)
        self.assertEqual(200, status_code)
        # self.assertEqual(401, status_code) # TODO - I would change the api logic to return 401
        # from what I read at:
        # https://www.lifewire.com/http-status-code-errors-4165131
        # its best to send 401 when getting "Bad credentials"


class TestGetBookingIds(unittest.TestCase):
    def test_should_return_bookingID_array(self):
        status_code, bookingID_array = get(booking_URL)

        self.assertTrue(len(bookingID_array) == 0 or bookingID_array[0]['bookingid'] is not None)
        self.assertEqual(200, status_code)


class TestGetBooking(unittest.TestCase):
    def test_should_return_persons_bookings_info(self):
        status_code, booking_info = get(booking_URL + '/1305')

        self.assertEqual(200, status_code)
        self.assertTrue(booking_info['firstname'] is not None)
        self.assertTrue(booking_info['lastname'] is not None)
        self.assertTrue(booking_info['totalprice'] is not None)
        self.assertTrue(booking_info['depositpaid'] is not None)
        self.assertTrue(booking_info['bookingdates'] is not None)

    def test_should_fail_with_404_if_no_such_client(
            self):  # currently, there is no booking under this id, and it would be unwise to go back with id's to 1 if there are bookings under 1305 id
        status_code, resp = get(booking_URL + '/1')

        self.assertEqual(404, status_code)


class TestCreateAndUpdateBooking(unittest.TestCase):
    def test_should_add_booking(self):
        resp: Response = post(booking_URL)
        global booking_id
        booking_id = str(resp.json()['bookingid'])

        self.assertTrue(booking_id is not None)
        self.assertEqual(200, resp.status_code)

    def test_should_update_booking(self):
        resp: Response = put(booking_URL + '/' + booking_id)

        self.assertEqual(200, resp.status_code)
        self.assertEqual('James_updated', resp.json()['firstname'])
        self.assertEqual('Brown_updated', resp.json()['lastname'])

    def test_should_update_first_and_last_name(self):  # TODO gives 400
        resp: Response = patch(booking_URL + '/' + booking_id)

        self.assertTrue(200, resp.status_code)
        self.assertEqual('James_pached', resp.json()['firstname'])
        self.assertEqual('Brown_pached', resp.json()['lastname'])


class TestDeleteBooking(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        resp: Response = post('https://restful-booker.herokuapp.com/booking')
        global booking_id_to_be_deleted
        booking_id_to_be_deleted = str(resp.json()['bookingid'])

    def test_should_delete_posted_booking(self):
        resp: Response = delete('https://restful-booker.herokuapp.com/booking/' + booking_id_to_be_deleted)
        self.assertTrue(201, resp.status_code)


class TestPing(unittest.TestCase):
    def test_should_give_true(self):
        resp: Response = ping()

        self.assertEqual(201, resp.status_code)
