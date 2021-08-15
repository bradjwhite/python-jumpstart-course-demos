def main():
    d = {
        'city': 'Portland',
        'state': 'ME',
        'details': ['Cold', 'Snowy', 'Winter']
    }

    print(d.get('country', 'USA'))
    d['country']