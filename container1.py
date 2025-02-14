#!/usr/bin/python3


"""Creates a file to put in a container - using modules that we don't have locally, but exist in the container.

watching 'containerize python applications with Docker - Neural 9
https://www.youtube.com/watch?v=0TFWtfFY87U&t=674s

"""

def main():
    """Main is a runner function, used to call individual functions in order."""
    pass


############### START HERE #####################
# if__name__ - will look into a hidden variable for the file, called 'dunder name', or 'double underscore name'.
# if this script is being run directly, as a script, and not just a container of functions, the
# if__name__ will run, to inspect the name of the script, which will be '__main__', and will evaluate to True.
# if __name__ is True, then go set some settings, and then go run the 'main()' function.
################################################
if __name__ == "__main__":
    main()