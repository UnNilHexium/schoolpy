# producing deliverable to make changes to file system!
#eg. - Automated
# Program file - *.py
# Data files- Text   - *.txt
#             Binary - *.bin
#                    - *.dat
#             CSV    - *.csv
#
#
#.txt - Not Secure - Read permission with everyone
#                  - Changeable
#                  - No confidentiality
#     - No structure/ Organisation
#     - Best suited for descriptive data
#     - Slowest - Has to translate bw unicode and binary
#
#           
# 1. Open file-
#       open(Arg1 , Arg2)
#       - Arg1 = flie name (if in same folder)
#       -       or file path (abs or relative)
#       - Arg2 = File Acess Mode
#                - Normal - "r", "w", "a", "r+w"/"r+", "w+r"/"w+", "a+r"/"a+"
#                - Binary - "rb", "wb", "ab", "rb+wb"/"rb+", "wb+rb"/"wb+", "ab+rb"/"ab+"
# File Pointer - assign a variable to open
#              - read byte/ work on them, goes to the next one (excusive)
#              - stop at End Of File (EOF)
# cannot open non existant file in read mode
# use w mode on non existant file - create file
# use w mode on existing file - instant wipe
# use a mode on non existant file - create file
# use a mode on existing file - add to file file