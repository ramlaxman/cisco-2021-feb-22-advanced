import sys


class TempOutput:
    def __init__(self, outfilename):
        print(f'Now in TempOutput.__init__, outfilename = {outfilename}')
        self.outfile = open(outfilename, 'w')
        self.old_stdout = None

    def __enter__(self):
        print(f'Now in TempOutput.__enter__')
        self.old_stdout = sys.stdout
        sys.stdout = self.outfile
        return self

    def __exit__(self, ex_type, ex_obj, ex_backtrace):
        print(f'Now in TempOutput.__exit__')
        sys.stdout = self.old_stdout
        self.old_stdout = None
        self.outfile.close()


print('Before')
with TempOutput('tempout.txt'):
    # __enter__
    print('Hello')
    # __exit__

print('After')