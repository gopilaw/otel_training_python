import json

import web

import postgres_manual_instrumentation
import transformers

urls = (
    # get all
    '/all_rooms', 'all_rooms',
    '/all_reservations', 'all_reservations',
    '/all_users', 'all_users',

    # get particular
    '/rooms/(.*)', 'get_room',
    '/reservations/(.*)', 'get_reservation',
    '/users/(.*)', 'get_user',

    # post/add particular
    '/add_room', 'add_room',
    '/add_reservation', 'add_reservation',
    '/add_user', 'add_user',

    # get fail
    '/fail', 'fail',
    '/amazing_python', 'amazing_python'
)

app = web.application(urls, globals())


class all_rooms:
    def GET(self):
        return postgres_manual_instrumentation.get_all('rooms', transformers.roomer)


class all_reservations:
    def GET(self):
        return postgres_manual_instrumentation.get_all('reservations', transformers.reservator)


class all_users:
    def GET(self):
        return postgres_manual_instrumentation.get_all('users', transformers.useror)


class get_room:
    def GET(self, item_id):
        return postgres_manual_instrumentation.get_item('rooms', 'room_id', item_id, transformers.roomer)


class get_reservation:
    def GET(self, item_id):
        return postgres_manual_instrumentation.get_item('reservations', 'reservation_id', item_id,
                                                        transformers.reservator)


class get_user:
    def GET(self, item_id):
        return postgres_manual_instrumentation.get_item('users', 'user_id', item_id, transformers.useror)


class add_room:
    def POST(self):
        data = json.loads(web.data().decode('utf-8'))
        return postgres_manual_instrumentation.insert_room(data)


class add_reservation:
    def POST(self):
        data = json.loads(web.data().decode('utf-8'))
        return postgres_manual_instrumentation.insert_reservation(data)


class add_user:
    def POST(self):
        data = json.loads(web.data().decode('utf-8'))
        return postgres_manual_instrumentation.insert_user(data)


class fail:
    def GET(self):
        return postgres_manual_instrumentation.fail('users', transformers.useror)


class amazing_python:
    def GET(self):
        return postgres_manual_instrumentation.amazing_python('users', transformers.useror)


if __name__ == "__main__":
    app.run()
