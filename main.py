import movie_svc
import requests

def main():
    print_header()
    search_event_loop()

def print_header():
    pass

def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input("Movie search text (x to exit): ")
            if search != 'x':
                results = movie_svc.find_movies(search)
                print(f'Found {len(results)} results.')
                for r in results:
                    print(f'{r.year} -- {r.title}')
                print()

        #TODO: Exception should handle individual errors.  Not simply say it didn't work for any reason.
        # Try removing Internet connectivity, OR searching for nothing.
        except requests.exceptions.ConnectionError:
            print(f'Error: Network Issue')
        except ValueError:
            print(f'Search text is required.')
        except Exception as x:
            #TODO: Demonstrate Exception as x, and type(), to diagnose errors.
            #TODO: Demonstrate how a null search in the browser also breaks.
            print(f"Whoops, that didn't work. Details{x}")

        #TODO: Explain importance of specificity in errors coming first. Most -> Least

    print("exiting... ")

if __name__ == '__main__':
    main()