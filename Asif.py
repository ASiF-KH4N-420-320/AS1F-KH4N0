import os, platform
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            import asif64
        elif bit == '32bit':
            import asifvv
Run()
