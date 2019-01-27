import movie_svc

def main():
    print_header()
    search_event_loop()

def print_header():
    pass

def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        search = input("Movie search text (x to exit): ")
        if search != 'x':
            results = movie_svc.find_movies(search)
            print(f'Found {len(results)} results.')
            for r in results:
                print(f'{r.year} -- {r.title}')
            print()

    print("exiting... ")

if __name__ == '__main__':
    main()