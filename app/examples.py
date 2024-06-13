from requests import request

# change this based on your server
url = 'http://127.0.0.1:5000'


def get_mine():
    return request('GET', url + '/mine')


def post_transactions():
    context = {
        'sender': 'A',
        'recipient': 'B',
        'amount': 1
    }
    return request('POST', url + '/transactions/new', json=context)


def get_chain():
    return request('GET', url + '/chain')


def post_nodes_register():
    context = {
        'nodes': ['http://127.0.0.1:5001', 'http://127.0.0.1:5002']
    }
    return request('POST', url + '/nodes/register', json=context)


def get_nodes_resolve():
    return request('GET', url + '/nodes/resolve')


# status codes : 200, 201, 400, 404, 500
if __name__ == '__main__':
    print(get_mine())
    print(post_transactions())
    print(get_chain())
    print(post_nodes_register())
    print(get_nodes_resolve())
