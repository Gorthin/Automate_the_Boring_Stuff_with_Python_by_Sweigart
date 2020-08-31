# Extending the Multiclipboard
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3:  # If 3 arguments in the command line -> save or delete the 3rd agrument
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]

elif len(sys.argv) == 2:  # If 2 argument in the command line -> copy list arguments to clipboard or
    # List keywords and load content.                  # delete all list arguments
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))

    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()

    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()